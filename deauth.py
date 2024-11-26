import requests

# URL for the AJAX logout request (as captured)
ajax_logout_url = 'http://172.16.1.1:8090/logout.xml'

# Parameters for the logout request
params = {
    'mode': '193',           # Logout mode
    'username': '', # Username to log out
    'producttype': '0'        # Product type
}

# AJAX-specific headers
headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)ṇ Chrome/129.0.0.0 Safari/537.36',
    'DNT': '1',  # Do Not Track
    'Referer': 'http://172.16.1.1:8090/',
    'X-Requested-With': 'XMLHttpRequest',  # Important for AJAX requests
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Send the GET request for logcout
response = requests.post(ajax_logout_url, data=params)

# Output the status and response
print(f'Status Code: {response.status_code}')
print(f'Response URL: {response.url}')
print(f'Response Body: {response.text}')
