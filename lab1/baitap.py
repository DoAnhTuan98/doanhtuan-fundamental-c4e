from pymongo import MongoClient
#1. connect to database server
uri = "mongodb://admin:admin123@ds229474.mlab.com:29474/c4e_24"
client = MongoClient(uri)



#2. select database
db = client.get_database()

#3. select collection
post_collection = db["account"]
post1_collection = db["account1"]
post2_collection = db["account2"]
new_document = {
    "username": "son",
    "email": "nguyenthaison@gmail.com",
    "phone": "0921321",
    "password": "sonoccho",
}
new_document1 = {
    "username": "tuan",
    "email": "tuandaika@gmail.com",
    "phone": "0921321",
    "password": "tuananh",
}
new_document2 = {
    "username": "tho",
    "email": "thoimoney@gmail.com",
    "phone": "323213124",
    "password": "thongaocan",
}

post_collection.insert_one(new_document)
post2_collection.insert_one(new_document2)




client.close()