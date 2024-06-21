#!/usr/bin/python3
"""
Subscribers count module
"""

import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit
    """
    url = "https://www.reddit.com/r/{subreddit}/about.json".format(subreddit)
    headers = {
            'User-Agent': "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return 0
    results = response.json().get("data")
    return = results.get("subscribers")
