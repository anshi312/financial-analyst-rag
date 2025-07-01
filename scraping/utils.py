# scraping/utils.py
from newspaper import Article

def extract_full_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

# Test
if __name__ == "__main__":
    print(extract_full_article("https://finance.yahoo.com/news/tesla-earnings-preview-q1-2024"))