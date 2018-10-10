#1. Download webpage
from bs4 import BeautifulSoup
from urllib.request import urlopen
import  pyexcel

url = 'https://dantri.com.vn'

#1.1 Open connection
conn = urlopen(url)

#1.2 Download raw data
raw_data = conn.read()

#1.3 Decode data
webpage_text = raw_data.decode('utf-8')

# urllib
#1.4 Save text
#w =>write
#b =>binary
# f = open('dantri.html','wb')
# f.write(raw_data)
# f.close()


#2. Extract ROI
#2.1 Convert text to soup
soup = BeautifulSoup(webpage_text,'html.parser')
# print (soup.prettify())
ul = soup.find('ul','ul1 ulnew')

li_list = ul.find_all('li')
print (li_list)
news_list = []
for li in li_list:
    a = li.h4.a
    title = a.string
    link = url + a['href']
    
    # print(title)
    # print(link)
    news = {
        "Title": title,
        "Link": link,
    }
    news_list.append(news)
    

#3. Extract data
pyexcel.save_as(records = news_list, dest_file_name = 'news.xlsx')

#4. Save data