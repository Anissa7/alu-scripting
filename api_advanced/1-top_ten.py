#!/usr/bin/python3
"""gets top ten posts"""
from requests import get


def top_ten(subreddit):
    """top ten"""
    base_url = 'https://www.reddit.com'
    full_url = base_url + '/r/{}/hot.json?limit=10'.format(subreddit)

    res = get(full_url, headers={'User-Agent': 'Mozilla/5.0'})

    if res.status_code != 200:
        print(None)
    else:
        posts = res.json().get('data').get('children')

        for post in posts:
            print(post.get('data').get('title'))
