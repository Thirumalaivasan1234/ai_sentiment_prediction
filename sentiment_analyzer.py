from textblob import TextBlob
import pandas as pd

def analyze_sentiments(input_file="data/tweets.csv"):
    df = pd.read_csv(input_file)
    sentiments = []

    for tweet in df['tweet']:
        blob = TextBlob(tweet)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            sentiment = 'Positive'
        elif polarity < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
        sentiments.append(sentiment)

    df['sentiment'] = sentiments
    df.to_csv("data/tweets_with_sentiments.csv", index=False)
    return df
