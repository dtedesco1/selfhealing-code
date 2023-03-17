import requests
from bs4 import BeautifulSoup

def install_libraries():
    try:
        import requests
        import bs4
    except ImportError:
        import os
        os.system('pip install requests beautifulsoup4')

def get_top_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    headlines = []
    for headline in soup.select('.gs-c-promo-heading__title', limit=5):
        title = headline.get_text()
        link = headline.parent['href']
        headlines.append((title, link))
    return headlines

def main():
    install_libraries()
    url = 'https://www.bbc.com/news'
    top_headlines = get_top_headlines(url)
    for i, (title, link) in enumerate(top_headlines, start=1):
        print(f'{i}. {title} - {link}')

if __name__ == '__main__':
    main()