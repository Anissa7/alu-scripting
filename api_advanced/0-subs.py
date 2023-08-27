#!/usr/bin/python3
"""Gets number of subscribers"""
from requests import get


def number_of_subscribers(subreddit):
    """Returns number of subscribers of a given subreddit"""
    base_url = 'https://www.reddit.com'
    full_url = base_url + '/r/{}/about.json'.format(subreddit)

    res = get(full_url, headers={'User-Agent': 'Mozilla/5.0'})

    if res.status_code != 200:
        return 0
    else:
        return res.json().get('data').get('subscribers')
