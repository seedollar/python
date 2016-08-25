import sqlalchemy as sa

conn = sa.create_engine("sqlite://")

conn.execute('''CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)''')

insert_statement = "INSERT INTO zoo (critter, count, damages) VALUES(?,?,?)"
conn.execute(insert_statement, 'duck', 10, 0.0)
conn.execute(insert_statement, 'bean', 2, 1000.0)
conn.execute(insert_statement, 'weasel', 10, 2000.50)

rows = conn.execute("SELECT * from zoo")

for row in rows:
    print(row)

