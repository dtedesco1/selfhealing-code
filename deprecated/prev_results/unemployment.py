import requests
from bs4 import BeautifulSoup

url = 'https://data.bls.gov/timeseries/LNS14000000'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find_all('table')[1]
rows = table.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    if cells:
        year = cells[0].get_text()
        if year == '2023':
            data = cells[1].get_text()
            print(data)
print(table)