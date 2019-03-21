import sqlalchemy as sqa
from secrets import username, password
from pprint import pprint


DATABASE_URI = f'postgres+psycopg2://{username}:{password}@localhost:5432/dvdrental'

engine = sqa.create_engine(DATABASE_URI)
connection = engine.connect()
metadata = sqa.MetaData()

actor = sqa.Table('actor', metadata, autoload=True, autoload_with=engine)
film = sqa.Table('film', metadata, autoload=True, autoload_with=engine)

#query = sqa.select([actor])
query = sqa.select([actor]).where(actor.columns.first_name == 'Penelope')
print(query)
print(type(query))


result_proxy = connection.execute(query)
#result_set = result_proxy.fetchall()
result_set = result_proxy.fetchmany(10)

#print(actor.columns.keys())
pprint(result_set)