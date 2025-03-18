import requests
import re
from pprint import pprint

log_file_path = './server_log.txt'    # TODO: Replace with your own server log path
black = []

with open(log_file_path, 'r') as file:
    content = file.readlines()
    for line in content:
        ip_address = line.split(' ')[4].strip(':')
        # Construct the API URL
        api_url = "https://ipinfo.io/" + ip_address + "/json"

        # Make the API request
        response = requests.get(api_url)

        if response.status_code == 200:
            # TODO: INSERT YOUR CUSTOM CODE HERE!
            resp = dict(response.json())
            if resp.get('country'):
                if resp['country'] == 'FR':
                    pprint(resp)
                    black.append(resp)
            
        else:
            # TODO: INSERT YOUR CUSTOM CODE HERE!
            pass

with open("./blacklist.txt", 'w') as file:
    for resp in black:
        file.write(f"{resp['ip']}: {resp['city']}, France\nOrg: {resp['org']}")                
