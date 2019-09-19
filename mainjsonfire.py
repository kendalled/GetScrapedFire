# GetScraped V5.0.1
# github.com/kendalled
# Firebase Edition (Time Based)
import datetime
#import firebase_admin
#import google.cloud
#from firebase_admin import credentials, firestore
import requests
import re
import pandas as pd
from glob import glob
import json
import shutil

# json function
def obj_dict(obj):
    return obj.__dict__

# Initialize Counter
total_counter = 0

# define the writing time
#startTime = datetime.time(12, 0, 0)
#endTime = datetime.time(13, 10, 0)

# Credentials and Firestore Reference
# cred = credentials.Certificate('Key/ServiceAccountKey.json')
# app = firebase_admin.initialize_app(cred)

# db = firestore.client()
# doc_ref = db.collection(u'Emails')

# Negative Email Endings
negatives = ['domain.net','group.calendar.google','youremail.com','sample.com','yoursite.com','internet.com','companysite.com','sentry.io','domain.xxx','sentry.wixpress.com', 'example.com', 'domain.com', 'address.com', 'xxx.xxx', 'email.com', 'yourdomain.com', 'godaddy.com']

# Set Response Headers
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

# function that compares the given time against start and end
# def isOpen(startTime, endTime):
#     x = datetime.datetime.now().time()
#     if startTime <= endTime:
#         return startTime <= x <= endTime
#     else:
#         return startTime <= x or x <= endTime

# Function to commit JSON in batches to firebase
# def commit_data(data):
#   n = 400
#   # List comprehension to break up into chunks
#   chunked_array = [data[i * n:(i + 1) * n] for i in range((len(data) + n - 1) // n )]

#   for elem in chunked_array:
#     batch = db.batch()

#     for item in elem:
#       new_doc = doc_ref.document()
#       batch.set(new_doc, item)
#     print('------------------------')
#     print('COMMITING DATA')
#     print('------------------------')  
#     batch.commit()

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
    fileName = './Output/' + filepath[filepath.find('/Data/')+6:filepath.find('.csv')] + '-EMAILS.json'
    # Initialize final list
    final_list = []
    global total_counter

    # Only appends businesses with valid email
    for index, row in df.iterrows():
        try:
          email = get_email(row['website'])
        except KeyboardInterrupt:
          continue
        if(email):
            currentDT = datetime.datetime.now()
 
            dt_string = currentDT.strftime("%m/%d/%Y")
            for address in [elem.lower() for elem in email]:
                if('%20' in address):
                  address = address.replace('%20','')
                final_list.append({'business': row['business_name'], 'website': row['website'], 'industry': 'Fire Department', 'city': row['city'], 'state': row['state'], 'email': address, 'contactDate': 'N/A', 'substatus': True, 'uploadDate': dt_string })

            total_counter += len(email)
            
        # if(len(final_list) >= 3500):
        #    # Writing to JSON
        #   with open(fileName, 'w') as f:
        #     json.dump(final_list, f, default=obj_dict, indent=2)
        #   break  
          
        # Printing Status
        print('------------------------')
        print(str(total_counter) + ' Email(s) found so far.')
        print('------------------------')
    
    # Writing to JSON (If list small but complete)
    with open(fileName, 'w') as f:
      json.dump(final_list, f, default=obj_dict, indent=2)
    print('File written! Kendall is the best. On to the next city!')

for entry in glob('./Data/*.csv'):
  # if isOpen(startTime, endTime):
  #   for file_name in glob('./Output/*.json'):
  #     with open(file_name, 'r') as f:
  #       data = json.load(f)
  #       print(file_name)
  #       commit_data(data)
  # else:
  #   print('Not writing time')
  # Actual Scraping
  runtime(entry)
  shutil.move(entry, './CompletedCSV/')

print('Finished all files.')
