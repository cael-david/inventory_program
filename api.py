import sqlite3

DB_NAME = 'stock.db'

class Api:
    def __init__(self):
        pass

    def _connect(self):
        conn = sqlite3.connect(DB_NAME)
        conn.execute('PRAGMA foreign_keys = ON')
        return conn

    # --- Stocks ---
    def list_stocks(self):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, description FROM stocks ORDER BY name")
        rows = cursor.fetchall()
        conn.close()
        return [{'id': r[0], 'name': r[1], 'description': r[2]} for r in rows]

    def add_stock(self, name, description=''):
        try:
            conn = self._connect()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO stocks (name, description) VALUES (?, ?)", (name, description))
            conn.commit()
            conn.close()
            return {'success': True, 'message': 'Stock added successfully!'}
        except sqlite3.IntegrityError as e:
            return {'success': False, 'message': f'Error: {str(e)}'}

    # --- Products ---
    def list_products(self):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, code, fraction, description FROM products ORDER BY code")
        rows = cursor.fetchall()
        conn.close()
        return [{'id': r[0], 'code': r[1], 'fraction': r[2], 'description': r[3]} for r in rows]

    def add_product(self, code, fraction='', description=''):
        try:
            conn = self._connect()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO products (code, fraction, description) VALUES (?, ?, ?)",
                           (code, fraction, description))
            conn.commit()
            conn.close()
            return {'success': True, 'message': 'Product added successfully!'}
        except sqlite3.IntegrityError as e:
            return {'success': False, 'message': f'Error: {str(e)}'}

    # --- Stock Entries ---
    def list_entries(self):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT se.id, s.name, p.code, p.description, b.bcode, se.quantity, a.street, a.session, a.shelf, se.entry_date
            FROM stock_entries se
            JOIN stocks s ON se.stock_id = s.id
            JOIN products p ON se.product_id = p.id
            JOIN batches b ON se.batch_id = b.id
            JOIN addresses a ON se.address_id = a.id
            ORDER BY se.entry_date DESC
        ''')
        rows = cursor.fetchall()
        conn.close()
        results = []
        for r in rows:
            results.append({
                'id': r[0],
                'stock_name': r[1],
                'product_code': r[2],
                'product_description': r[3],
                'batch_code': r[4],
                'quantity': r[5],
                'street': r[6],
                'session': r[7],
                'shelf': r[8],
                'entry_date': r[9]
            })
        return results

    def add_entry(self, stock_id, product_id, batch_id, address_id, quantity):
        try:
            conn = self._connect()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO stock_entries (stock_id, product_id, batch_id, address_id, quantity)
                VALUES (?, ?, ?, ?, ?)
            ''', (stock_id, product_id, batch_id, address_id, quantity))
            conn.commit()
            conn.close()
            return {'success': True, 'message': 'Stock entry added successfully!'}
        except sqlite3.IntegrityError as e:
            return {'success': False, 'message': f'Error: {str(e)}'}

