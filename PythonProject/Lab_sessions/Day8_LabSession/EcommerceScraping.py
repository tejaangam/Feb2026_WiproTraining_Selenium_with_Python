from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/search?q=laptop"
headers = {"User-Agent": "Chrome/144.0.7559.133"}

response = requests.get(url, headers = headers)
print(response.status_code)

#parse the html
soup = BeautifulSoup(response.text, features="html.parser")
#html code is printed
print(soup)

products = soup.find_all("div", class_="_75nlfW")
print(f"--- Found {len(products)} products ---\n")