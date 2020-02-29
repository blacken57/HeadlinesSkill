import requests
import json
import time
import unidecode
import random
def get_headlines():
    user_pass_dict = {
        'user': 'Blacken57',
        'passwd': 'agarm@x57',
        'api_type': 'json'}
    sess = requests.Session()
    sess.headers.update({'User-Agent':'This is for skills'})
    sess.post('https://www.reddit.com/api/login',data = user_pass_dict)
    time.sleep(1)
    url = 'https://reddit.com/r/worldnews/.json?limit=10'
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = [unidecode.unidecode(listing['data']['title'])for listing in data['data']['children']]
    #titles = '... '.join([i for i in titles])
    return titles

titles = get_headlines()
print(titles[2])
print("Your news is: "+ titles[random.randint(0,10)])
