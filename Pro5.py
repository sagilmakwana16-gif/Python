import requests
import json
import time
import os

# Data folder
os.makedirs("data", exist_ok=True)

# User input API
API_key = input("Enter your API: ")

# Start time
start_time = time.time()
try:
# Response
 response = requests.get(API_key)
 print("Response:", response)

# Status code
 status_code = response.status_code

# Response JSON
 data = response.json()

# Raw data save
 with open("data/raw.json", "w") as file:
    json.dump(data, file, indent=3)

# Processing data
 processing_data = []

 for item in data["data"]["data"]:
    processing_data.append({
        "id": item.get("id"),
        "name": item.get("Name"),
        "symbol": item.get("Symbol"),
        "currentPrice": item.get("CurrentPrice")
    })

# Processed data save
 with open("data/processed.json", "w") as file:
    json.dump(processing_data, file, indent=3)

# Number of records
 record = len(data["data"]["data"])

# End time
 end_time = time.time()

# Response time
 response_time = end_time - start_time

# Display
 print("Response time:", response_time)
 print("Record:", record)
 print("Status code:", status_code)
except:
   print("Error")