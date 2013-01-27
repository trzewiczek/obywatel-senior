from bottle import request, template


def main():
    return template('admin/addresses', {'addresses': _get_address()})

def edit(address_id):
    try:
        address = _get_address(int(address_id))
    except ValueError:
        address = None

    return template('admin/addresses_edit', {'address': address})

def save(address_id):
    import sqlite3

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    s = request.environ.get('beaker.session')
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
        query = 'INSERT INTO addresses VALUES(?,?,?,?,?,?,?,?,?,?)'
        insert_data = (None, s['grp'], person, name, adrs, zipc, city, phone, email, 0)
        cur.execute(query, insert_data)

    con.commit()

def add_newsletter(address_id, newsletter):
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


def delete(address_id):
    import sqlite3

    con = sqlite3.connect('data/data.db')
    cur = con.cursor()

    cur.execute('DELETE FROM addresses WHERE id=%d' % int(address_id))
    con.commit()


def _format_time(record):
    import datetime as dt
    dd = dt.datetime.strptime(record['date'], '%Y.%m.%d %H.%M.%S')
    record['date'] = dd.strftime('%d.%m.%Y')
    record['overdue'] = dt.datetime.now() > dd

    return record

def _get_address(address_id=None):
    '''
    Grabs all notes notes from db
    '''
    import sqlite3

    con = sqlite3.connect('data/data.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    s = request.environ.get('beaker.session')
    cur.execute('SELECT * FROM addresses WHERE grp=%s ORDER BY name' % s['grp'])

    addresses = [dict(e) for e in cur.fetchall()]

    if address_id:
        return [address for address in addresses if address['id'] == int(address_id)].pop()
    else:
        return addresses
