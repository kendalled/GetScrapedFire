# Testing writing JSON to firestore

import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
import json 
from glob import glob
import shutil
import time

# Credentials and Firestore Reference
cred = credentials.Certificate('Key/ServiceAccountKey.json')
app = firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection(u'Emails')
batch = db.batch()

# Function to commit JSON in batches to firebase
def commit_data(data):
  n = 400
  # List comprehension to break up into chunks
  chunked_array = [data[i * n:(i + 1) * n] for i in range((len(data) + n - 1) // n )]

  for elem in chunked_array:
    batch = db.batch()

    for item in elem:
      new_doc = doc_ref.document()
      batch.set(new_doc, item)
    print('------------------------')
    print('COMMITING DATA')
    print('------------------------')  
    batch.commit()
    time.sleep(1)

for file_name in glob('./Output/*.json'):
  with open(file_name, 'r') as f:
    data = json.load(f)
    print(file_name)
    commit_data(data)
    # Move a file from the directory d1 to d2
    shutil.move(file_name, './Uploaded/')

