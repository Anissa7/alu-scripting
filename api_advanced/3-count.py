#!/usr/bin/python3
"""Module for count_words function"""

import json
import requests


def count_words(subreddit, word_list, after='', hot_list=[]):
    """Function that queries the Reddit API."""
    if after == '':
        hot_list = [0] * len(word_list)
    url = "https://www.reddit.com/r/{}/hot.json" \
        .format(subreddit)
    request = requests.get(url, params={'after': after},
                           allow_redirects=False,
                           headers={'User-Agent': 'My User Agent 1.0'})
    if request.status_code == 200:
        data = request.json()

        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        hot_list[i] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for i in range(len(word_list)):
                for k in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[k].lower():
                        save.append(k)
                        hot_list[i] += hot_list[k]

            for i in range(len(word_list)):
                for k in range(i, len(word_list)):
                    if (hot_list[k] > hot_list[i] or
                            (word_list[i] > word_list[k] and
                             hot_list[k] == hot_list[i])):
                        a = hot_list[i]
                        hot_list[i] = hot_list[k]
                        hot_list[k] = a
                        a = word_list[i]
                        word_list[i] = word_list[k]
                        word_list[k] = a

            for i in range(len(word_list)):
                if (hot_list[i] > 0) and i not in save:
                    print("{}: {}".format(word_list[i].lower(), hot_list[i]))
        else:
            count_words(subreddit, word_list, after, hot_list)
