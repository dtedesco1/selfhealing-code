import requests
from bs4 import BeautifulSoup

url = "https://weather.com/weather/today/l/USPA1276:1:US"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
temperature = soup.find('span', {'class': 'CurrentConditions--tempValue--3KcTQ'}).text
condition = soup.find('div', {'class': 'CurrentConditions--phraseValue--2xXSr'}).text.strip()
print(f"{temperature} and {condition}")