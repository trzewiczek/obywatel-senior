from bottle import request, template


def main():
    return template('admin/blog', {'posts': _get_blog_posts()})

def edit(post_id):
    try:
        post = _get_blog_posts(int(post_id))
    except ValueError:
        post = None

    return template('admin/blog_edit', {'post': post})

def save(post_id):
    import sqlite3
    import datetime as dt

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    title = request.POST.get('title', '').decode('utf-8')
    text  = request.POST.get('text', '').decode('utf-8')
    path  = request.POST.get('path', '').decode('utf-8')

    try:
        post_id = int(post_id)
        query   = 'UPDATE blog SET title=?, text=?, path=?  WHERE id=?'
        cur.execute(query, (title, text, path, post_id))

    except ValueError:
        s = request.environ.get('beaker.session')
        date  = '%s' % dt.datetime.now().strftime('%Y.%m.%d %H.%M.%S')
        query = 'INSERT INTO blog VALUES(?,?,?,?,?,?,?)'
        cur.execute(query, (None, s['grp'], date, s['user'], title, text, path))

    con.commit()

def delete(post_id):
    import sqlite3

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

#    cur.execute('SELECT path FROM blog WHERE id=%s' % post_id)
#    path = cur.fetchone()[0]
#    if path:
#        import os
#        os.remove('.'+path)

    cur.execute('DELETE FROM blog WHERE id=%d' % int(post_id))
    con.commit()


def upload():
    import os
    import StringIO

    upload = request.POST.get('upload')
    fname  = upload.filename
    imgdir = 'static/images/uploads/'

    while os.path.exists(imgdir + fname):
        fname = '0'+fname

    path = imgdir + fname

    f = open(path, 'wb')
    f.write(upload.file.read())
    f.close()

    import Image
    img = Image.open(path)
    img.thumbnail((500, 500), Image.ANTIALIAS)
    img.save(path)

    return '/%s' % path


def _format_time(record):
    import datetime as dt
    dd = dt.datetime.strptime(record['date'], '%Y.%m.%d %H.%M.%S')
    record['date'] = dd.strftime('%d.%m.%Y')
    record['overdue'] = dt.datetime.now() > dd

    return record

def _get_blog_posts(post_id=None):
    s = request.environ.get('beaker.session')

    import sqlite3

    con = sqlite3.connect('data/data.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute('SELECT * FROM blog WHERE grp=%s ORDER BY date DESC' % s['grp'])

    posts = [_format_time(dict(e)) for e in cur.fetchall()]

    if post_id:
        return [post for post in posts if post['id'] == int(post_id)].pop()
    else:
        return posts

