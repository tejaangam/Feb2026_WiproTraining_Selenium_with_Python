import requests
from lxml import html

url = "https://news.ycombinator.com"
response = requests.get(url)

data = html.fromstring(response.content)
title = data.find("//title").text
print(title)

#links
links = data.find_all("a")
print(links)

#links + URLs
links = data.xpath("//a")
for link in links:
    print(link.text)
    print(link.get("href"))

#extract the data using class name
titlelines  = data.xpath("//span[@class='title']")
print(titlelines)
for title in titlelines:
    print(title.text)