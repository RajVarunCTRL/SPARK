import requests
import socket
import time as t


def checkForConnection(host = "8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    
    except socket.error as ex:
        return False


def login(usr,pwd):
# Define the login credentials

    login_url = 'http://172.16.1.1:8090/login.xml'  # Ensure this URL is correct

    # Parameters for the login request
    params = {
        'mode': '191',               # Login mode
        'username': usr,        # Username to log in
        'password': pwd,        # Password for the user
        'a': '1',       # Example timestamp, can be generated dynamically if needed
        'producttype': '0'          # Product type
    }
    while(True):
        if(not checkForConnection()):
            try:
            # Send the POST request for login
                response = requests.post(login_url, data=params)
                status_code = response.status_code

                print(f'Status Code: {status_code}')
                # print(f'Response URL: {response.url}')
                print(f'Response Body: {response.text}')
                # Output the status and response
                
                if status_code == 200:
                        # print(f"Login successful! username: {usr}")
                        pass
                else:
                    print("Login failed.")
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
        else:
            print("Active Connection.")
            print("Program is sleeping. For Approx 30mins")
            t.sleep(1800)
            
            


login( )
