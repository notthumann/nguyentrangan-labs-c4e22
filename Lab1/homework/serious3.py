from pymongo import MongoClient
from matplotlib import pyplot
uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = MongoClient(uri)
db = client.get_default_database()

customers = db['customers']
customer_list = customers.find()
count_customers = 0
count_events = 0
count_wom = 0
count_ads = 0
for c in customer_list:
    count_customers += 1
    if c['ref']==  'events':
        count_events += 1
    elif c['ref']== 'event':
        count_events += 1
    elif c['ref']== 'wom':
        count_wom +=1
    elif c['ref']== 'ads':
        count_ads +=1
print('Number of customers: ',count_customers)
print('Customer acquired from events: ', count_events)
print('Customer acquired by word of mouth: ', count_wom)
print('Customer acquired by advertisements: ',count_ads)

customer_counts = [count_events, count_wom, count_ads]
customers_refs = ['Events','Word of Mouth','Ads']
pyplot.pie(customer_counts, labels=customers_refs, autopct='%.1f%%', shadow=True)
pyplot.axis('equal')
pyplot.title('Percentage of customers references')
pyplot.show()
