import requests
from bs4 import BeautifulSoup as bs

# Load the webpage content

r = requests.get("https://keithgalli.github.io/web-scraping/example.html")

# Converting to BeautifulSoup object

soup = bs(r.content, features="html.parser")

# find and find all

first_grab = soup.find("h2")
print(first_grab)

headers = soup.find_all("h2")
print(headers)
print("\n" * 10)

# pass in list of elements to look for

first_header = soup.find(['h2', 'h1'])
print(first_header)

headers_all = soup.find_all(['h1', 'h2'])
print(headers_all)
print("\n" * 10)

# You can pass an attribute to find/fin_all function

paragraphs = soup.find_all("p", attrs = {"id": "paragraph-id"})
print(paragraphs)
print("\n" * 10)

# You can nest find/find_all calls

body = soup.find("body")
div = body.find("div")
header = div.find("h1")
print(header)
print("\n" * 10)

# We can search in specific strings in our find/find_all calls

import re

paragraph = soup.find_all('p', string = re.compile("Some"))
print(paragraph)

headers = soup.find_all('h2', string = re.compile("(H|h)eader"))
print(headers)
print(10 * "\n")
# Select CSS (Collector)

content = soup.select("div p")
print(content)

paragraphs = soup.select("h2 ~ p")
print(paragraphs)

bold_text = soup.select("p#paragraph-id b")
print(bold_text)

paragraphs = soup.select("body > p")
print(paragraphs)

for paragraph in paragraphs:
    print(paragraph.select("i"))
print()
middle = soup.select("[align=middle]")
print(middle)

# use .string method

header = soup.find("h2")
print(header.string)

# if multipile child elements use get_text()

div = soup.find("div")
print(div.get_text())

# Get specific property from an element

link = soup.find('a')
print(link['href'])

paragraphs = soup.select('p#paragraph-id')
print(paragraphs[0]['id'])

# Know the terms: Parent, Sibling, Child

ans = soup.body.find('div').find_next_siblings()
print(ans)
