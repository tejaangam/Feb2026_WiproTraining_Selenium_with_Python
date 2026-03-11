from bs4 import BeautifulSoup
import requests

#1.Install and import BeautifulSoup from the bs4 module.
#Write a simple program to parse a small HTML string.

html_doc = """
<html>
  <head><title>Test Page</title></head>
  <body>
    <h1>Welcome</h1>
    <p>This is a paragraph.</p>
    <a href="https://google.com"/></a>
  </body></html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup)

#extract the title
print(soup.title.string)

#extracting the <h1>
print(soup.find("h1"))

#extracting the paragraph
print(soup.find("p").text)

#extracting the <a>
print(soup.find("a"))

#getting href attribute
print(soup.get("href"))

first_anchor = soup.select_one('a')
print(first_anchor['href'])