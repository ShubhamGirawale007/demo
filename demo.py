from pymongo import MongoClient 
# Connect to the default MongoDB instance (localhost:27017) 
client = MongoClient()  
# Connect to a specific host and port 
# client = MongoClient('localhost', 27017)  
# Connect with authentication (if required) 
# client = MongoClient('mongodb://<username>:<password>@<host>:<port>/') 
db = client['your_database_name'] 
collection = db['your_collection_name'] 
data = {'name': 'John Doe', 'age': 30, 'city': 'New York'} 
result = collection.insert_one(data)  
print(result.inserted_id) 
# Find all documents 
results = collection.find()  
# Find documents with specific criteria 
results = collection.find({'age': {'$gt': 25}})  
for doc in results: 
print(doc) 
client.close() 