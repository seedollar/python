import sqlite3

conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)''')
curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')
curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')
new_record = "INSERT INTO zoo (critter, count, damages) VALUES(?,?,?)"
curs.execute(new_record, ('weasel', 1, 2000.00))

curs.execute("SELECT * from zoo")
rows = curs.fetchall()
print(rows)

curs.execute("SELECT * from zoo order by count")
rows_ordered = curs.fetchall()
print(rows_ordered)

curs.close()
conn.close()