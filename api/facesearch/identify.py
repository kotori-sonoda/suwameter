# coding:utf8

import httplib
import json
import constants
import face as f

def _request(method, host, path, header, body):
    conn = httplib.HTTPSConnection(host)
    conn.request(method, path, body, header)
    response = conn.getresponse()
    return response.read()

def identify_person(is_local, src, person_group):
    print('Identifying person...')
    header = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': constants.COGNITIVE_KEY
    }

    if is_local:
        face_ids = f.get_face_id_by_file(src)
    else:
        face_ids = f.get_face_id_by_url(src)

    if len(face_ids) == 0:
        return []

    body = {
        'faceIds': face_ids,
        'personGroupId': person_group
    }

    data = json.loads(_request('POST', constants.COGNITIVE_HOST, '/face/v1.0/identify', header, json.dumps(body)))
    try:
        if 'error' in data:
            print(data)
            return []
        result = []
        for face in data:
            face_id = face['faceId']
            if len(face['candidates']) == 0:
                return []
            for candidate in face['candidates']:
                result.append(constants.PEOPLE[person_group][candidate['personId']])
        return result
    except KeyError:
        print(data)
        return []
