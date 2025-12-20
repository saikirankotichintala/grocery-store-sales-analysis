import mysql.connector 
conn=mysql.connector.connect(host="localhost",user="root",password="Saikiran@12345$")
cursor= conn.cursor()
cursor.execute("CREATE DATABASE GROCERY_STORE")
cursor.execute("USE GROCERY_STORE")
cursor.execute("""CREATE TABLE PRODUCTS( product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price FLOAT,
    stock INT
)
""")
print("Products table created")
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    quantity_sold INT,
    sale_date DATE,
    total_amount FLOAT,
    FOREIGN KEY (product_id) REFERENCES products(product_id))
""")
print("Sales table created")
conn.close()