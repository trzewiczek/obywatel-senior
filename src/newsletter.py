from bottle import request, template

def main():
    return template('admin/newsletter', {'letters': _get_letters()})

def new():
    return template('admin/newsletter_edit') 

def send():
    import sqlite3
    import datetime as dt

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    s = request.environ.get('beaker.session')

    date  = dt.datetime.now().strftime('%Y.%m.%d %H.%M.%S')
    title = request.POST.get('title', '').decode('utf-8')
    text  = request.POST.get('text', '').decode('utf-8')

    query = "INSERT INTO newsletter VALUES(?,?,?,?,?)"
    cur.execute(query, (None, s['grp'], date, title, text))
    con.commit()

    _send_letter(title, text)

def resend(letter_id):
    import sqlite3
    import datetime as dt

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    letter_id = int(letter_id)

    query   = 'SELECT title, text FROM newsletter WHERE id=?'
    cur.execute(query, (letter_id,))
    data = cur.fetchone()

    _send_letter(*data)


def _get_letters():
    '''
    Grabs all done from db
    '''
    import sqlite3

    con = sqlite3.connect('data/data.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    s = request.environ.get('beaker.session')
    cur.execute("SELECT * FROM newsletter WHERE grp=%s ORDER BY date DESC" % s['grp'])

    letters = [_format_time(dict(e)) for e in cur.fetchall()]

    return letters


def _send_letter(title, text):
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

def _format_time(record):
    import datetime as dt
    dd = dt.datetime.strptime(record['date'], '%Y.%m.%d %H.%M.%S')
    record['date'] = dd.strftime('%d.%m.%Y')
    record['overdue'] = dt.datetime.now() > dd

    return record
