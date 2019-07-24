import pprint
import time
from instagram import Account, WebAgentAccount, CheckpointException
from config import USERNAME, PASSWORD, INSTA_ACC


login = Account(USERNAME)
pw = PASSWORD
base_acc = Account(INSTA_ACC)
settings = {}

agent = WebAgentAccount(login)
agent_url = ''
agent_code = ''
try:
    agent.auth(pw)
except CheckpointException as e:
    agent_url = e.checkpoint_url
    ch_handle = agent.checkpoint_handle(e.checkpoint_url, settings=settings)
    agent.checkpoint_send(checkpoint_url=e.checkpoint_url, forward_url=ch_handle['navigation']['forward'], choice = min([x['value'] for x in e.types ]), settings=settings)
    print('enter code')
    agent_code = str(input())
    agent.checkpoint(agent_url, agent_code)
    




def fl(): 
    for i in ac[0]: 
        a = Account(i) 
        agent.update(a) 
        bio = a.biography 
        if 'CEO' in bio or 'Founder' in bio or 'founder' in bio or 'owner' in bio or 'Owner' in bio: 
            print(f'https://www.instagram.com/{a}/') 
    ab = agent.get_followers(account=base_acc, pointer=ac[1], count=5, limit=2, delay=5) 
    return ab


ac = agent.get_followers(base_acc)

for i in range(100):
    ac = fl()
