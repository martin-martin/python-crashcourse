from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Integer, String, SmallInteger
from secrets import username, password


DATABASE_URI = f'postgres+psycopg2://{username}:{password}@localhost:5432/class'

engine = create_engine(DATABASE_URI, echo=True)
connection = engine.connect()
metadata = MetaData()


test = Table('test', metadata,
            Column('id', Integer(), autoincrement=True, primary_key=True),
            Column('quote', String(255), nullable=False),
            Column('year', Integer()),
            Column('greatness', SmallInteger())
            )

t2 = Table('t2', metadata,
            Column('id', Integer(), autoincrement=True, primary_key=True),
            Column('quote', String(255), nullable=False),
            Column('year', Integer()),
            Column('greatness', SmallInteger())
            )


metadata.create_all(engine)


