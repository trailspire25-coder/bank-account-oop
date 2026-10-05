import sqlite3

connection = sqlite3.connect("shop.db")

cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY, 
    name TEXT, 
    price REAL
    )
""")
connection.commit()

cursor.execute(
    "INSERT INTO products (name, price) VALUES(?, ?)", 
    ("Laptop", 3500)
)

cursor.execute(
    "INSERT INTO products (name, price) VALUES(?, ?)", 
    ("Phone", 1800)
)


connection.commit()

# cursor.execute("SELECT * FROM products")
cursor.execute("SELECT * FROM products WHERE name = ?", 
    ("Phone",)
)

products = cursor.fetchone()             # connect - cursor - execute - commit - fetch
print(products)


cursor.execute(
    "UPDATE products SET price = ? WHERE name = ?", (2000, "Phone")
)

connection.commit()

cursor.execute(
    "SELECT * FROM products WHERE name = ?", ("Phone",)
)

print(cursor.fetchone())

cursor.execute(
    "DELETE FROM products WHERE id = ?", (7,)
)

connection.commit()

cursor.execute("SELECT * FROM products")

products = cursor.fetchall()
print(products)

