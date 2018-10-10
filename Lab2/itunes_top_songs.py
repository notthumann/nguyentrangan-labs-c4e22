from bs4 import BeautifulSoup
from urllib.request import urlopen
url =  'https://www.apple.com/itunes/charts/songs/'

conn = urlopen(url)
raw_data = conn.read()
webpage_text = raw_data.decode('utf-8')
soup = BeautifulSoup(webpage_text,'html.parser')
chart_grid = soup.find('div','section chart-grid')
li_list = chart_grid.find_all('li')
print(li_list)