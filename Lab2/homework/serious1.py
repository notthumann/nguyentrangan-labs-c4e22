from bs4 import BeautifulSoup
from urllib.request import urlopen
import pyexcel
url = 'https://www.apple.com/itunes/charts/songs/'

conn = urlopen(url)
raw_data = conn.read()
web_text = raw_data.decode('utf-8')
soup = BeautifulSoup(web_text,'html.parser')
section_content = soup.find('section','section chart-grid')
content = section_content.find('div','section-content')
ul = content.find('ul')
li_list = ul.find_all('li')
song_list  = []
for li in li_list:
    a = li.h3.a
    name = a.string
    b = li.h4.a
    artist = b.string
    song = {
        'Name' : name,
        'Artist': artist,
    }
    song_list.append(song)

pyexcel.save_as(records = song_list, dest_file_name = 'iTunesTopSongs.xlsx')