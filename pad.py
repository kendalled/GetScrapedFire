# Testing P1 Scrape V0.0.1
# github.com/kendalled

import requests
import re
import html
import time
import unicodecsv as csv

# Set Response Headers
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def get_name_address(url):
    # Get HTML, regexp match, filter out bad emails
    try:
        site = requests.get(url, verify=True, headers=headers, timeout=15).content.decode()
        possible_emails = re.findall(r'class="DefList-description">(.+?)<\/dd>', site)
        found_string = re.findall(r'<h1 class="Article-p Article-p--heading">(.+?)-', site)
        print('Fetched Web Page.\n')
        res = possible_emails
        res2 = found_string[0]
    # Fail case 1
    except:
        print('Web Page Not Found. Retry...')
        return {}

    # Fail case 2 (no address)
    if(not res):
        print('No Address Found. Retry...')
        return {}
     # Fail case 3 (no name)
    if(not res2):
        print('No Name Found. Retry...')
        return {}

    # Success
    else:
        res.remove(res[0])
        res.insert(0, res2)
        if (res[3] != 'California' and res[3] != 'california'):
          res = res[:3] + res[4:]
        print('Station Data:\n')
        print(res[:res.index('Police Departments')-2])
        new_details = res[:res.index('Police Departments')-2]
        return {

          'station_name': new_details[0],

          'address1':new_details[1],

          'city':new_details[2],

          'state':new_details[3],

          'zip': new_details[4]
        }

    # Extraneous Fail case
    return {}

# asks for single url, gets addresses
def runtime():
  urls = []
  data = []
  with open(r'./Data/saved.html', "r") as f:
    page = f.read()
    partial_links = re.findall(r'href="/law-enforcement-directory/police-departments/(.+?)"', page)
    print('Fetched Links.\n')

  for elem in partial_links:
    urls.append('https://www.policeone.com/law-enforcement-directory/police-departments/' + elem)
  
  for url in urls[301:]:
    data.append(get_name_address(url))
    time.sleep(1)

  with open('./CaliPD2.csv', 'ab') as csvfile:
    fieldnames = ['station_name', 'address1', 'city', 'state', 'zip']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()

    for row in data:
      writer.writerow(row)


runtime()
