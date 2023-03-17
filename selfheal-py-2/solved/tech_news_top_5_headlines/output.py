import sys
import subprocess

def check_and_install_libraries():
    try:
        import requests
        import bs4
    except ImportError:
        subprocess.call([sys.executable, "-m", "pip", "install", "requests", "beautifulsoup4"])
        import requests
        from bs4 import BeautifulSoup
    return requests, bs4

requests, bs4 = check_and_install_libraries()
BeautifulSoup = bs4.BeautifulSoup

def extract_top_headlines():
    url = 'https://techcrunch.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h2', class_='post-block__title')
    
    for index, headline in enumerate(headlines[:5]):
        print(f"{index+1}. {headline.text.strip()}\n{headline.find('a')['href']}\n")

extract_top_headlines()