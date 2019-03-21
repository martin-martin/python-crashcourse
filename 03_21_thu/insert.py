import sqlalchemy as sqa


DATABASE_URI = 'postgres+psycopg2://martin:yore2settle@localhost:5432/class'

engine = sqa.create_engine(DATABASE_URI, echo=True)
connection = engine.connect()
metadata = sqa.MetaData()

t2 = sqa.Table('t2', metadata, autoload=True, autoload_with=engine)

# query = sqa.insert(t2).values(
#     quote='to be or not to be',
#     year=1583,
#     greatness=5
# )
# result_proxy = connection.execute(query)


query = sqa.insert(t2)
quotes = [{'quote': 'things change', 'year': 2019, 'greatness': 8},
               {'quote': 'noice', 'year': 2019, 'greatness': 7}]
result_proxy = connection.execute(query, quotes)
