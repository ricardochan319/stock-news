import requests
from datetime import datetime, timedelta

# Function to fetch news
def fetch_news(api_key):
    url = 'https://newsapi.org/v2/everything'

    # Calculate yesterday's date
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    params = {
        'q': 'tesla',
        'apiKey': api_key,
        'from': yesterday,
        'to': datetime.now().strftime('%Y-%m-%d'),
        'language': 'en',
        'sortBy': 'popularity',
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get('articles', [])

        # Print only the top 3 articles
        for i, article in enumerate(articles):
            if i >= 3:
                break

            title = article.get('title', 'No Title')
            description = article.get('description', 'No Description')
            source = article.get('source', {}).get('name', 'Unknown Source')
            published_at = article.get('publishedAt', 'Unknown Date')

            print(f"Title: {title}\nSource: {source}\nDescription: {description}\nPublished At: {published_at}\n\n")
    else:
        print(f"Error fetching news: {response.status_code}")

# Function to fetch stock price
def fetch_stock_price(api_key):
    symbol = 'TSLA'
    interval = '5min'

    stock_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={api_key}'

    stock_response = requests.get(stock_url)

    if stock_response.status_code == 200:
        stock_data = stock_response.json()
        time_series = stock_data.get('Time Series (5min)', {})

        # Print the latest stock price
        latest_time = max(time_series.keys())
        latest_price = time_series[latest_time]['4. close']

        print(f"Stock Price for {symbol} at {latest_time}: {latest_price}")
    else:
        print(f"Error fetching stock price: {stock_response.status_code}")

# Your News API key
news_api_key = 'YOUR_NEWS_API_KEY'

# Your Alpha Vantage API key
alpha_vantage_api_key = 'YOUR_ALPHA_VANTAGE_API_KEY'

# Fetch news
fetch_news(news_api_key)

# Fetch stock price
fetch_stock_price(alpha_vantage_api_key)
