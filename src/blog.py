from bottle import request, template


def main():
    return template('blog', {'posts': _get_blog_posts()})

def edit(post_id):
    try:
        post = _get_blog_posts(int(post_id))
    except ValueError:
        post = None

    return template('blog_edit', {'post': post})

def save(post_id):
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

def delete(post_id):
    import sqlite3

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    cur.execute('DELETE FROM blog WHERE id=%d' % int(post_id))
    con.commit()

def _format_time(record):
    import datetime as dt
    dd = dt.datetime.strptime(record['date'], '%Y.%m.%d %H.%M.%S')
    record['date'] = dd.strftime('%d.%m.%Y')
    record['overdue'] = dt.datetime.now() > dd

    return record

def _get_blog_posts(post_id=None):
    '''
    Grabs all blog posts from db
    '''
    import sqlite3

    con = sqlite3.connect('data/data.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute('SELECT * FROM blog ORDER BY date DESC')

    posts = [_format_time(dict(e)) for e in cur.fetchall()]

    if post_id:
        return [post for post in posts if post['id'] == int(post_id)].pop()
    else:
        return posts
