import pandas as pd
import matplotlib.pyplot as plt

def visualize_sentiment(file_path="data/tweets_with_sentiments.csv"):
    df = pd.read_csv(file_path)
    sentiment_counts = df['sentiment'].value_counts()

    plt.figure(figsize=(6, 4))
    sentiment_counts.plot(kind='bar', color=['green', 'blue', 'red'])
    plt.title("Sentiment Analysis of Tweets")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Tweets")
    plt.tight_layout()
    plt.savefig("output/sentiment_plot.png")
    plt.show()
