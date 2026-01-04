## Module
import requests
import pandas as pd
from datetime import datetime
import streamlit as st


## ==================================================
## App : NSW Rest Area Analysis
## 1. Retrive data from API
## 2. Store data into a dataframe
## 3. Show data using a map chart
## 4. Analyze data with EDA
## ==================================================


api_url2 = "https://api.transport.nsw.gov.au/v1/roads/spatial"
headers = {
    "accept": "application/json",
    "Authorization": "apikey eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJOOF9jQlNEb1l6ajQ2M1NyVlFvZi03QjAyTkYyZXh5XzZwR1dfM29FeElvIiwiaWF0IjoxNzY3NDM0Nzg0fQ.nuvoL0Uyv9s4PUWw6V8jG7zvR3S6e9XJbAl6jN11f5o"
}
format = "json"
query = "select * from rest_areas"
req_api_url = f'''{api_url2}?format={format}&q={query.replace(" ", "%20")}'''

response = requests.get(req_api_url, headers=headers)

if response.status_code == 200:
    data = response.json()
    rows = []
    for feature in data["features"]:
        attrs = feature["attributes"]
        geometry = feature.get("geometry", {})
        points = geometry.get("points", [[None, None]])
        longitude, latitude = points[0]
        row = {
            # metadata (similar to your timestamps)
            "retrieved_timestamp": datetime.utcnow().timestamp(),
            "retrieved_datetime": datetime.utcnow(),

            # geometry
            "longitude": longitude,
            "latitude": latitude,
        }
        # merge all attributes dynamically
        row.update(attrs)
        rows.append(row)

    df = pd.DataFrame(rows)

    st.write(df)
    
else:
    st.write(f"Error code : {response.status_code}")
    st.write(f"An error occurred : {requests.exceptions.RequestException}")
