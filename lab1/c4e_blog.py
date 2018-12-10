from pymongo import MongoClient
#1. connect to database server ket noi vs may chu csdl
uri = "mongodb://admin:admin123@ds229474.mlab.com:29474/c4e_24"
client = MongoClient(uri)



#2. select database chon co so du lieu
db = client.get_database()

#3. select collection chon bo suu tap
post_collection = db["posts"]
#4. create document tao tai lieu

# new_document = {
#     "title": "hom nay vn thang",
#     "post":"Minh  di bao",
# }

#5 add document into collection them vao collection
# post_collection.insert_one(new_document)
for post in post_collection.find():
    print(post)

#6. close connection
client.close()