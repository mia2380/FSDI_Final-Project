import pymongo
import certifi

con_str = "mongodb+srv://mia2380:FSDI1234@cluster0.ajul34m.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("pets")