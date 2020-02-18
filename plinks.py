# Testing P1 ScrapeLinks V0.0.1
# github.com/kendalled

import re
import html
res = []
with open(r'./Data/saved.html', "r") as f:
    page = f.read()
    partial_links = re.findall(r'href="/law-enforcement-directory/police-departments/(.+?)"', page)
    print('Fetched Web Page.\n')
#tree = html.fromstring(page)

for elem in partial_links:
  res.append('https://www.policeone.com/law-enforcement-directory/police-departments/' + elem)

print(len(res))
#print(page)
