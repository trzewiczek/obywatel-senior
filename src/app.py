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

@route('/notatki/<note_id>')
def notepad_read(note_id):
    '''
    note post edit view
    '''
    note = get_notes(int(note_id))

    return template('notepad_read', {'note': note})

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
def blog_save(note_id):
    '''
    Notes delete
    '''
    import sqlite3

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    cur.execute('DELETE FROM notepad WHERE id=%d' % int(note_id))
    con.commit()

    redirect('/notatki')


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



# -- run the app
if __name__ == '__main__':
    run(host='localhost', port=8082, reloader=True)


