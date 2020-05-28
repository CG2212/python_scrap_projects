# In this script we will be extracting data from the COVID19INDIA website which provides an API for accessing the contents of the particular state,ditrict which have been affected by the Corona Virus.We will be calculating the number of confirmed and recoverd cases in Pune city.  
import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import pandas as pd
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://api.covid19india.org/state_district_wise.json"
html = urllib.request.urlopen(url, context=ctx).read()
data = json.loads(html)
confirmed = data["Maharashtra"]["districtData"]["Pune"]["confirmed"]
recovered = data["Maharashtra"]["districtData"]["Pune"]["recovered"]
print("No of confirmed cases are:",confirmed)
print("No of recovered cases are:",recovered)
