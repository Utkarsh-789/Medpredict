import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Victus@456",   # 🔴 your MySQL password
    database="medpredict"
)

print("Connected successfully!")