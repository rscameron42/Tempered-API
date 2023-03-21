#!/usr/bin/env python3

# Built-in/Generic Imports
import sys
import requests

# Get Conductor Location and API ClientID & Token
creds = sys.argv[1]
with open(creds, 'r') as f:
    # Read the contents of the file
    contents = f.read()
lines = contents.split('\n')
conductor = lines[0]
api_client_id = lines[1]
api_token = lines[2]

url_fw_updates = "https://" + conductor + "/api/v1/firmware_updates"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "X-API-Client-ID": api_client_id,
    "X-API-Token": api_token
}
# Get Conductor version
query_params = {"paginate": "false", "sort": "version"}
response = requests.get(url_fw_updates, params=query_params, headers=headers, verify=False)
data = response.json()
# Get Available Firmware IDs
query_params = {"paginate": "false", "sort": "version"}
response = requests.get(url_fw_updates, params=query_params, headers=headers, verify=False)
data = response.json()
for item in data:
    id = item.get('id')
    model = item.get('model')
    version = item.get('version')
    description =  item.get('description')
    if (version == "2.2.12" and model == "Airwall-mvebu"):
        aw250_intermetiate = id
    if (version == "2.2.12" and model == "Airwall-x86_64"):
        aw500_intermetiate = id
    if (version == "2.2.12" and model == "Airwall-mvebu64"):
        aw75_intermetiate = id
    if (version == "3.1.2" and model == "Airwall-mvebu"):
        aw250_latest = id
    if (version == "3.1.2" and model == "Airwall-x86_64"):
        aw500_latest = id
    if (version == "3.1.2" and model == "Airwall-mvebu64"):
        aw75_latest = id
    #print(version)

print("Firmware package updates 110, 150, 250, AV3200 series and certain 32-bit ARM 300v Airwalls:")
print("\tversion 2.2.12 = ", aw250_intermetiate, "\n\tversion 3.1.2 =  ", aw250_latest, "\n")
print("Firmware package updates the 100rc, 300v, 310rc, 400, 500, and AV3033 series Airwalls:")
print("\tversion 2.2.12 = ", aw500_intermetiate, "\n\tversion 3.1.2 =  ", aw500_latest, "\n")
print("Firmware package updates 75 series and certain 64-bit ARM 300v Airwalls:")
print("\tversion 2.2.12 = ", aw75_intermetiate, "\n\tversion 3.1.2 =  ", aw75_latest, "\n")
