import sqlite3

class Database:

    def __init__(self):
        self.conn = sqlite3.connect("expense.db",check_same_thread=False)
        self.create_tables()

    def create_tables(self):

        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS categories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name TEXT UNIQUE
        )
        """)

        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS transactions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        description TEXT,
        amount REAL,
        type TEXT,
        category_id INTEGER,
        source_type TEXT,
        FOREIGN KEY(category_id) REFERENCES categories(id)
        )
        """)

        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS budgets(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER,
        monthly_limit REAL,
        month INTEGER,
        year INTEGER
        )
        """)

    def insert_categories(self,cat):
        self.conn.execute(
        "INSERT OR IGNORE INTO categories(category_name) VALUES(?)",(cat,))
        self.conn.commit()

    def insert_transactions(self,df):
        df.to_sql("transactions",self.conn,
                  if_exists="append",index=False)

    def fetch(self,query):
        import pandas as pd
        return pd.read_sql(query,self.conn)