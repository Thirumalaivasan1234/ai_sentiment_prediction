import tweepy
import pandas as pd

def get_tweets(keyword, count, api_key, api_secret, access_token, access_secret):
    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
    api = tweepy.API(auth)
    tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="en", tweet_mode='extended').items(count)

    tweet_data = [{'tweet': tweet.full_text} for tweet in tweets]
    df = pd.DataFrame(tweet_data)
    df.to_csv("data/tweets.csv", index=False)
    return df
