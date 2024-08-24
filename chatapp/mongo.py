from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://sanjayram2134:ram_2134@cluster0.1mxxz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# client = MongoClient(uri, server_api=ServerApi('1'))
# db = client['mydb1']
# collection = db['temp1']

# Insert Document into MongoDB
def insert_data(document):
    """Insert a document into MongoDB."""
    try:
        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client['mydb1']
        collection = db['temp1']

        inserted_document = collection.insert_one(document)
        print(f"Inserted Document ID: {inserted_document.inserted_id}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Ensure the MongoDB client is closed
        client.close()

# # Close MongoDB Connection
# client.close()