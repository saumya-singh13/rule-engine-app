import sqlite3

DB_PATH = "rules.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rule TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_rule_to_db(rule_str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO rules (rule) VALUES (?)", (rule_str,))
    rule_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return rule_id

def get_rule_from_db(rule_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT rule FROM rules WHERE id = ?", (rule_id,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None
