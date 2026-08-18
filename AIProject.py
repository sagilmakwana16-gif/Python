import os
import requests
import pandas
from importlib.metadata import version
from dotenv import load_dotenv

load_dotenv()

#folder list
folders=("Data","logs","config","src")

#Folser Creater
for folder in folders:
    os.makedirs(folder,exist_ok=True)

#.env file using the python-dotenv library.
api_key=os.getenv("SARVAM_API_KEY")
api_url=os.getenv("API_URL")

print("api_key",api_key)
print("api_url",api_url)

# API Key ko mask karo
if not api_key:
    print("Error: SARVAM_API_KEY is missing in .env file.")
elif not api_url:
    print("Error: API_URL is missing in .env file.")
else:
    masked_key="*" * (len(api_key)-4) + (api_url)[-4:]


print("Install Library Versions")
print("Masked key",masked_key)
print("requests:",requests.__version__)
print("pandas:",pandas.__version__)
print("python-dotenv:",version)
print("Masked API Key:", masked_key)
print("API URL:", api_url)
    