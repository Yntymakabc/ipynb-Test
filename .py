import requests

url = "http://127.0.0.1:8000/register"

# Data to send in the POST request
data = {
    "username": "abc",
    "email": "asdfasdfasdf@example.com",
    "password": "asdfsadfsadf"
}

# Sending the POST request
response = requests.post(url, json=data)

# Printing the response
if response.status_code == 200:
    print("User registered successfully:", response.json())
else:
    print("Error:", response.status_code, response.json())
    