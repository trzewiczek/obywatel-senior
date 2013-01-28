from bottle import request, redirect, route, run, template, static_file, default_app
from beaker.middleware import SessionMiddleware

def page():
    import sqlite3

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    cur.execute('SELECT name FROM users')
    users = [e[0] for e in cur.fetchall()]

    return template('login', {'error': False, 'users': users})


def check():
    import sqlite3

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    user = request.POST.get('user', '')
    pswd = request.POST.get('pass', '')
    
    cur.execute("SELECT COUNT(*) FROM users WHERE name='%s' AND pass='%s'" % (user, pswd))
    if cur.fetchone()[0] == 1:
        cur.execute("SELECT grp FROM users WHERE name='%s'" % user)
        grp = cur.fetchone()[0]

        s = request.environ.get('beaker.session')
        s['user'] = user.decode('utf-8')
        s['grp']  = grp

        redirect('/admin/blog')
    else:
        cur.execute('SELECT name FROM users')
        users = [e[0] for e in cur.fetchall()]

        return template('login', {'error': True, 'users': users})


def logout():
    s = request.environ.get('beaker.session')
    try:
        del s['user']
        del s['grp']
    except KeyError:
        pass


# TODO make it a real LoginMiddleware
def login_middleware(fn):
    def wrapper(*args, **kwargs):
        s = request.environ.get('beaker.session')
        if 'user' in s:
            log_statistics() 
            return fn(*args, **kwargs)
        else:
            redirect('/admin/login')

    return wrapper


def log_statistics():
    import datetime as dt
    import sqlite3

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    s = request.environ.get('beaker.session')
    date, time = ("%s" % dt.datetime.now()).split(' ')
    cur.execute('INSERT INTO log VALUES(?,?,?,?)', (date, time, s['user'], request.path))
    con.commit()

