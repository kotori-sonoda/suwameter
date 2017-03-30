#!/usr/bin/python
# coding:utf8

from requests_oauthlib import OAuth1Session
import json
import mysql.connector
import dbconf
import facesearch.constants as const

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
    cur.execute('select display_name, count from member order by count desc')
    rows = cur.fetchall()
    msg ='''
すわわがハグしたいのは・・・

1位 %s: %d
2位 %s: %d
3位 %s: %d

すわわがハグしたい人メーター
http://suwameter.sato-t.net/
#lovelive #lovelive_shushine
''' % (rows[0][0].encode('utf8'), rows[0][1], rows[1][0].encode('utf8'), rows[1][1], rows[2][0].encode('utf8'), rows[2][1])
finally:
    cur.close()
    conn.close()

session = OAuth1Session(
    const.TW_CONSUMER_KEY,
    const.TW_CONSUMER_SEC,
    const.TW_ACCESS_TOKEN,
    const.TW_ACCESS_TOKEN_SEC
)

url = 'https://api.twitter.com/1.1/statuses/update.json'
params = {'status': msg}
res = session.post(url, params=params)
