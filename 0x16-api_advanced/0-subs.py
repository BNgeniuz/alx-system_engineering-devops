#!/usr/bin/python3
"""Script that queries subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    # Define the URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Define the headers with a custom User-Agent
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        # Make the request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # If the subreddit is invalid, return 0
            return 0
