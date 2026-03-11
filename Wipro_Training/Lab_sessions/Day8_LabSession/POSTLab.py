import requests

try:
    data = {
    "id" : 1,
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}

    response = requests.post("https://api.restful-api.dev/objects", json = data)
    print(response)

    #check if type status code is 200ok
    if response.status_code == 200:
        print("Status code is 200 OK")

        #parse the jason file
        data = response.json()
        print(data)
    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")