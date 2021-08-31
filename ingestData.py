import pandas as pd
import requests
import os
from dotenv import load_dotenv

# Credentials
load_dotenv('.env')
URL = os.environ.get('URL') # URL of our API GateWay

# Read the testfile
data = pd.read_csv('testData.csv', sep = ',')

# Write single row from the testfile into the api
export = data.loc[2].to_json()
response = requests.post(URL, data = export)
print(response)