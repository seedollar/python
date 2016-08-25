# Example of how to use the SQL Expression Language in SQLAlchemy

import sqlalchemy as sa

connection = sa.create_engine("sqlite://")

meta = sa.MetaData()

zoo = sa.Table('zoo', meta, sa.Column('critter', sa.String, primary_key=True),
               sa.Column('count', sa.Integer),
               sa.Column('damages', sa.Float))

meta.create_all(connection)

connection.execute(zoo.insert(('tiger', 4, 5600.32)))
connection.execute(zoo.insert(('elephant', 2, 8693.05)))
connection.execute(zoo.insert(('giraffe', 1, 392.58)))

result = connection.execute(zoo.select())

rows = result.fetchall()
print(rows)
