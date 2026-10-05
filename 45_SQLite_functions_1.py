import sqlite3

connection = sqlite3.connect("product.db")
cursor = connection.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY, 
        name TEXT NOT NULL UNIQUE, 
        price REAL CHECK (price >= 0),
        stock INTEGER DEFAULT 0
        )
""")
connection.commit()

#   Add starting products only if the table is empty
cursor.execute("SELECT COUNT(*) FROM products")
count = cursor.fetchone()[0]
if count == 0:
    cursor.execute(
        "INSERT INTO products (name, price) VALUES(?, ?)", 
            ("Shoe", 400)
    )

    cursor.execute(
            "INSERT INTO products (name, price) VALUES(?, ?)", 
            ("Shirt", 1000)
        )
    
    cursor.execute(
            "INSERT INTO products (name, price) VALUES(?, ?)", 
            ("Shorts", 300)
        )

    cursor.execute(
            "INSERT INTO products (name, price) VALUES(?, ?)", 
            ("Notebook", 50)
        )
    connection.commit()


def add_product(name, price):
    cursor.execute("SELECT COUNT(*) FROM products WHERE name = ?", 
        (name,)
    )
       
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute(
            "INSERT INTO products (name, price) VALUES(?, ?)", 
                (name, price)
        )
        connection.commit()

    else:
        print("Product already exists.")
    

def get_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    return products


def update_product(name, new_price):
    cursor.execute("UPDATE products SET price = ? WHERE name = ?",
                   (new_price, name)
    )
    
    if cursor.rowcount == 0:
        print("Product not found.")
    else:
        print("Product Updated.")

    connection.commit()

def delete_product(name):
    cursor.execute("DELETE FROM products WHERE name = ?", 
                   (name,)
    )

    if cursor.rowcount == 0:
        print("Product not found.")
    else:
        print("Product Deleted.")
        
    connection.commit()

def get_products_by_price():
    cursor.execute("SELECT * FROM products ORDER BY price DESC;")
    products = cursor.fetchall()
    return products

def get_most_expensive_products(limit):
    cursor.execute("SELECT * FROM products ORDER BY price DESC LIMIT ?;", 
                   (limit,)
    )
    products = cursor.fetchall()
    return products

def search_products(keyword):
    cursor.execute("SELECT * FROM products WHERE name LIKE ?;",
                   (f"%{keyword}%",)
    )
    products = cursor.fetchall()
    return products

def get_products_in_price_range(min_price, max_price):
    cursor.execute("SELECT * FROM products WHERE price >= ? AND price <= ?;", 
                   (min_price, max_price)
    )
    products = cursor.fetchall()
    return products

def get_cheap_or_expensive_products(min_price, max_price):
    cursor.execute("SELECT * FROM products WHERE price < ? OR price > ?;", 
                   (min_price, max_price)
    )
    products = cursor.fetchall()
    return products

def get_selected_products():
    cursor.execute("SELECT * FROM products WHERE name IN (?, ?, ?)", 
                   ("Shoe", "Shirt", "Laptop")
    )
    products = cursor.fetchall()
    return products

def get_total_product_prices():
    cursor.execute("SELECT SUM(price) FROM products")
    products = cursor.fetchone()
    return products

def get_average_product_price():
    cursor.execute("SELECT AVG(price) FROM products")
    products = cursor.fetchone()
    return products

def get_min_product_price():
    cursor.execute("SELECT MIN(price) FROM products")
    products = cursor.fetchone()
    return products

def get_max_product_price():
    cursor.execute("SELECT MAX(price) FROM products")
    products = cursor.fetchone()
    return products

def get_average_group_product_price():
    cursor.execute("SELECT category, AVG(price) FROM products GROUP BY category")
    products = cursor.fetchall()
    return products

def get_sum_group_product_price():
    cursor.execute("SELECT category, SUM(price) FROM products GROUP BY category")
    products = cursor.fetchall()
    return products

def get_sum_group__and_having_product_price():
    cursor.execute("""SELECT category, SUM(price) FROM products GROUP BY category
                    HAVING SUM(price) > 2000""")
    products = cursor.fetchall()
    return products

def get_each_different_category():
    cursor.execute("SELECT DISTINCT category FROM products")
    products = cursor.fetchall()
    return products


try:
    cursor.execute("ALTER TABLE products ADD COLUMN category TEXT")
    connection.commit()
except sqlite3.OperationalError:
    pass

cursor.execute("""UPDATE products SET category = ? WHERE name = ? """,
               ("Electronics", "Laptop"))
connection.commit()

cursor.execute("""UPDATE products SET category = ? WHERE name = ? """,
               ("Clothing", "Shorts"))
connection.commit()

cursor.execute("""UPDATE products SET category = ? WHERE name = ? """,
               ("Clothing", "Shirt"))
connection.commit()


cursor.execute("""UPDATE products SET category = ? WHERE name = ? """,
               ("Clothing", "Shoe"))
connection.commit()


cursor.execute("""SELECT category, COUNT(*) FROM products GROUP BY category
""")

print(cursor.fetchall())


print(get_average_group_product_price())
print(get_sum_group_product_price())
print(get_sum_group__and_having_product_price())
print(get_each_different_category())


print(get_products_by_price())
print(get_most_expensive_products(2))
print(search_products("oe"))

print(get_products_in_price_range(500, 2000))
print(get_cheap_or_expensive_products(400, 1000))
print(get_selected_products())
print(get_total_product_prices())
print(get_average_product_price())
print(get_min_product_price())
print(get_max_product_price())


def reset_suppliers_table():
    cursor.execute("DROP TABLE suppliers")
    connection.commit()

def add_suppliers():
    cursor.execute("""CREATE TABLE IF NOT EXISTS suppliers 
            (id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
    """)
    connection.commit()
    cursor.execute("INSERT OR IGNORE INTO suppliers (name) VALUES (?)",("TechWorld",))
    cursor.execute("INSERT OR IGNORE INTO suppliers (name) VALUES (?)",("FashionHub",))

    connection.commit()

add_suppliers()

cursor.execute("SELECT * FROM suppliers")
print(cursor.fetchall())

try:
    cursor.execute("""ALTER TABLE products ADD COLUMN supplier_id INTEGER""")
except sqlite3.OperationalError:
    pass

cursor.execute("""UPDATE products SET supplier_id = ? WHERE name = ?""",
                (1, "Laptop"))
connection.commit()

cursor.execute("""UPDATE products SET supplier_id = ? WHERE name = ?""",
                (2, "Shoe"))
connection.commit()

cursor.execute("""UPDATE products SET supplier_id = ? WHERE name = ?""",
                (2, "Shirt"))
connection.commit()

cursor.execute("""UPDATE products SET supplier_id = ? WHERE name = ?""",
                (2, "Shorts"))
connection.commit()

cursor.execute("SELECT * FROM products")
print(cursor.fetchall())


def inner_join():
    cursor.execute("""
        SELECT products.name, 
        suppliers.name
        FROM products
        JOIN suppliers
        ON products.supplier_id = suppliers.id
    """)
    print(f"\n{cursor.fetchall()}")

def left_join():
    cursor.execute("""
            SELECT products.name, 
            suppliers.name
            FROM products
            LEFT JOIN suppliers
            ON products.supplier_id = suppliers.id
    """)
    print(cursor.fetchall())

inner_join()
left_join()