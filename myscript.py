import pprint
import time
import os
from instagram import Account, WebAgentAccount, CheckpointException, InternetException, UnexpectedResponse
from config import USERNAME, PASSWORD, INSTA_ACC
from custom_config import API_CODE, API_LINKS 
import requests

first_profile = True
fp_name = ''

def fl():
    global fp_name
    global first_profile
    for i in ac[0]:
        if i == fp_name:
            first_profile = False
        if fp_name == '':
            fp_name = i
        a = Account(i) 
        agent.update(a) 
        bio = a.biography 
        if 'CEO' in bio or 'Founder' in bio or 'founder' in bio or 'owner' in bio or 'Owner' in bio: 
            link = f'https://www.instagram.com/{a}/' 
            print(link)
            requests.post(API_LINKS, data={'link': link})
    ab = agent.get_followers(account=base_acc, pointer=ac[1], count=5, limit=2, delay=5) 
    return ab

login = Account(USERNAME)
pw = PASSWORD
base_acc = Account(INSTA_ACC)
settings = {}

agent = WebAgentAccount(login)

agent_url = ''
agent_code = ''
auth_failed = True


try:
    agent.auth(pw)
except CheckpointException as e:
    is_fail = True
    agent_url = e.checkpoint_url
    ch_handle = agent.checkpoint_handle(e.checkpoint_url, settings=settings)
    agent.checkpoint_send(checkpoint_url=e.checkpoint_url, forward_url=ch_handle['navigation']['forward'], choice = min([x['value'] for x in e.types ]), settings=settings)
    while is_fail:
        try:
            api_req = requests.get(API_CODE)
            agent_code = api_req.json()[-1]['value']
            print(agent_code)
            agent.checkpoint(agent_url, agent_code)

            is_fail = False
        except Exception:
            time.sleep(30)
            continue

    
# while auth_failed:
#     try:
#         print(agent_code)
#         time.sleep(5)
#         agent.auth(pw)
#         time.sleep(2)
#         auth_failed = False
#     except Exception as e:

    



ac = agent.get_followers(base_acc)




while first_profile is True:
    try:
        ac = fl()
    except InternetException:
        time.sleep(3)
        ac = fl()

