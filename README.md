# Decoding Emotions Through Sentiment Analysis

This project collects tweets from Twitter based on a keyword and analyzes the sentiment of the tweets to understand the emotions expressed.

## Features

- Collects tweets using Tweepy
- Analyzes sentiment using TextBlob
- Visualizes the sentiment distribution

## How to Run

1. Clone the repo or extract the ZIP
2. Install requirements: `pip install -r requirements.txt`
3. Add your Twitter API credentials to `main.py`
4. Run the project: `python main.py`

## Output

- `data/tweets.csv`: Raw tweets
- `data/tweets_with_sentiments.csv`: Tweets with sentiment
- `output/sentiment_plot.png`: Sentiment bar chart
