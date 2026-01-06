## Module
import requests
import pandas as pd
from datetime import datetime
import mysql.connector
import streamlit as st


## ==================================================
## App : NSW Rest Area Analysis
## 1. Retrive data from database
## 2. Show data using a map chart
## 3. Analyze data with EDA
## ==================================================

try:
    mydb = mysql.connector.connect(
        host="o8nk3m.h.filess.io",
        port="3307",
        user="NSW_Rest_Areas_capoldest",
        password="Abcd1234%^&*",
        database="NSW_Rest_Areas_capoldest",
        ssl_disabled=False,
        connection_timeout=10
    )

    if mydb.is_connected():
        cursor = mydb.cursor()

        cursor.execute("SELECT * FROM dataset")
        rows = cursor.fetchall()

        # Optional: get column names
        columns = [col[0] for col in cursor.description]

        # Convert to pandas DataFrame
        df = pd.DataFrame(rows, columns=columns)

        st.write(df)
        cursor.close()
        mydb.close()

except mysql.connector.Error as err:
    st.write(f"Connection to database error : {err}")
