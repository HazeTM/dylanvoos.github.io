import mysql.connector

try:
    connection=mysql.connector.connect(
        host= 'localhost',
        port= '3306',
        user= 'root',
        password= '',
        db='prueba1'
    )