from bs4 import BeautifulSoup
import requests

url = "http://books.toscrape.com/"
headers = {"User-Agent": "Chrome/144.0.7559.133"}

response = requests.get(url, headers = headers)
print(response.status_code)

#parse the html
soup = BeautifulSoup(response.text, features="html.parser")
#html code is printed
print(soup)

#get the head tag
headtag = soup.head
print(headtag)
#get the body
print(soup.body)
#get the title of the page
print(soup.title.string)
#get the first matching tag
print(soup.find("h1"))
#get the matching paragraph
print(soup.find("p"))

for link in links:
    print(link.get("href"))
#extract the book
books = soup.find_all("article",   class_ = "product_pod")

#extract title and price in the books
for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.find("p", class_ = "price_color").text
    print("Title: ", title)
    print("Price: ", price)

#extracting the data

html_doc = """
<html>
<head>
  <title>List Example</title>
</head>
<body>
  <ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
  </ul>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, features = "html.parser")

#finding listitems tags <li>
items = soup.find_all('li')
for item in items:
    print(item.text)

html_doc = """
<html>
<head><title>CSS Selector Example</title></head>
<body>
  <div id="main">
    <p class="info">Info Paragraph 1</p>
    <p class="info">Info Paragraph 2</p>
  </div>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, features = "html.parser")
#finding the <p>
paras = soup.find_all('p')
for para in paras:
    print(para.text)