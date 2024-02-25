# Install Mysql on your computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'NuPashword',
    auth_plugin='mysql_native_password'
)

# prepare a cursor object
cursor_object = database.cursor()

# Create the database
cursor_object.execute("CREATE DATABASE dcrm_data;")

print("All done!")