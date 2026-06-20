import sqlite3

# Connect to database
conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
)
""")
conn.commit()

def add_product():
    pid = int(input("Enter Product ID: "))
    name = input("Enter Product Name: ")
    qty = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))

    cursor.execute(
        "INSERT INTO products VALUES (?, ?, ?, ?)",
        (pid, name, qty, price)
    )
    conn.commit()
    print("Product added successfully.")

def view_products():
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    print("\nInventory:")
    print("-" * 50)
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Qty: {row[2]}, Price: {row[3]}")
    print("-" * 50)

def update_quantity():
    pid = int(input("Enter Product ID: "))
    qty = int(input("Enter New Quantity: "))

    cursor.execute(
        "UPDATE products SET quantity=? WHERE product_id=?",
        (qty, pid)
    )
    conn.commit()
    print("Quantity updated.")

def delete_product():
    pid = int(input("Enter Product ID: "))

    cursor.execute(
        "DELETE FROM products WHERE product_id=?",
        (pid,)
    )
    conn.commit()
    print("Product deleted.")

def search_product():
    pid = int(input("Enter Product ID: "))

    cursor.execute(
        "SELECT * FROM products WHERE product_id=?",
        (pid,)
    )

    product = cursor.fetchone()

    if product:
        print(product)
    else:
        print("Product not found.")

while True:
    print("\n=== Inventory Management System ===")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Quantity")
    print("4. Delete Product")
    print("5. Search Product")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_product()
    elif choice == '2':
        view_products()
    elif choice == '3':
        update_quantity()
    elif choice == '4':
        delete_product()
    elif choice == '5':
        search_product()
    elif choice == '6':
        break
    else:
        print("Invalid choice!")

conn.close()