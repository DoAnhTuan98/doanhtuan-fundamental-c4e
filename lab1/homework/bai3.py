from pymongo import MongoClient
#1. connect to database server
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)



#2. select database
db = client.get_database()

#3. select collection

post1_collection = db["posts"]
new_document = {
    "title": "Tôi buồn",
    "author": "Mãi yêu Em",
    "content": "Tôi buồn thổi khúc tiêu xa.Nhờ cơn gió hạ mang qua bên nàng.Trăng thanh điệp",
    
}



post1_collection.insert_one(new_document)
client.close()