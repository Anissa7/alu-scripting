#!/usr/bin/python3
""""Doc"""
import requests

def count_words(subreddit, word_list, after="", words_count={}):
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    header = {'User-Agent': 'Mozilla/5.0'}
    param = {'after': after}
    res = requests.get(url, headers=header, params=param)

    if res.status_code != 200:
        return

    json_res = res.json()
    after = json_res.get('data').get('after')
    has_next = after is not None

    if len(words_count) == 0:
        words_count = {word.lower(): 0 for word in word_list}

    hot_articles = json_res.get('data').get('children')

    for article in hot_articles:
        title_words = article.get('data').get('title').lower().split()
        for title_word in title_words:
            for word in word_list:
                if word.lower() == title_word:
                    words_count[word.lower()] += 1

    if has_next:
        return count_words(subreddit, word_list, after, words_count)
    else:
        words_count = {key: value for key, value in words_count.items() if value != 0}
        sorted_counts = sorted(words_count.items(), key=lambda item: item[1], reverse=True)

        for word, count in sorted_counts:
            print("{}: {}".format(word, count))

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2].split()
        count_words(subreddit, word_list)

