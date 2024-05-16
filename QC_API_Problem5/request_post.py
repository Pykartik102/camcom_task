import requests

#  base URL of your Flask application
base_url = "http://127.0.0.1:5000"

# Endpoint for /login
login_url = base_url + "/login"

# JSON data containing the username and password
data = {
    "username": "kartik123",
    "password": "kart@123"
}

# Send a POST request to the /login endpoint
response = requests.post(login_url, json=data)

# Check if the response status code indicates success
if response.status_code == 200:
    try:
        # Try to parse the JSON response
        json_response = response.json()
        # Print the JSON response
        print(json_response)
    except requests.exceptions.JSONDecodeError:
        # Print raw response content if JSON decoding fails
        print("Response content is not in JSON format:")
        print(response.text)
else:
    # Print an error message if the request was not successful
    print(f"Request failed with status code {response.status_code}")
    print(response.text)
