#Database implemention and operations

import sqlite3



def create_database():
    conn = sqlite3.connect('rsa_keys.db')
    c = conn.cursor()
    # Creating tables with TEXT type for large integers
    c.execute('''CREATE TABLE IF NOT EXISTS primary_values
                 (id INTEGER PRIMARY KEY, p TEXT, q TEXT, n TEXT, phi TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS key_pairs
                 (id INTEGER PRIMARY KEY, e TEXT, d TEXT, r TEXT,
                  FOREIGN KEY(id) REFERENCES primary_values(id))''')
    conn.commit()
    conn.close()

def store_key_params(p, q, r, n, phi, e, d):
    p, q, r, n, phi, e, d = map(str, (p, q, r, n, phi, e, d))
    conn = sqlite3.connect('rsa_keys.db')
    c = conn.cursor()
    c.execute("INSERT INTO primary_values (p, q, n, phi) VALUES (?, ?, ?, ?)",
              (p, q, n, phi))
    c.execute("INSERT INTO key_pairs (e, d, r) VALUES (?, ?, ?)", (e, d, r))
    conn.commit()
    conn.close()










def fetch_public_key_indexes():
    conn = sqlite3.connect('rsa_keys.db')
    c = conn.cursor()
    c.execute("SELECT e, n FROM key_pairs INNER JOIN primary_values "
              "ON key_pairs.id = primary_values.id")
    result = c.fetchone()
    conn.close()
    return tuple(map(int, result))

def fetch_private_key_indexes():
    conn = sqlite3.connect('rsa_keys.db')
    c = conn.cursor()
    c.execute("SELECT d, n FROM key_pairs INNER JOIN primary_values "
              "ON key_pairs.id = primary_values.id")
    result = c.fetchone()
    conn.close()
    return tuple(map(int, result))


if __name__ == '__main__':
    create_database()


















