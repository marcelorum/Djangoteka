import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'user',
    passwd = 'password'
)

# Prepare a cursor object

cursorObject = dataBase.cursor()

# Create a DB

cursorObject.execute("CREATE DATABASE db")

print('All Done!')
