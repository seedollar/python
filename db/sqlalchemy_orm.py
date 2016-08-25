# Example to show how you can use ORM strategy using SQLAlchemy library

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

connection = sa.create_engine("sqlite:///zoo.db")

Base = declarative_base()
class Zoo(Base):
    __tablename__ = 'zoo'
    critter = sa.Column('critter', sa.String, primary_key=True)
    count = sa.Column('count', sa.Integer)
    damages = sa.Column('damages', sa.Float)

    def __init__(self, critter, count, damages):
        self.critter = critter
        self.count = count
        self.damages = damages

    def __repr__(self):
        return "<Zoo({}. {}, {})>".format(self.critter, self.count, self.damages)


Base.metadata.create_all(connection)

snake = Zoo('snake', 16, 860.46)
cow = Zoo('cow', 5, 94.74)
lion = Zoo('lion', 3, 883.34)

Session = sessionmaker(bind=connection)
session = Session()

session.add(snake)
session.add_all([cow, lion])

session.commit()



