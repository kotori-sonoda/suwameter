# coding: utf8

from requests_oauthlib import OAuth1Session
import falcon
import json
import mysql.connector
import dbconf

class MembersResource:
    def on_get(self, req, resp):
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
            cur.execute('select name, display_name, display_full_name, count from member order by count desc')
            rows = cur.fetchall()
            members = []
            for row in rows:
                members.append({
                    'name': row[0],
                    'displayName': row[1].encode('utf8'),
                    'displayFullName': row[2].encode('utf8'),
                    'count': row[3]
                })
        finally:
            cur.close()
            conn.close()

        msg = {
            'members': members
        }
        resp.body = json.dumps(msg)
        resp.append_header('Access-Control-Allow-Origin', '*')

class PhotosResource:
    def on_get(self, req, resp, name):
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
            cur.execute('select distinct url from photo where name=\'%s\'' % name)
            rows = cur.fetchall()
        finally:
            cur.close()
            conn.close()

        photos = [row[0] for row in rows]

        msg = {
            'photos': photos
        }
        resp.body = json.dumps(msg)
        resp.append_header('Access-Control-Allow-Origin', '*')

class SuwawaResource:
    def on_get(self, req, resp):
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
            cur.execute('select url from suwawa')
            rows = cur.fetchall()
        finally:
            cur.close()
            conn.close()

        photos = [row[0] for row in rows]

        msg = {
            'photos': photos
        }
        resp.body = json.dumps(msg)
        resp.append_header('Access-Control-Allow-Origin', '*')

api = falcon.API()
api.add_route('/members', MembersResource())
api.add_route('/photos/{name}', PhotosResource())
api.add_route('/suwawa', SuwawaResource())
