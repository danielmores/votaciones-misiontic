import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://danielmoreno:l4K3truXlCOcRRyi@cluster0.lu6yo3v.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print("db", db)

baseDatos=client["registraduria-test"]
print("collections", baseDatos.list_collection_names())