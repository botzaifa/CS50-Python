import pytest
from project import fetch_news_headlines, analyze_sentiment, visualize_sentiment, write_to_excel
from unittest.mock import patch
import os

@pytest.fixture
def mock_news_response():
    # Mocked news response data
    return {
        'articles': [
            {'title': 'Test Title', 'description': 'Test Description', 'url': 'https://test.com'}
        ]
    }

def test_fetch_news_headlines(mock_news_response):
    # Mocking the request.get method
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = mock_news_response
        api_key = 'fake_key'
        topic = 'test'
        result = fetch_news_headlines(api_key, topic)
        assert len(result) == 1
        assert result[0] == ('Test Title', 'Test Description', 'https://test.com')

def test_analyze_sentiment():
    headlines = [('Positive headline', 'Positive description', 'https://positive.com'),
                 ('Negative headline', 'Negative description', 'https://negative.com')]
    result = analyze_sentiment(headlines)
    assert len(result) == 2
    assert result[0][1] == 'Positive'
    assert result[1][1] == 'Negative'

def test_visualize_sentiment(monkeypatch):
    sentiments = [('Positive headline', 'Positive', 'Positive description', 'https://positive.com'),
                  ('Negative headline', 'Negative', 'Negative description', 'https://negative.com'),
                  ('Neutral headline', 'Neutral', 'Neutral description', 'https://neutral.com')]
    visualize_sentiment(sentiments)
    assert os.path.exists('sentiment_distribution.png')
