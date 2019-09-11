# GetScraped V4.0.1
# github.com/kendalled
# Firebase Edition

from datetime import datetime
import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
import requests
import re
import pandas as pd
from glob import glob

cred = credentials.Certificate('Key/ServiceAccountKey.json')
app = firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection(u'Emails')

# Negative Email Endings
negatives = ['domain.net','group.calendar.google','youremail.com','sample.com','yoursite.com','internet.com','companysite.com','sentry.io','domain.xxx','sentry.wixpress.com', 'example.com', 'domain.com', 'address.com', 'xxx.xxx', 'email.com', 'yourdomain.com']

# Set Response Headers
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def get_email(url):

    # Filtering Function
    def filter_func(x):
        ind = x.find('@')+1
        print('filtering...')
        return not (x[ind:] in negatives)


    # Get HTML, regexp match, filter out bad emails
    try:

        site = requests.get(url, verify=True, headers=headers, timeout=(2, 2)).content.decode()
        possible_emails = re.findall(r'[A-Za-z0-9._%+-]{3,}@[a-z]{3,}\.[a-z]{2,}(?:\.[a-z]{2,})?', site)
        print('Fetched Web Page.\n')
        res = list(set(filter(filter_func,possible_emails)))

    # Fail case 1
    except:
        print('Web Page Not Found. Deleting...')
        return []

    # Fail case 2
    if(not res):
        print('No Emails Found. Deleting...')
        return []

    # Success
    else:
        print('Email(s):\n')
        print(res)

        return res

    # Extraneous Fail case
    return []


def runtime(filepath):
    # Reads website column, initializes counter variable
    df = pd.read_csv(filepath)
    counter = 0
    total_counter = 0
    batch = db.batch()
    # Only appends businesses with valid email
    for index, row in df.iterrows():
        email = get_email(row['website'])
        if(email):
            now = datetime.now()
 
            dt_string = now.strftime('%d/%m/%Y %H:%M')
            for address in [elem.lower() for elem in email]:
                if('%20' in address):
                  address = address.replace('%20','')
                new_doc = doc_ref.document()
                batch.set(new_doc, {'business': row['business_name'], 'website': row['website'], 'industry': row['industry'], 'city': row['city'], 'state': row['state'], 'email': address, 'contactDate': 'N/A', 'substatus': True, 'uploadDate': dt_string })
            counter += len(email)
            total_counter += len(email)

        if(counter >= 225):
          batch.commit()
          print('Commiting ' + str(counter) + ' emails.')
          counter = 0
        # Printing Status
        print('------------------------')
        print(str(total_counter) + ' Email(s) found so far.')
        print('------------------------')

    print('File written! Kendall is the best. On to the next one!')

for entry in glob('./Data/*.csv'):
    try:
      runtime(entry)
    except KeyboardInterrupt:
      continue

print('Finished all files.')
