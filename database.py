import sqlite3

DB_NAME = 'stock.db'

def recreate_database():
    conn = sqlite3.connect(DB_NAME)
    conn.execute('PRAGMA foreign_keys = ON')  # Habilita FK
    cursor = conn.cursor()
    # Cria tabela de estoques (stocks)
    cursor.execute('''
    CREATE TABLE stocks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        description TEXT
    )
    ''')

    # Cria tabela de produtos
    cursor.execute('''
    CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT NOT NULL,
        fraction TEXT,
        description TEXT
    )
    ''')

    # Cria tabela de batches
    cursor.execute('''
    CREATE TABLE batches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bcode TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )
    ''')

    # Cria tabela de addresses
    cursor.execute('''
    CREATE TABLE addresses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        street TEXT NOT NULL,
        session TEXT NOT NULL,
        shelf TEXT NOT NULL
    )
    ''')

    # Cria tabela stock_entries vinculando a tabela stocks
    cursor.execute('''
    CREATE TABLE stock_entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        stock_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        batch_id INTEGER NOT NULL,
        address_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        entry_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (stock_id) REFERENCES stocks(id),
        FOREIGN KEY (product_id) REFERENCES products(id),
        FOREIGN KEY (batch_id) REFERENCES batches(id),
        FOREIGN KEY (address_id) REFERENCES addresses(id)
    )
    ''')

    conn.commit()
    conn.close()
    print("Banco de dados recriado com sucesso!")

# Chame a função para recriar o banco
recreate_database()
