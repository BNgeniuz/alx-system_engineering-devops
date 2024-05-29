#!/usr/bin/python3
"first 10 hot posts"

import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; top_ten/1.0)'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        children = data.get('data', {}).get('children', [])

        for i in range(min(10, len(children))):
            print(children[i]['data']['title'])
    else:
        print(None)
