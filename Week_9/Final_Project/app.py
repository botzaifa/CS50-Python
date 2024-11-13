import openpyxl
import requests
from textblob import TextBlob
import matplotlib.pyplot as plt
import os

def fetch_news_headlines(api_key, topic):
    """Fetches news headlines from a news API."""
    url = f'https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}'
    response = requests.get(url)
    headlines = response.json()['articles']
    return [(headline['title'], headline['description'], headline['url']) for headline in headlines]

def analyze_sentiment(headlines):
    """Analyzes the sentiment of news headlines."""
    sentiments = []
    for headline, description, url in headlines:
        analysis = TextBlob(headline)
        polarity = analysis.sentiment.polarity
        sentiment = 'Positive' if polarity > 0 else 'Negative' if polarity < 0 else 'Neutral'
        sentiments.append((headline, sentiment, description, url))
    return sentiments

def visualize_sentiment(sentiments):
    """Visualizes the sentiment distribution."""
    sentiment_counts = {'Positive': 0, 'Negative': 0, 'Neutral': 0}
    for _, sentiment, _, _ in sentiments:
        sentiment_counts[sentiment] += 1

    plt.bar(sentiment_counts.keys(), sentiment_counts.values())
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.title('Sentiment Distribution of News Headlines')
    # Save the visualization as an image
    plt.savefig('sentiment_distribution.png')
    plt.close()  # Close the plot to avoid displaying it in a new window

def write_to_excel(sentiments):
    """Writes headlines, sentiment, and extra information to an Excel file."""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['Headline', 'Sentiment', 'Description', 'URL'])
    for headline, sentiment, description, url in sentiments:
        ws.append([headline, sentiment, description, url])
    wb.save('news_headlines.xlsx')

def main():
    api_key = '91169448c3814262a7e01b3fd0a90f4f'
    topic = input('Enter a topic: ')
    headlines = fetch_news_headlines(api_key, topic)
    sentiments = analyze_sentiment(headlines)
    write_to_excel(sentiments)
    visualize_sentiment(sentiments)

if __name__ == '__main__':
    main()
