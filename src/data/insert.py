import yaml
import sqlite3

schema = {
    'users'     : ['id', 'name', 'pass', 'grp'],
    'blog'      : ['id', 'grp', 'date', 'author', 'title', 'text'],
    'notepad'   : ['id', 'grp', 'date', 'author', 'title', 'text'],
    'calendar'  : ['id', 'grp', 'status', 'date', 'person', 'title', 'text'],
    'addresses' : ['id', 'grp', 'person', 'name', 'address', 'zip', 'city', 'phone', 'email', 'newsletter'],
    'newsletter': ['id', 'grp', 'date', 'title', 'text']
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


