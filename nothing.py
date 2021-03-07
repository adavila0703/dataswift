import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
#format (cid, name, type, notnull, dflt_value, pk)
hello = cur.execute("PRAGMA table_info('new_table')")
# hello = cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
schema = hello.fetchall()

print(schema)

for s in schema:
    print(s)