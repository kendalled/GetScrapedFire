# Testing P1 Scrape V0.0.1
# github.com/kendalled

import requests
import re
import html
import time
import unicodecsv as csv

# Set Response Headers
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

# exlude ones i sent like a dummy
ex_list = ['Chittenango Village Police Department', 'Cazenovia Village Police Department', 'Ramapo Town Police Department', 'Canastota Village Police Department', 'Baldwinsville Village Police Department', 'Tupper Lake Village Police Department', 'Saranac Lake Village Police Department','Rouses Point Village Police Department', 'Troy City Police Department', 'Malone Village Police Department', 'Lake Placid Village Police Department', 'Whitehall Village Police Department', 'Ticonderoga Police Department', 'Hudson Falls Village Police Department', 'Greenwich Village Police Department', 'Granville Village Police Department', 'Fort Edward Village Police Department', 'Corinth Village Police Department', 'Cambridge Village Police Department', 'WestSeneca Town Police Department', 'South Glens Falls Village Police Department', 'Glens Falls City Police Department', 'White Plains City Police Department', 'Southampton Town Police Department', 'Port Jervis City Police Department', 'Liberty Village Police Department', 'Monticello Village Police Department', 'Wappingers Falls Village Police Department', 'Village of Walden Police Department', 'Rhinebeck Village Police Department', 'Red Hook Village Police Department', 'Rome City Police Department', 'Greenburgh Town Police Department', 'New Paltz Town/Village Police Department', 'Maybrook Village Police Department', 'Freeport Village Police Department', 'Town of Poughkeepsie Police Department', 'Lloyd Town Police Department', 'Cornwall', 'Beacon City Police Department', 'Ellenville Village Police Department', 'Catskill Village Police Department', 'Haverstraw Town Police Department', 'Brighton Town Police Department', 'Scotia Village Police Department', 'Jamestown City Police Department', 'Yorktown Town Police Department', 'Orangetown Town Police Department', 'North Tonawanda City Police Department', 'Menands Village Police Department', 'Watervliet City Police Department', 'Waterford Town Police Department', 'Long Bch City Police Department', 'Carmel Town Police Department', 'Green Island Village Police Department', 'Stillwater Town Police Department', 'Mechanicville City Police Department', 'Johnstown City Police Department', 'Elmira City Police Department', 'Coxsackie Village Police Department', 'Cobleskill Village Police Department', 'Chatham Village Police Department', 'Guilderland Police Department', 'Auburn City Police Department', 'Ballston Spa Village Police Department', 'Athens Village Police Department', 'Poughkeepsie City Police Department', 'Altamont Police Department', 'Manlius Town Police Department', 'Gates Town Police Department', 'Webster Town/Village Police Department', 'Orchard Park Town Police Department', 'Rotterdam Town Police Department', 'Bethlehem Town Police Department', 'Ithaca City Police Department', 'Watertown City Police Department', 'Camillus Town/Village Police Department', 'Mount Pleasant Town Police Department']
# method for calculating that
def dont_exclude(row):
  return(row[0].strip() not in ex_list)

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
        if (res[3] != 'New York' and res[3] != 'new york'):
          res = res[:3] + res[4:]
        print('Station Data:\n')
        print(res[:res.index('Police Departments')-2])
        new_details = res[:res.index('Police Departments')-2]
        try:
          # only checking existence of element 4 because 0-3 are guaranteed if 4 exists
          if(new_details[4]):
            print('Address Complete with ZIP.')
        # handling incomplete pages
        except IndexError:
          return {}
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
  with open(r'./Data/pol.html', "r") as f:
    page = f.read()
    partial_links = re.findall(r'href="/law-enforcement-directory/police-departments/(.+?)"', page)
    print('Fetched Links.\n')

  for elem in partial_links:
    urls.append('https://www.policeone.com/law-enforcement-directory/police-departments/' + elem)
  # CHANGE WHEN DOING NEW BATCH YEET
  for url in urls[0:]:
    data.append(get_name_address(url))
    time.sleep(1)

  with open('./NYPDRealREAL.csv', 'ab') as csvfile:
    fieldnames = ['station_name', 'address1', 'city', 'state', 'zip']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()

    for row in data:
      if(dont_exclude):
        writer.writerow(row)
      else:
        print('EXCLUDING DUPE')


runtime()
