from pymongo import MongoClient
uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = MongoClient(uri)
db = client.get_default_database()

posts = db['posts']
post = {
    'title' : 'From a Ghost',
    'author' : 'Not Human Being',
    'content': 'Try To Escape Reality. But Still Here.'
}
posts.insert_one(post)