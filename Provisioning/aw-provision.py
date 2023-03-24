#!/usr/bin/env python3

# Automate Airwall provisioning steps

"""
Descripion
of script
process
"""

__author__ = "Ron Cameron"
__copyright__ = "Copyright 2023, Tempered Airwall Provisioning"
__credits__ = ["Ron Cameron"]

__license__ = '{license}'
__version__ = "0.0.1"
__maintainer__ = "Ron Cameron"
__email__ = "rscameron@gmail.com"
__status__ = '{dev_status}'

# Futures
#from __future__ import print_function
# […]

# Built-in/Generic Imports
import sys
import requests
from datetime import datetime, timedelta

# Get Conductor Location and API ClientID & Token
creds = sys.argv[1]
with open(creds, 'r') as f:
    # Read the contents of the file
    contents = f.read()

lines = contents.split('\n')

conductor = lines[0]
api_client_id = lines[1]
api_token = lines[2]

# Set up the API endpoints, headers, and authentication credentials
url_aws = "https://" + conductor + "/api/v1/hipservices"
url_aw_groups = "https://" + conductor + "/api/v1/hipservice_groups"
url_fw_updates = "https://" + conductor + "/api/v1/firmware_updates"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "X-API-Client-ID": api_client_id,
    "X-API-Token": api_token
}

# Set the query parameters
query_params = {"paginate": "false", "sort": "title"}

# Make the GET request
response = requests.get(url_aws, params=query_params, headers=headers, verify=False)

# Format the data into json
data = response.json()

# Interate through the data and print and generate output for Airwalls


# Count the number of Airwalls

num_airwalls = 0
for item in data:
    id = item.get('id')
    title = item.get('title')
    serial_number = item.get('serial_number')
    num_airwalls += 1

print("    ")
print(f'Number of Airwalls: {num_airwalls}')
print("    ")

# Create the list of Airwalls to Provision
aw2provision = []

# Set initial Airwall settings and upgrade

for aw in aw2provision:
    # Set Managed flag
    # Set Airwall group
    # Upgrade Airwall

# Setup port-groups

# Set DHCP Passthrough

# Set Device Discovery
