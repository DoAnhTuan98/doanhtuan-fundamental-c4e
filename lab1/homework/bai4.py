from matplotlib import pyplot
from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)

db = client.get_database()

collection_customers = db["customers"]

events =  collection_customers.count_documents({"ref": "events"})
wom = collection_customers.count_documents({"ref": "wom"})
ads = collection_customers.count_documents({"rè": "ads"})

count = [events,wom,ads]
name = ["Events","Wom","Ads"]

pyplot.pie(count,labels= name,autopct= "%0.1f%%",shadow = True,explode = [0,0.1,0])
pyplot.axis("equal")
pyplot.show()
client.close()





