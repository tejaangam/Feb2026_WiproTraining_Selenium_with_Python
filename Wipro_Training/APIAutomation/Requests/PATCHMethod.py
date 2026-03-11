import requests

try:
    data = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }

#make a post request to an api endpoint
    response = requests.patch("https://api.restful-api.dev/objects/ff8081819782e69e019c50d085b56477", json = data)
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