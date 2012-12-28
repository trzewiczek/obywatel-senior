import yaml
import sqlite3

schema = {
    'blog'      : ['id', 'date', 'author', 'title', 'text'],
    'notepad'   : ['id', 'date', 'author', 'title', 'text'],
    'calendar'  : ['id', 'status', 'date', 'person', 'title', 'text'],
    'addresses' : ['id', 'person', 'name', 'address', 'zip', 'city', 'phone', 'email', 'newsletter'],
    'newsletter': ['id', 'date', 'title', 'text']
}

con = sqlite3.connect('data.db')
cur = con.cursor()

sample_data = yaml.load(open('sample_data.yaml', 'r').read())

for table in sample_data.keys():
    columns = schema[table]
    data    = [tuple([doc[k] for k in columns]) for doc in sample_data[table]]
    query   = 'INSERT INTO %s VALUES(%s)' % (table, ','.join(['?'] * len(columns)))

    cur.executemany(query, data)

con.commit()


