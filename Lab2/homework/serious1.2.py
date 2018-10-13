from bs4 import BeautifulSoup
from urllib.request import urlopen
import pyexcel
from youtube_dl import YoutubeDL

url = 'https://www.apple.com/itunes/charts/songs/'
conn = urlopen(url)
raw_data = conn.read()
web_text = raw_data.decode('utf-8')
soup = BeautifulSoup(web_text,'html.parser')
section_content = soup.find('section','section chart-grid')
div = section_content.find('div','section-content')
ul = div.find('ul')
li_list = ul.find_all('li')
song_list = []
options = {
    'default_search':'ytsearch',
    'max_download':1,
    'format':'bestaudio/audio'
}
dl = YoutubeDL(options)
for li in li_list:
    a = li.h3.a
    name = a.string
    b = li.h4.a
    artist = b.string
    dl.download([name,artist])
    song = {
        'Name':name,
        'Artist':artist
    }
    song_list.append(song)
print(song_list)
