#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Main access point to the kuklok prototype
'''

from bottle import request, redirect, route, run, template, static_file, default_app
from beaker.middleware import SessionMiddleware

import addresses
import blog
import todos
import notepad
import newsletter
import login
from login import login_middleware

DEBUG = True

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 3600,
    'session.data_dir': './session_data',
    'session.auto': True
}
app = SessionMiddleware(default_app(), session_opts)


# -- routes for  P U B L I C  B L O G
@route('/')
def index():
    return template('main', get_posts())

@route('/<grp:int>')
def group_blog(grp):
    return template('blog', get_posts(grp))


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
def notepad_delete(note_id):
    notepad.delete(note_id)
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
@login_middleware
def todos_done(todo_id):
    todos.done(todo_id)
    redirect('/admin/terminarz')


# -- routes for  A D R E S Y
@route('/admin/adresy')
@login_middleware
def addresses_main():
    return addresses.main()


@route('/admin/adresy/<address_id>')
@login_middleware
def addresses_edit(address_id):
    return addresses.edit(address_id)

@route('/admin/adresy/<address_id>', method='POST')
@login_middleware
def addresses_save(address_id):
    addresses.save(address_id)
    redirect('/admin/adresy')

@route('/admin/adresy/newsletter/<address_id>/<newsletter>')
@login_middleware
def addresses_newsletter(address_id, newsletter):
    addresses.add_newsletter(address_id, newsletter)
    return ''

@route('/admin/adresy/<address_id>/delete')
@login_middleware
def addresses_delete(address_id):
    addresses.delete(address_id)
    redirect('/admin/adresy')

# -- routes for  NEWSLETTER
@route('/admin/newsletter')
@login_middleware
def newsletter_main():
    return newsletter.main()

@route('/admin/newsletter/nowy')
@login_middleware
def newsletter_new():
    return newsletter.new()


@route('/admin/newsletter/send', method='POST')
@login_middleware
def newsletter_send():
    newsletter.send()
    redirect('/admin/newsletter')


@route('/admin/newsletter/<letter_id:int>')
@login_middleware
def newsletter_resend(letter_id):
    newsletter.resend(letter_id)
    redirect('/admin/newsletter')


# -- hiper admin routes
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


# -- routes for  L O G I N
@route('/admin/login')
def login_page():
    return login.page()

@route('/admin/check_login', method='POST')
def check_login_page():
    return login.check()

@route('/admin/logout')
def logout():
    login.logout()
    redirect('/')

# -- run the app
if __name__ == '__main__':
    if DEBUG:
        run(app=app, host='localhost', port=8082, reloader=True)
    else:
        application = app


