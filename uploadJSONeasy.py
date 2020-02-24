# Testing writing JSON to firestore

import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
import json 
from glob import glob

# Credentials and Firestore Reference
cred = credentials.Certificate('Key/ServiceAccountKey.json')
app = firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection(u'items').document(u'item1')
batch = db.batch()

# Function to commit JSON in batches to firebase
def print_data(data):
  print(data)


with open('test.json', 'r') as f:
  data = json.load(f)
  print(data)
  batch.set(doc_ref, data)

batch.commit()

