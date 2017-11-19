# Source: yanofsky/tweet_dumper.py on Github

import tweepy
import csv


APP_KEY = '3JfI3Mr9KezadyXR4y1CYHP9g'
APP_SECRET = 'abjzs4UhZNjrE7VGX68WsZP7AlQurYCXMx9iaIHlzXAQUYsutS'

access_token = '922527675599683584-gF6Co8HREIGNoxKlPZVmE8b7RcR2xvl'
access_token_secret = 'rikHEcHJTdojitDX6k8PA9vJ9qyiSGalU1kMaDgTqHGps'


def scrape_tweets(screen_name):

    auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    all_tweets = []
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)
    all_tweets.extend(new_tweets)

    oldest = all_tweets[-1].id - 1

    while len(new_tweets) > 0:
        print("getting tweets before %s" % oldest)

        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        all_tweets.extend(new_tweets)

        oldest = all_tweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(all_tweets)))

    out_tweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"), tweet.retweet_count, tweet.favorite_count] for tweet in all_tweets]

    with open('%s_tweets.csv' % screen_name, mode='w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "text", "#retweets", "#favorites"])
        writer.writerows(out_tweets)

    pass

if __name__ == '__main__':
    scrape_tweets('NC5')

# Selected screen_names:
# BBCWorld
# TheEconomist
# TIME
# AP
# NashvilleScene
# NC5


