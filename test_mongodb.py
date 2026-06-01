from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://jamesir637276_db_user:johankar4545@cluster0.3crc5hy.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
