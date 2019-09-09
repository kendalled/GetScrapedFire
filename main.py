import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore

cred = credentials.Certificate("Key/ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()
doc_ref = store.collection(u'Emails').limit(5)
# doc_ref = store.collection(u'test')
# doc_ref.add({u'name': u'test', u'added': u'just now'})

try:
    docs = doc_ref.stream()
    for doc in docs:
        print(u'Doc Data:{}'.format(doc.to_dict()))
except google.cloud.exceptions.NotFound:
    print(u'Missing data')