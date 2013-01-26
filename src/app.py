#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Main access point to the kuklok prototype
'''

from bottle import request, redirect, route, run, template, static_file, default_app
from beaker.middleware import SessionMiddleware

import blog
import todos
import notepad

DEBUG = True

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './session_data',
    'session.auto': True
}
app = SessionMiddleware(default_app(), session_opts)

# TODO make it a real LoginMiddleware
def login_middleware(fn):
    def wrapper(*args, **kwargs):
        s = request.environ.get('beaker.session')
        if 'user' in s:
            return fn(*args, **kwargs)
        else:
            redirect('/admin/login')

    return wrapper

@route('/')
def index():
    return template('main', get_posts())

@route('/<grp:int>')
def group_blog(grp):
    return template('blog', get_posts(grp))


# -- routes for  L O G I N
@route('/admin/login')
def login_page():
    import sqlite3

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    cur.execute('SELECT name FROM users')
    users = [e[0] for e in cur.fetchall()]

    return template('login', {'error': False, 'users': users})

@route('/admin/check_login', method='POST')
def check_login_page():
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
        s['user'] = user
        s['grp']  = grp

        redirect('/admin/blog')
    else:
        cur.execute('SELECT name FROM users')
        users = [e[0] for e in cur.fetchall()]

        return template('login', {'error': True, 'users': users})

@route('/admin/logout')
def logout():
    s = request.environ.get('beaker.session')
    try:
        del s['user']
        del s['grp']
    except KeyError:
        pass

    redirect('/')

# -- routes for  B L O G
@route('/admin')
def index():
    redirect('/admin/blog')


@route('/admin/blog')
@login_middleware
def blog_main():
    return blog.main()

@route('/admin/blog/<post_id>')
@login_middleware
def blog_edit(post_id):
    return blog.edit(post_id)

@route('/admin/blog/<post_id>', method='POST')
@login_middleware
def blog_save(post_id):
    blog.save(post_id)
    redirect('/admin/blog')

@route('/admin/blog/<post_id>/delete')
@login_middleware
def blog_delete(post_id):
    blog.delete(post_id)
    redirect('/admin/blog')


# -- routes for  N O T E P A D
@route('/admin/notatki')
@login_middleware
def notepad_main():
    return notepad.main()

@route('/admin/notatki/<note_id>')
@login_middleware
def notepad_edit(note_id):
    return notepad.edit(note_id)

@route('/admin/notatki/<note_id>', method='POST')
@login_middleware
def notepad_save(note_id):
    notepad.save(note_id)
    redirect('/admin/notatki')


@route('/admin/notatki/<note_id>/delete')
@login_middleware
def notepad_save(note_id):
    notepad.save(note_id)
    redirect('/admin/notatki')


# -- routes for  C A L E N D A R
@route('/admin/terminarz')
@login_middleware
def todos_main():
    return todos.main()


@route('/admin/terminarz/nowe')
@login_middleware
def todos_new():
    return todos.new_task()


@route('/admin/terminarz/nowe', method='POST')
@login_middleware
def todos_add():
    todos.add()
    redirect('/admin/terminarz')


@route('/admin/terminarz/<todo_id>')
def todos_done(todo_id):
    todos.done(todo_id)
    redirect('/admin/terminarz')


# -- routes for  A D R E S Y
@route('/admin/adresy')
def addresses():
    '''
    Main page view
    '''
    return template('addresses', {'addresses': get_address()})


@route('/admin/adresy/<address_id>')
def addresses_edit(address_id):
    '''
    address post edit view
    '''
    try:
        address = get_address(int(address_id))
    except ValueError:
        address = None

    return template('addresses_edit', {'address': address})


@route('/admin/adresy/<address_id>', method='POST')
def addresses_save(address_id):
    '''
    addresses address edit view
    '''
    import sqlite3

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    person = request.POST.get('person', '').decode('utf-8')
    name   = request.POST.get('name', '').decode('utf-8')
    adrs   = request.POST.get('address', '').decode('utf-8')
    zipc   = request.POST.get('zip', '').decode('utf-8')
    city   = request.POST.get('city', '').decode('utf-8')
    phone  = request.POST.get('phone', '').decode('utf-8')
    email  = request.POST.get('email', '').decode('utf-8')

    try:
        address_id = int(address_id)
        query = '''UPDATE addresses
                   SET person=?, name=?, address=?, zip=?, city=?, phone=?, email=?
                   WHERE id=?'''
        update_data = (person, name, adrs, zipc, city, phone, email, address_id)
        cur.execute(query, update_data)

    except ValueError:
        query = 'INSERT INTO addresses VALUES(?,?,?,?,?,?,?,?,?)'
        insert_data = (None, person, name, adrs, zipc, city, phone, email, 0)
        cur.execute(query, insert_data)

    con.commit()

    redirect('/admin/adresy')

@route('/admin/adresy/newsletter/<address_id>/<newsletter>')
def addresses_newsletter(address_id, newsletter):
    import sqlite3

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    address_id = int(address_id)
    newsletter = int(newsletter)

    query = '''UPDATE addresses
               SET newsletter=?
               WHERE id=?'''
    cur.execute(query, (newsletter, address_id))
    con.commit()

    return ''

@route('/admin/adresy/<address_id>/delete')
def addresses_save(address_id):
    '''
    addresss delete
    '''
    import sqlite3

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    cur.execute('DELETE FROM addresses WHERE id=%d' % int(address_id))
    con.commit()

    redirect('/admin/adresy')

# -- routes for  NEWSLETTER
@route('/admin/newsletter')
def newsletter():
    '''
    Main page view
    '''
    return template('newsletter', {'letters': get_letters()})


@route('/admin/newsletter/nowy')
def newsletter_new():
    '''
    letter post edit view
    '''
    return template('newsletter_edit')


@route('/admin/newsletter/send', method='POST')
def newsletter_send():
    '''
    newsletter letter edit view
    '''
    import sqlite3
    import datetime as dt

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    date  = dt.datetime.now().strftime('%Y.%m.%d %H.%M.%S')
    title = request.POST.get('title', '').decode('utf-8')
    text  = request.POST.get('text', '').decode('utf-8')

    query = "INSERT INTO newsletter VALUES(?,?,?,?)"
    cur.execute(query, (None, date, title, text))
    con.commit()

    send_letter(title, text)

    redirect('/admin/newsletter')


@route('/admin/newsletter/<letter_id:int>')
def newsletter_resend(letter_id):
    '''
    letter post edit view
    '''
    import sqlite3
    import datetime as dt

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    letter_id = int(letter_id)

    query   = 'SELECT title, text FROM newsletter WHERE id=?'
    cur.execute(query, (letter_id,))
    data = cur.fetchone()

    send_letter(*data)

    redirect('/admin/newsletter')


@route('/deletealldata')
def delete_all_data():
    return template('deletealldata')


@route('/reallydeletealldata', method='POST')
def really_delete_all_data():
    if request.POST.get('password', '') == 'kozak':
        queries = [
            "DELETE FROM blog",
            "DELETE FROM notepad",
            "DELETE FROM calendar",
            "DELETE FROM addresses",
            "DELETE FROM newsletter"
        ]

        import sqlite3

        con = sqlite3.connect('data/data.db')
        cur = con.cursor()

        for query in queries:
            cur.execute(query)

        con.commit()

    redirect('/')

# -- routes for S T A T I C   F I L E S
@route('/upload', method='POST')
def upload():
    upload = request.POST.get('upload')
    path = 'static/images/uploads/%s' % upload.filename

    f = open(path, 'wb')
    f.write(upload.file.read())
    f.close()

    return '/%s' % path


@route('/static/<path:path>')
def serve_files(path):
    '''
    Static files route
    '''
    return static_file(path, root='static/')

def get_posts(grp=None):
    '''
    Grabs all blog posts from db
    '''
    import sqlite3

    con = sqlite3.connect('data/data.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()

    if grp:
        cur.execute('SELECT * FROM blog WHERE grp = ? ORDER BY date DESC', (grp,))
        return {'posts': [format_time(dict(e)) for e in cur.fetchall()]}
    else:
        cur.execute('SELECT * FROM blog WHERE grp = 1 ORDER BY date DESC')
        grp_one = [format_time(dict(e)) for e in cur.fetchall()]

        cur.execute('SELECT * FROM blog WHERE grp = 2 ORDER BY date DESC')
        grp_two = [format_time(dict(e)) for e in cur.fetchall()]

        return {'grp_one': grp_one, 'grp_two': grp_two}


def format_time(record):
    import datetime as dt
    dd = dt.datetime.strptime(record['date'], '%Y.%m.%d %H.%M.%S')
    record['date'] = dd.strftime('%d.%m.%Y')
    record['overdue'] = dt.datetime.now() > dd

    return record





def get_address(address_id=None):
    '''
    Grabs all notes notes from db
    '''
    import sqlite3

    con = sqlite3.connect('data/data.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute('SELECT * FROM addresses ORDER BY name')

    addresses = [dict(e) for e in cur.fetchall()]

    if address_id:
        return [address for address in addresses if address['id'] == int(address_id)].pop()
    else:
        return addresses

def get_letters():
    '''
    Grabs all done from db
    '''
    import sqlite3

    con = sqlite3.connect('data/data.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM newsletter ORDER BY date DESC")

    letters = [format_time(dict(e)) for e in cur.fetchall()]

    return letters


def send_letter(title, text):
    import sqlite3
    import smtplib
    from email.mime.text import MIMEText
    from email.Utils import formataddr

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()
    cur.execute("SELECT email FROM addresses WHERE newsletter=1")

    for email in [e[0] for e in cur.fetchall()]:
        msg = MIMEText(text, 'html', 'utf-8')

        msg['Subject'] = title
        msg['From'] = 'krzysztof@trzewiczek.info'
        msg['To'] = email

        print msg.as_string()
#        s = smtplib.SMTP('localhost')
#        s.sendmail('krzysztof@trzewiczek.info', email, msg.as_string())
#        s.quit()



# -- run the app
if __name__ == '__main__':
    if DEBUG:
        run(app=app, host='localhost', port=8082, reloader=True)
    else:
        application = app


