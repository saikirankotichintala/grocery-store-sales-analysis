import csv
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Saikiran@12345$",
    database="GROCERY_STORE"
)
cur = conn.cursor()
with open("sales_values.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)   # skip header
    for row in reader:
        # convert empty strings to NULL
        row = [value if value != "" else None for value in row]
        cur.execute(
            """
            INSERT INTO sales (product_id, quantity_sold, sale_date, total_amount)
            VALUES (%s, %s, %s, %s)
            """,
            row
        )
conn.commit()
conn.close()
print("Sales inserted successfully")
