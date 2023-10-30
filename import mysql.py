import mysql.connector
import pymysql
import os

try:
    connection=mysql.connector.connect(
        host= 'localhost',
        port= '3306',
        user= 'root',
        password= '',
        db='prueba1'
    )