import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/coronavirus/'
output_file = 'html/covid19.json'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('table', attrs={'id': 'main_table_countries_today'})
table_rows = table.find_all('tr')
table_head = table.find_all('thead')

data_list = []
col_list = []

for tr in table_head:
    th = tr.find_all('th')
    th_row = [tr.text for tr in th]
    col_list = th_row

for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    data_list.append(row)

df = pd.DataFrame(data_list, columns=col_list)
df.drop(df.index[:8], inplace=True)

df = df.replace('\n', '', regex=True)
with open('html/covid19.json', 'w') as json_file:
    json_file.write(df.to_json(orient='records'))
