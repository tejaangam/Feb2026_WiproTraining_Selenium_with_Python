from bs4 import BeautifulSoup
import requests

html = '''
<html>
<head><title>My Page</title></head>
<body>
<h1>Welcome</h1>
<h2>My Name is HTML</h2>
<p>This is a paragraph.</p>
<a  href="https://google.com">Google</a>
<a href="https://github.com">GitHub</a>
<a href="https://google.com" id="link1" class="search">Google</a>
</body>
</html>
'''
#1. create a parser
soup = BeautifulSoup(html, "html.parser")
#2.Get title
title = soup.title.text
print(title)

#3.h1 tag
for tag in soup.find_all("h1"):
    print(tag.text)


#Extract all paragraphs
para = soup.find_all("p")
for p in para:
    print(p.text)

#extract all links
links = soup.find_all("a")
for link in links:
    print(link.get("href"))

#count links
print("No of links:", len(links))
#Extract Attributes
tag = soup.find("a")
print(tag)
tag.get("href")

#h2 tag
h2= soup.find("h2")
print(h2)

#bold
bold = soup.find("b")
print(bold)

links = soup.find_all("a")
for link in links:
    print(link.get("href"))

#get all text
all_text = soup.get_text()
print(all_text)

#title
title = soup.title.next
print(title)

#headings
headings = soup.find_all(["h1", "h2"])
for h in headings:
    print(h.text)

#table
table = soup.find("table")
print(table)

#image
images = soup.find_all("img")
for img in images:
    print(img.get("src"))
