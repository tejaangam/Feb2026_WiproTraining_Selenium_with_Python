import requests
from requests.auth import HTTPBasicAuth

try:

    headers = {
        "User-Agent": "MyApp/1.0",
        "Accept": "application/json"
    }
    response = requests.get("https://videogamedb.uk:443/api/v2/videogame", auth = HTTPBasicAuth('username', 'password'), timeout=5, headers=headers )
    print(response)

    #check if type status code is 200ok
    if response.status_code == 200:
        print("Status code is 200 OK")
        #parse the JSON file
        data = response.json()
        #text of the response
        print(response.text)
        #content of the response
        print(response.status_code)
        #headers
        print(response.headers)
        #history
        print(response.history)
        #url
        print(response.url)
        #fetch the single header
        content_type = response.headers.get('Content-Type')
        print(content_type)

        #parse the JSON file
        data = response.json()
        print(data)
    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")