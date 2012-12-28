#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Main access point to the kuklok prototype
'''

from bottle import request, redirect, route, run, template, static_file


# -- routes for  B L O G
@route('/')
def index():
    '''
    Main page view
    '''
    redirect('/blog')

@route('/blog')
def blog():
    '''
    Main page view
    '''
    return template('blog', {'posts': get_blog_posts()})


@route('/blog/<post_id>')
def blog_edit(post_id):
    '''
    Blog post edit view
    '''
    try:
        post = get_blog_posts(int(post_id))
    except ValueError:
        post = None

    return template('blog_edit', {'post': post})


@route('/blog/<post_id>', method='POST')
def blog_save(post_id):
    '''
    Blog post edit view
    '''
    import sqlite3
    import datetime as dt

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    author = request.POST.get('author', '').decode('utf-8')
    title  = request.POST.get('title', '').decode('utf-8')
    text   = request.POST.get('text', '').decode('utf-8')

    try:
        post_id = int(post_id)
        query   = 'UPDATE blog SET author=?, title=?, text=?  WHERE id=?'
        cur.execute(query, (author, title, text, post_id))

    except ValueError:
        date  = '%s' % dt.datetime.now().strftime('%Y.%m.%d %H.%M.%S')
        query = 'INSERT INTO blog VALUES(?,?,?,?,?)'
        cur.execute(query, (None, date, author, title, text))

    con.commit()

    redirect('/blog')

@route('/blog/<post_id>/delete')
def blog_save(post_id):
    '''
    Blog post edit view
    '''
    import sqlite3

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    cur.execute('DELETE FROM blog WHERE id=%d' % int(post_id))
    con.commit()

    redirect('/blog')


# -- routes for  N O T E P A D
@route('/notatki')
def notepad():
    '''
    Main page view
    '''
    return template('notepad', {'notes': get_notes()})


@route('/notatki/<note_id>')
def notepad_edit(note_id):
    '''
    note post edit view
    '''
    try:
        note = get_notes(int(note_id))
    except ValueError:
        note = None

    return template('notepad_edit', {'note': note})


@route('/notatki/<note_id>', method='POST')
def notepad_save(note_id):
    '''
    notepad note edit view
    '''
    import sqlite3
    import datetime as dt

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    author = request.POST.get('author', '').decode('utf-8')
    title  = request.POST.get('title', '').decode('utf-8')
    text   = request.POST.get('text', '').decode('utf-8')

    try:
        note_id = int(note_id)
        query   = 'UPDATE notepad SET author=?, title=?, text=?  WHERE id=?'
        cur.execute(query, (author, title, text, note_id))

    except ValueError:
        date  = '%s' % dt.datetime.now().strftime('%Y.%m.%d %H.%M.%S')
        query = 'INSERT INTO notepad VALUES(?,?,?,?,?)'
        cur.execute(query, (None, date, author, title, text))

    con.commit()

    redirect('/notatki')


@route('/notatki/<note_id>/delete')
def notepad_save(note_id):
    '''
    Notes delete
    '''
    import sqlite3

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    cur.execute('DELETE FROM notepad WHERE id=%d' % int(note_id))
    con.commit()

    redirect('/notatki')


# -- routes for  C A L E N D A R
@route('/terminarz')
def calendar():
    '''
    Main page view
    '''
    return template('calendar', {'todo': get_todos(), 'done': get_done()})


@route('/terminarz/nowe')
def calendar_new():
    return template('calendar_new')


@route('/terminarz/nowe', method='POST')
def calendar_add():
    import sqlite3
    import datetime as dt

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    person = request.POST.get('person', '').decode('utf-8')
    title  = request.POST.get('title', '').decode('utf-8')
    text   = request.POST.get('text', '').decode('utf-8')
    date   = request.POST.get('date', '').decode('utf-8')
    date   = dt.datetime.strptime(date, "%d.%m.%Y")
    date   = date.strftime('%Y.%m.%d %H.%M.%S')

    query = 'INSERT INTO calendar VALUES(?,?,?,?,?,?)'
    cur.execute(query, (None, u'todo', date, person, title, text))

    con.commit()

    redirect('/terminarz')


@route('/terminarz/<todo_id>')
def calendar_done(todo_id):
    '''
    Main page view
    '''
    import sqlite3

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()
    cur.execute("UPDATE calendar SET status='done' WHERE id=%d" % int(todo_id))
    con.commit()

    redirect('/terminarz')


# -- routes for  A D R E S Y
@route('/adresy')
def addresses():
    '''
    Main page view
    '''
    return template('addresses', {'addresses': get_address()})


@route('/adresy/<address_id>')
def addresses_edit(address_id):
    '''
    address post edit view
    '''
    try:
        address = get_address(int(address_id))
    except ValueError:
        address = None

    return template('addresses_edit', {'address': address})


@route('/adresy/<address_id>', method='POST')
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

    redirect('/adresy')

@route('/adresy/newsletter/<address_id>/<newsletter>')
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

@route('/adresy/<address_id>/delete')
def addresses_save(address_id):
    '''
    addresss delete
    '''
    import sqlite3

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    cur.execute('DELETE FROM addresses WHERE id=%d' % int(address_id))
    con.commit()

    redirect('/adresy')

# -- routes for  NEWSLETTER
@route('/newsletter')
def newsletter():
    '''
    Main page view
    '''
    return template('newsletter', {'letters': get_letters()})


@route('/newsletter/nowy')
def newsletter_new():
    '''
    letter post edit view
    '''
    return template('newsletter_edit')


@route('/newsletter/send', method='POST')
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

    redirect('/newsletter')


@route('/newsletter/<letter_id:int>')
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

    redirect('/newsletter')


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

def get_blog_posts(post_id=None):
    '''
    Grabs all blog posts from db
    '''
    import sqlite3

    con = sqlite3.connect('data/data.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute('SELECT * FROM blog ORDER BY date DESC')

    posts = [format_time(dict(e)) for e in cur.fetchall()]

    if post_id:
        return [post for post in posts if post['id'] == int(post_id)].pop()
    else:
        return posts

def format_time(record):
    import time
    tt = time.strptime(record['date'], '%Y.%m.%d %H.%M.%S')
    record['date'] = time.strftime('%d.%m.%Y', tt)

    return record


def get_notes(note_id=None):
    '''
    Grabs all notes notes from db
    '''
    import sqlite3

    con = sqlite3.connect('data/data.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute('SELECT * FROM notepad ORDER BY date DESC')

    notes = [format_time(dict(e)) for e in cur.fetchall()]

    if note_id:
        return [note for note in notes if note['id'] == int(note_id)].pop()
    else:
        return notes


def get_todos():
    '''
    Grabs all todos from db
    '''
    import sqlite3

    con = sqlite3.connect('data/data.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM calendar WHERE status='todo' ORDER BY date DESC")

    todos = [format_time(dict(e)) for e in cur.fetchall()]

    return todos

def get_done():
    '''
    Grabs all done from db
    '''
    import sqlite3

    con = sqlite3.connect('data/data.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM calendar WHERE status='done' ORDER BY date DESC")

    todos = [format_time(dict(e)) for e in cur.fetchall()]

    return todos


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
    run(host='localhost', port=8082, reloader=True)


