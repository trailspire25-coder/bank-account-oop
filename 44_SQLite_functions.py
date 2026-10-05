import sqlite3

connection = sqlite3.connect("product.db")
cursor = connection.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY, 
        name TEXT, 
        price REAL
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
        print("Product already exist.")
    

def get_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    return products


def update_products(name, new_price):
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


add_product("Laptop", 3000)
add_product("Phone", 1500)

update_products("Laptop", 3500)

delete_product("Phone")

products = get_products()
print(products)