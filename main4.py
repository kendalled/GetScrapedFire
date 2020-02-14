# Testing P1 Scrape V0.0.1
# github.com/kendalled

import requests
import re

# Set Response Headers
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def get_address(url):
    # Get HTML, regexp match, filter out bad emails
    try:
        site = requests.get(url, verify=True, headers=headers, timeout=(2, 2)).content.decode()
        possible_emails = re.findall(r'class="DefList-description">(.+?)<\/dd>', site)
        print('Fetched Web Page.\n')
        res = possible_emails
    # Fail case 1
    except:
        print('Web Page Not Found. Retry...')
        return []

    # Fail case 2
    if(not res):
        print('No Address Found. Retry...')
        return []

    # Success
    else:
        print('Address:\n')
        print(res[:res.index('Police Departments')])
        return res[:res.index('Police Departments')]

    # Extraneous Fail case
    return []

# asks for single url, gets addresses
def runtime():
  url = input('paste URL of policeone page: ')
  get_address(url)
  print('--------------------------------')

runtime()
