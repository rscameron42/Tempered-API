#  The purpose of this script is to search through all of the Airwalls in a particular Conductor
#    and calculate the time they have been offline and if they have been offline for more than
#    90 days, add a tag to them
#
import requests
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText

# Set up the API endpoint, headers, and authentication credentials
url = "https://<insert your conductor URL>/api/v1/hipservices"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "X-API-Client-ID": "<insert your client ID>",
    "X-API-Token": "<insert your API token>"
}

# Set the query parameters
query_params = {"paginate": "false", "sort": "title"}


# Make the GET request
response = requests.get(url, params=query_params, headers=headers, verify=False)

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

# Count the number of Airwalls offline more than 90 days
#   Iterate through the data again - check if airwall is offline more than 90 days
#   Count the number of airwalls offline more than 90 days
#   Print out one line for each airwall with title and time offline

counter = 0
for item in data:
    title = item.get('title')
    serial_number = item.get('serial_number')
    offline_at = item.get('offline_at')
    product_platform = item.get('product_platform')

# Make sure offline_at is not None
    if offline_at is not None:
        time_value_datetime = datetime.strptime(offline_at, "%Y-%m-%dT%H:%M:%S.%fZ")
        current_time = datetime.now()
        time_difference = current_time - time_value_datetime
        if time_difference.days > 90:
            if product_platform == "300v-112": 
                if title and (title.startswith("CEG Airwall") or title.startswith("SBH-300 Airwall")):
                    counter += 1
                    print("{} has been offline for {} days.".format(item['title'], time_difference.days))
        
print("    ")
print(f"The number of Airwalls offline over 90 days is: {counter}")
print("    ")

#  Cycle through again and print id add a tag

tag_to_add = "offline_over_90_days"

# Define json for POST

tags = {
    "tag_refs": [
        tag_to_add
    ]
}
counter = 0

for item in data:
    id = item.get('id')
    title = item.get('title')
    serial_number = item.get('serial_number')
    offline_at = item.get('offline_at')
    product_platform = item.get('product_platform')

# Make sure offline_at is not None
    if offline_at is not None:
        url = "https://obb-dev.tempered.network/api/v1/hipservices"
        time_value_datetime = datetime.strptime(offline_at, "%Y-%m-%dT%H:%M:%S.%fZ")
        current_time = datetime.now()
        time_difference = current_time - time_value_datetime
        if time_difference.days > 90:
            if product_platform == "300v-112": 
                if title and (title.startswith("CEG Airwall") or title.startswith("SBH-300 Airwall")):
                    counter += 1
                    print("{} has been offline for {} days. id={}".format(item['title'], time_difference.days, item['id']))
                    new_url = url + "/" + id + "/tags?id=" + id
                    print(f"The new url: {new_url}")
                    # Post request to add tag
                    response = requests.post(new_url, json=tags, headers=headers, verify=False)
print("    ")                    
print(f"The number of Airwalls offline over 90 days is: {counter}")
print(f"The following tag was added to all Airwalls: {tag_to_add}")
print("    ")

# Check the response status code
if response.status_code == 200:
    # Print the response data
    print("    ")
    print("Successful Response")
    print("    ")
else:
    # Print the error message
    print(f"Error {response.status_code}: {response.text}")


