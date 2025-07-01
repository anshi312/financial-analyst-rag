# scraping/news_scraper.py
import requests
from bs4 import BeautifulSoup

def fetch_yahoo_finance_news(ticker="AAPL"):
    url = f"https://finance.yahoo.com/quote/{ticker}?p={ticker}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, "html.parser")
    
    articles = []
    for link in soup.select("a[href^='/news/']"):
        headline = link.text.strip()
        href = "https://finance.yahoo.com" + link["href"]
        articles.append({"title": headline, "url": href})
    
    return articles

if __name__ == "__main__":
    news = fetch_yahoo_finance_news("TSLA")
    for n in news[:5]:
        print(n)