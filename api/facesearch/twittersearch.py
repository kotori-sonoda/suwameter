# coding:utf8

from requests_oauthlib import OAuth1Session
import json
import time
import constants
import identify as i

def query_twitter(kwd, count, times, since_id):
    session = OAuth1Session(
        constants.TW_CONSUMER_KEY,
        constants.TW_CONSUMER_SEC,
        constants.TW_ACCESS_TOKEN,
        constants.TW_ACCESS_TOKEN_SEC
    )

    url = 'https://api.twitter.com/1.1/search/tweets.json'

    print('Querying Twitter...')
    res = json.loads(session.get(url, params = {'q':'%s filter:images' % kwd, 'count':count, 'result_type':'recent', 'include_entities':'true', 'since_id':since_id}).text)

    if len(res['statuses']) == 0:
        return [], 0

    links = []
    min_id = res['statuses'][0]['id']
    max_id = 0
    for tw in res['statuses']:
        if tw ['id'] > max_id:
            max_id = tw['id']
        if 'extended_entities' in tw:
            for media in tw['extended_entities']['media']:
                links.append(media['media_url'])
        else:
            if 'media' in tw['entities']:
                for media in tw['entities']['media']:
                    links.append(media['media_url'])
        if tw['id'] < min_id:
            min_id = tw['id']

    for i in range(1, times):
        res = json.loads(session.get(url, params = {'q':'%s filter:images' % kwd, 'count':count, 'result_type':'recent', 'include_entities':'true', 'since_id':since_id, 'max_id':min_id}).text)

        if len(res['statuses']) == 0:
            return links, max_id

        min_id = res['statuses'][0]['id']
        for tw in res['statuses']:
            if tw ['id'] > max_id:
                max_id = tw['id']
            if 'extended_entities' in tw:
                for media in tw['extended_entities']['media']:
                    links.append(media['media_url'])
            else:
                if 'media' in tw['entities']:
                    for media in tw['entities']['media']:
                        links.append(media['media_url'])
            if tw['id'] < min_id:
                min_id = tw['id']

    return links, max_id

def identify(links, person_group):
    personmap = {}
    for k, v in constants.PEOPLE[person_group].items():
        personmap[v] = []
    for link in links:
        people_found = i.identify_person(False, link, person_group)
        if len(people_found) > 0:
            for p in people_found:
                personmap[p].append(link)
    return personmap
