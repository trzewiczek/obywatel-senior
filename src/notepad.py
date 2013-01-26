from bottle import request, template


def main():
    return template('admin/notepad', {'notes': _get_notes()})

def edit(note_id):
    try:
        note = _get_notes(int(note_id))
    except ValueError:
        note = None

    return template('admin/notepad_edit', {'note': note})

def save(note_id):
    import sqlite3
    import datetime as dt

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    title  = request.POST.get('title', '').decode('utf-8')
    text   = request.POST.get('text', '').decode('utf-8')

    try:
        note_id = int(note_id)
        query   = 'UPDATE notepad SET title=?, text=?  WHERE id=?'
        cur.execute(query, (title, text, note_id))

    except ValueError:
        s = request.environ.get('beaker.session')
        date  = '%s' % dt.datetime.now().strftime('%Y.%m.%d %H.%M.%S')
        query = 'INSERT INTO notepad VALUES(?,?,?,?,?,?)'
        cur.execute(query, (None, s['grp'], date, s['user'], title, text))

    con.commit()


def delete(note_id):
    import sqlite3

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    cur.execute('DELETE FROM notepad WHERE id=%d' % int(note_id))
    con.commit()


def _format_time(record):
    import datetime as dt
    dd = dt.datetime.strptime(record['date'], '%Y.%m.%d %H.%M.%S')
    record['date'] = dd.strftime('%d.%m.%Y')
    record['overdue'] = dt.datetime.now() > dd

    return record

def _get_blog_posts(note_id=None):
    '''
    Grabs all blog posts from db
    '''
    import sqlite3

    con = sqlite3.connect('data/data.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute('SELECT * FROM blog ORDER BY date DESC')

    posts = [_format_time(dict(e)) for e in cur.fetchall()]

    if note_id:
        return [post for post in posts if post['id'] == int(note_id)].pop()
    else:
        return posts


def _get_notes(note_id=None):
    '''
    Grabs all notes notes from db
    '''
    import sqlite3

    con = sqlite3.connect('data/data.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute('SELECT * FROM notepad ORDER BY date DESC')

    notes = [_format_time(dict(e)) for e in cur.fetchall()]

    if note_id:
        return [note for note in notes if note['id'] == int(note_id)].pop()
    else:
        return notes

