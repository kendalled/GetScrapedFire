# Testing Corporate Scrape V0.0.1
# github.com/kendalled

import requests
import re
import html
import time
import unicodecsv as csv

substring = '<div class='

# Set Response Headers
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def get_name_address(url):
    # Get HTML, regexp match, filter out bad emails
    try:
        site = requests.get(url, verify=True, headers=headers, timeout=15).content.decode()
        possible_address = re.findall(r'<dd>(.+?)<\/dd>', site)
        found_string = re.findall(r'<h1>(.+?)</h1>', site)
        print('Fetched Web Page.\n')
        res = [i for i in possible_address if substring not in i]
        res2 = found_string[0]
    # Fail case 1
    except:
        print('Web Page Not Found. Retry...')
        return {}

    # Fail case 2 (no address)
    if(not res):
        print('No Address Found. Retry...')
        return {}
    #  # Fail case 3 (no name)
    if(not res2):
        print('No Name Found. Retry...')
        return {}

    # Success
    else:
        res.insert(0, res2)
        if (res[1].replace(' ', '').isalpha()):
          res.remove(res[1])
        # res.remove(res[0])
        # res.insert(0, res2)
        # if (res[3] != 'Texas'):
        #   res = res[:3] + res[4:]
        print('Company Data:\n')
        address = res[2].split(',')

        try:
          city = address[0]
          state = address[1].replace(' ', '')
        except IndexError:
          return {}
        
        # print(res[:res.index('Police Departments')-2])
        # new_details = res[:res.index('Police Departments')-2]
        new_details = res
        print({

          'business_name': new_details[0],

          'address1':new_details[1],

          'city': city,

          'state': state,

          'zip': new_details[3]
        })
        return {

          'business_name': new_details[0],

          'address1':new_details[1],

          'city': city,

          'state': state,

          'zip': new_details[3]
        }

    # Extraneous Fail case
    return {}

# asks for single url, gets addresses
def runtime():
  urls = []
  data = []
  with open(r'./Data/biz1.html', "r") as f:
    page = f.read()
    partial_links = re.findall(r'href="/(.+?)"', page)
    print('Fetched Links.\n')

  for elem in partial_links:
    urls.append('http://www.corporate-office-headquarters.com/' + elem)
    print(urls)
  
  for url in urls[:]:
    data.append(get_name_address(url))
    time.sleep(1)

  with open('./corpL.csv', 'ab') as csvfile:
    fieldnames = ['business_name', 'address1', 'city', 'state', 'zip']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()

    for row in data:
      writer.writerow(row)


runtime()
