import yaml
import sqlite3

data = yaml.load(open('sample_data.yaml', 'r').read())

cols = ['id', 'date', 'author', 'title', 'text']

con = sqlite3.connect('data.db')
cur = con.cursor()

for table in data.keys():
    dd = [tuple([doc[k] for k in cols]) for doc in data[table]]
    query = 'INSERT INTO %s VALUES(%s)' % (table, ','.join(['?'] * len(data[table][0].keys())))
    cur.executemany(query, dd)

con.commit()


