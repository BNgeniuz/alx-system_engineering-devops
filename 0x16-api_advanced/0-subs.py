#!/usr/bin/python3
"""
Subscribers count module
"""

import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get("data")
    num_subs = data.get("subscribers")

    return num_subs
