import csv
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Saikiran@12345$",
    database="GROCERY_STORE"
)

cur = conn.cursor()

with open("products_values.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)   # skip header

    for row in reader:
        # convert empty strings to NULL
        row = [value if value != "" else None for value in row]

        cur.execute(
            "INSERT INTO products (product_name, category, price, stock) VALUES (%s,%s,%s,%s)",
            row
        )

conn.commit()
conn.close()

print("Products inserted successfully")
