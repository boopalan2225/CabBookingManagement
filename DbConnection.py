import streamlit as st
import mysql.connector

host = "localhost"
user = "root"
password = "Root@123"
database = "CabBookingManagement"

try:
# Create a connection to the MySQL server
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

except mysql.connector.Error as err:
    print("MySQL Connection Error: {}".format(err))

def getDbConnectionCursor():
    connectionStatus = connection.is_connected()
    if connectionStatus:
            print("Connected to MySQL")
            return connection.cursor()    # Create a cursor object
    else:
        st.write(f"Connection to MySQL failed {connectionStatus}")