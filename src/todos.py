from bottle import request, template


def main():
    return template('admin/calendar', {'todo': _get_todos(), 'done': _get_done()})

def new_task():
    return template('admin/calendar_new', {'users': _get_users()})

def add():
    import sqlite3
    import datetime as dt

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    s = request.environ.get('beaker.session')

    person = request.POST.get('person', '').decode('utf-8')
    title  = request.POST.get('title', '').decode('utf-8')
    text   = request.POST.get('text', '').decode('utf-8')
    date   = request.POST.get('date', '').decode('utf-8')
    date   = dt.datetime.strptime(date, "%d.%m.%Y")
    date   = date.strftime('%Y.%m.%d %H.%M.%S')

    query = 'INSERT INTO calendar VALUES(?,?,?,?,?,?,?,?)'
    cur.execute(query, (None, s['grp'], u'todo', date, person, title, text, s['user']))

    con.commit()

def done(todo_id):
    import sqlite3

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    s = request.environ.get('beaker.session')
    cur.execute("UPDATE calendar SET status='done', author='%s' WHERE id=%d" % (s['user'], int(todo_id)))
    con.commit()

def _get_todos():
    '''
    Grabs all todos from db
    '''
    import sqlite3

    con = sqlite3.connect('data/data.db')
    con.row_factory = sqlite3.Row

    s = request.environ.get('beaker.session')

    cur = con.cursor()
    cur.execute("SELECT * FROM calendar WHERE status='todo' AND grp=%s ORDER BY date" % s['grp'])

    todos = [_format_time(dict(e)) for e in cur.fetchall()]

    return todos


def _get_users():
    import sqlite3

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    s = request.environ.get('beaker.session')
    cur.execute("SELECT name FROM users WHERE grp=%s ORDER BY name" % s['grp'])

    users = [e[0] for e in cur.fetchall()]

    return users


def _get_done():
    '''
    Grabs all done from db
    '''
    import sqlite3

    con = sqlite3.connect('data/data.db')
    con.row_factory = sqlite3.Row

    s = request.environ.get('beaker.session')

    cur = con.cursor()
    cur.execute("SELECT * FROM calendar WHERE status='done' AND grp=%s ORDER BY date DESC" % s['grp'])

    todos = [_format_time(dict(e)) for e in cur.fetchall()]

    return todos

def _format_time(record):
    import datetime as dt
    dd = dt.datetime.strptime(record['date'], '%Y.%m.%d %H.%M.%S')
    record['date'] = dd.strftime('%d.%m.%Y')
    record['overdue'] = dt.datetime.now() > dd

    return record

