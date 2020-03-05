# college test 
import requests
import re
import html
import time
import unicodecsv as csv

# Set Response Headers
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def get_name_address(url):
  try:
    site = requests.get(url, verify=True, headers=headers, timeout=15).content.decode()
  except:
    print('DECODING ERROR')
    return {}
  street_address = re.findall(r'<span itemprop="streetAddress">(.+?)<\/span>', site)
  city = re.findall(r'<span itemprop="addressLocality">(.+?) \(', site)
  state = re.findall(r'<span itemprop="addressRegion">(.+?)<\/span>', site)
  postal = re.findall(r'<span itemprop="postalCode">(.+?)<\/span>', site)
  college_name = re.findall(r'<h1 itemprop="name">(.+?)<\/h1>', site)
  print('Fetched Web Page.\n')
  print(college_name)
  print(street_address)
  print(city)
  print(state)
  print(postal)

  try:
    res = {
      'college_name': college_name[0],

      'address1': street_address[0],

      'city': city[0],

      'state': state[0],

      'zip': postal[0]
    }
    return res
  except:
    print('error')
    return {}

  print('Fetched Web Page.\n')
  print(college_name)
  print(street_address)
  print(city)
  print(state)
  print(postal)


# asks for single url, gets addresses
def runtime():
  urls = []
  data = []
  with open(r'./Data/college.html', "r") as f:
    page = f.read()
    partial_links = re.findall(r'href="/(.+?)"', page)
    print('Fetched Links.\n')

  for elem in partial_links:
    if not (elem[:-4].isalpha()):
      urls.append('https://www.4icu.org/' + elem)
      print('https://www.4icu.org/' + elem)
    else:
      print('not a college link')
  
  for url in urls:
    data.append(get_name_address(url))
    time.sleep(1)

  with open('./college.csv', 'ab') as csvfile:
    fieldnames = ['college_name', 'address1', 'city', 'state', 'zip']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()

    for row in data:
      writer.writerow(row)


runtime()