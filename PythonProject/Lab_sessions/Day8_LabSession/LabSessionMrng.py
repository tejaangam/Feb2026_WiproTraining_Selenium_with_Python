#Section 1: Basic Level
#1. Write a Python script to send a GET request to https://jsonplaceholder.typicode.com/users and print only name and email.
import requests

try:

    response = requests.get("https://jsonplaceholder.typicode.com/users")
    print(response)

    #check if type status code is 200ok
    if response.status_code == 200:
        print("Status code is 200 OK")

        #parse the jason file
        data = response.json()
        print(data)

        for user in data:
            # Access 'name' and 'email' from the dictionary, not the response object
            print(f"Name: {user['name']}, Email: {user['email']}")
    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")
#2. Send a GET request with query parameter userId=2 and print number of posts returned.
#import requests
# Define the endpoint and parameters
#url = "https://jsonplaceholder.typicode.com/posts?userId=2"
# Send the GET request
#response = requests.get(url)
# Check if the request was successful
#if response.status_code == 200:
 #   posts = response.json()
  #  print(f"Number of posts returned: {len(posts)}")
#else:
 #   print(f"Failed to fetch data. Status code: {response.status_code}")
#3. Write a POST request to create a new resource and verify status code 201.
try:
    data = {
        "name": "Teja Angam",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
             "lat": "-37.3159",
            "lng": "81.1496"
            }
        }
    }
        # make a post request to an api endpoint
    response = requests.post("https://jsonplaceholder.typicode.com/users", json=data)
    print(response)

    # check if type status code is 200ok
    if response.status_code == 200:
        print("Status code is 200 OK")
        # parse the jason file
        data = response.json()
        print(data)
    else:
        print(f"Error: Received status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")

#4. Explain the difference between data= and json= in requests.post().
#5. Write code to check if response status code is not 200 and raise an exception.
import requests
url = "https://jsonplaceholder.typicode.com/posts/9999"  # This will 404
try:
    response = requests.get(url)
    # This line raises an exception if the status is NOT between 200 and 299
    response.raise_for_status()
    # If we get here, the request was successful
    print("Success:", response.json())
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"Other error occurred: {err}")
#Section 2: Intermediate Level
#6. Fetch all users and print usernames in uppercase.
#7. Implement timeout handling (2 seconds) and catch Timeout exception.
#8. Use Session object to send multiple requests and demonstrate cookie persistence.
#9. Upload a file using requests and print server response.
#10. Fetch posts and save response JSON into a file named posts.json.


