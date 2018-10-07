from pymongo import MongoClient

uri = "mongodb://NotHumanBeing:minhngoc123@ds125293.mlab.com:25293/c4e22"

#Connet to Database
client = MongoClient(uri)
db = client.get_default_database()

# Collection
posts = db['posts']
post_list=posts.find()
for p in post_list:
    print (p['author'])
    print (p['type'])
    print (p['content'])
#Document
#Creat a document
# post = {
#     'type':'Hom nay troi xau',
#     'content':'toi khong o nha lam bai tap c4e nua',
#     'author':'not me'
# }
# #Insert created document
# posts.insert_one(post)
#find