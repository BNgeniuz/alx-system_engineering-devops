#!/usr/bin/python3
"""Requests module for sending HTTP requests to the Reddit API"""
import requests

def number_of_subscribers(subreddit):
    """Get the number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = "user-agent": "linux:0x16-api-advanced:v1-0.0 (by /u/bdov_)"
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 400:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
