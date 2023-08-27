#!/usr/bin/python3
""""Recursively gets all host posts"""
from requests import get


base_url = 'https://www.reddit.com'
headers = {'User-Agent': 'Mozilla/5.0'}


def recurse(subreddit, hot_list=[], after=''):
    """"
    Continually gets all hot posts recursively
    """
    full_url = base_url + '/r/{}/hot.json'.format(subreddit)
    params = {'after': after}
    response = get(full_url, headers=headers, params=params)

    if response.status_code != 200:
        return None
    else:
        data = response.json().get('data')
        has_next = data.get('after') is not None

        hot_articles = data.get('children')
        hot_list += map(
                lambda article: article.get('data').get('title'),
                hot_articles)

        return recurse(subreddit, hot_list, after=after) \
            if has_next else hot_list
