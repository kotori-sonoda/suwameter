#!/usr/bin/python
# coding: utf8

import sys
import mysql.connector
import facesearch.twittersearch as tw
import dbconf

if __name__ == '__main__':
    mode = sys.argv[1]

    conn = mysql.connector.connect(
        host=dbconf.HOST,
        port=dbconf.PORT,
        db=dbconf.DB_NAME,
        user=dbconf.DB_USER,
        password=dbconf.DB_PASSWORD,
        charset=dbconf.DB_CHARSET
    )
    cur = conn.cursor(buffered=True)

    try:
        base_max_id = 0
        if mode != 'init':
            cur.execute('select id from max_id')
            base_max_id = cur.fetchall()[0][0]

        links, max_id1 = tw.query_twitter('suwa nanaka', 100, 1, base_max_id)
        links2, max_id2 = tw.query_twitter('諏訪ななか', 100, 1, base_max_id)
        links3, max_id3 = tw.query_twitter('すわわ', 100, 1, base_max_id)
        links4, max_id4 = tw.query_twitter('ラブライブ', 100, 1, base_max_id)
        links5, max_id5 = tw.query_twitter('Aqours', 100, 1, base_max_id)
        links6, max_id6 = tw.query_twitter('ふわさた', 100, 1, base_max_id)
        links7, max_id7 = tw.query_twitter('サンシャイン', 100, 1, base_max_id)

        links.extend(links2)
        links.extend(links3)
        links.extend(links4)
        links.extend(links5)
        links.extend(links6)
        links.extend(links7)

        max_id = max(max_id1, max_id2, max_id3, max_id4, max_id5, max_id6, max_id7)

        if max_id > 0:
            cur.execute('update max_id set id=%d' % max_id)
            conn.commit()
    except Exception as e:
        with open('~/suwawa-hug-meter/error.log', 'a') as f:
            f.write(e)
            f.flush()
    finally:
        cur.close()
        conn.close()

    links = list(set(links))
    print '%d images to be processed...' % len(links)
    personmap = tw.identify(links, 'aqours')

    conn = mysql.connector.connect(
        host=dbconf.HOST,
        port=dbconf.PORT,
        db=dbconf.DB_NAME,
        user=dbconf.DB_USER,
        password=dbconf.DB_PASSWORD,
        charset=dbconf.DB_CHARSET
    )
    cur = conn.cursor(buffered=True)

    try:
        for k, v in personmap.items():
            if k == 'nanaka_suwa':
                continue
            for url in v:
                cur.execute('insert into photo(name, url) values(\'%s\', \'%s\')' % (k, url))
            cur.execute('select distinct url from photo where name=\'%s\'' % k)
            count = len(cur.fetchall())
            cur.execute('update member set count=%d where name=\'%s\'' % (count, k))
            conn.commit()
    except Exception as e:
        with open('~/suwawa-hug-meter/error.log', 'a') as f:
            f.write(e)
            f.flush()
    finally:
        cur.close()
        conn.close()

