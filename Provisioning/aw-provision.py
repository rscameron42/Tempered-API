#
import requests
from datetime import datetime, timedelta

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

