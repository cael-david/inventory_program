import sqlite3

DB_NAME = 'stock.db'

def connect():
    return sqlite3.connect(DB_NAME)

def insert_stock_entry(name_stock, product_id, batch_id, address_id, quantity):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO stock_entries (name_stock, product_id, batch_id, address_id, quantity)
            VALUES (?, ?, ?, ?, ?)
        ''', (name_stock, product_id, batch_id, address_id, quantity))
        conn.commit()

def get_all_stock_entries():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('''  
            SELECT se.id, se.name_stock, p.code, p.description, b.bcode, a.street, a.session, a.shelf, se.quantity, se.entry_date
            FROM stock_entries se
            JOIN products p ON se.product_id = p.id
            JOIN batches b ON se.batch_id = b.id
            JOIN addresses a ON se.address_id = a.id
        ''')
        return cursor.fetchall()

def delete_stock_entry(entry_id):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM stock_entries WHERE id = ?', (entry_id,))
        conn.commit()

def update_quantity(entry_id, new_quantity):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE stock_entries SET quantity = ? WHERE id = ?', (new_quantity, entry_id))
        conn.commit()

def get_all_products():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products')
        return cursor.fetchall()

def insert_product(code, fraction, description):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('''  
            INSERT INTO products (code, fraction, description)
            VALUES (?, ?, ?)
        ''', (code, fraction, description))
        conn.commit()

def get_all_batches():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM batches')
        return cursor.fetchall()

def insert_batch(bcode, quantity):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('''  
            INSERT INTO batches (bcode, quantity)
            VALUES (?, ?)
        ''', (bcode, quantity))
        conn.commit()

def get_all_addresses():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM addresses')
        return cursor.fetchall()

def insert_address(street, session, shelf):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('''  
            INSERT INTO addresses (street, session, shelf)
            VALUES (?, ?, ?)
        ''', (street, session, shelf))
        conn.commit()

def delete_all_stock_entries():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM stock_entries')
        conn.commit()

def delete_all_products():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM products')
        conn.commit()

def delete_all_batches():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM batches')
        conn.commit()

def delete_all_addresses():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM addresses')
        conn.commit()
