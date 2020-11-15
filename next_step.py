import requests
from bs4 import BeautifulSoup as bs
import re
url = 'https://keithgalli.github.io/web-scraping/'
r = requests.get(url + "webpage.html")

webpage = bs(r.content, features = 'html.parser')

links = webpage.select('ul.socials a')

# for link in links:
#     if 'https' in link['href']:
#         print(link['href'])

alinks = webpage.find('ul', attrs = {"class": "socials"})
links = alinks.find_all('a')
#
# for link in links:
#     if 'https' in link['href']:
#         print(link['href'])
#

import pandas as pd

table = webpage.select('table.hockey-stats')[0]
column = table.find("thead").find_all('th')
column_names = [c.string for c in column]

table_rows = table.find('tbody').find_all('tr')
rows = []

for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.get_text().strip() for tr in td]
    rows.append(row)
df = pd.DataFrame(rows, columns = column_names)
# print(df.loc[df['Team'] != "Did not play"].sum())

# grab all fun facts that use word 'is'

facts = webpage.select('ul.fun-facts li')
facts_with_is = [fact.find(string = re.compile('is')) for fact in facts]
facts_with_is = [fact for fact in facts_with_is if fact]
# print(facts_with_is)

# Download image

images = webpage.select('div.row div.column img')
image_url = images[0]['src']
full_url = url + image_url

img_data = requests.get(full_url).content
with open('lake_como.jpg', 'wb') as handler:
    handler.write(img_data)

files = webpage.select("div.block ul li a")
for f in files:
    full_url = url + f['href']
    r = requests.get(full_url)
    bs_file = bs(r.content, features="html.parser")
    print(bs_file.find("p", attrs = {"id": "secret-word"}).get_text())
