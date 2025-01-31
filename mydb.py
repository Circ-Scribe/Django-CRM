import mysql.connector
database=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="crm1"
)

cursorObject=database.cursor()
cursorObject.execute("CREATE DATABASE IF NOT EXISTS crm1")
print("Database created")