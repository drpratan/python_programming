import mysql.connector

mydb = mysql.connector.connect(
        host = 'localhost',
         port='3306',
        user = 'raja',
        passwd = 'cisco'
    )

print (mydb)
