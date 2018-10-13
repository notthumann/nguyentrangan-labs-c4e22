from bs4 import BeautifulSoup
from urllib.request import urlopen
import pyexcel

url = 'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'
conn = urlopen(url)
raw_data = conn.read()
web_text = raw_data.decode('utf-8')
soup = BeautifulSoup(web_text,'html.parser')
table = soup.find('table',{'style':'border-top: solid 1px #e6e6e6;border-left:solid 1px #cccccc;border-bottom:solid 1px #cccccc'})
rows = table.find_all('tr')
list1 =[]

for i in range (0,72):    
    row = rows[i]
    data_list = row.find_all('td')
    data = {}
    for td in data_list:
        name = data_list[0].string
        data = {
            'Content':name,
            'Quý 4 - 2016':data_list[1].string,
            'Quý 1 - 2017':data_list[2].string,
            'Quý 2 - 2017':data_list[3].string,
            'Quý 3 - 2017':data_list[4].string
        }
    list1.append(data)

pyexcel.save_as(records = list1, dest_file_name = 'holy.xlsx')
