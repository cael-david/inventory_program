import sqlite3

DB_NAME = 'stock.db'

class StockController:
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_stock(self, name):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO stocks (name) VALUES (?)', (name,))
            conn.commit()
            return cursor.lastrowid

    def get_stock(self, stock_id):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, name FROM stocks WHERE id = ?', (stock_id,))
            row = cursor.fetchone()
            if row:
                return {"stock_id": row[0], "name": row[1]}
            return None

    def get_all_stocks(self):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, name FROM stocks')
            rows = cursor.fetchall()
            return [{"stock_id": r[0], "name": r[1]} for r in rows]

    def delete_stock(self, stock_id):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM stocks WHERE id = ?', (stock_id,))
            conn.commit()

    def get_stock_entries(self, stock_id):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT se.id, se.name_stock, p.code, p.description, b.bcode, a.street, a.session, a.shelf, se.quantity, se.entry_date
                FROM stock_entries se
                JOIN products p ON se.product_id = p.id
                JOIN batches b ON se.batch_id = b.id
                JOIN addresses a ON se.address_id = a.id
                WHERE se.stock_id = ?
            ''', (stock_id,))
            return cursor.fetchall()
