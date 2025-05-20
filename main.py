from src.twitter_scraper import get_tweets
from src.sentiment_analyzer import analyze_sentiments
from src.visualize import visualize_sentiment

# Twitter API keys (replace with your credentials)
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_secret = 'YOUR_ACCESS_SECRET'

if __name__ == "__main__":
    keyword = "mental health"
    tweet_count = 100

    print("Fetching tweets...")
    # get_tweets(keyword, tweet_count, api_key, api_secret, access_token, access_secret)

    print("Analyzing sentiments...")
    analyze_sentiments()

    print("Visualizing results...")
    visualize_sentiment()
