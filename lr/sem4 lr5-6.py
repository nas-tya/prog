import sqlite3

try:
    conn = sqlite3.connect('zhukov.db')
except sqlite3.DatabaseError as e:
    print('Couldn\'t connect to the database: ', e)

c = conn.cursor()


def create():
    try:
        c.execute('''PRAGMA table_info(user)''')
    except:
        c.execute('''CREATE TABLE user
          (id int, height real, name text, primary key(id))'''
                  )


def read():
    try:
        crud_read_str = "SELECT * FROM user"
        crud_res = c.execute(crud_read_str)
    except sqlite3.OperationalError as e:
        print(e)
    else:
        for r in crud_res:
            print(r)


def add(name, height):
    try:
        insert_str = 'INSERT INTO user (height, name) VALUES (?, ?)'
        c.execute(insert_str, (height, name))
        conn.commit()
    except sqlite3.OperationalError as e:
        print(e)


def update(id, name, height):
    try:
        if name:
            crud_update_str = 'UPDATE user SET name = ? WHERE id = ?'
            c.execute(crud_update_str, (name, id))
            conn.commit()
        if height:
            crud_update_str = 'UPDATE user SET height = ? WHERE id = ?'
            c.execute(crud_update_str, (height, id))
            conn.commit()
    except sqlite3.OperationalError as e:
        print(e)


def delete(id):
    try:
        crud_delete_str = 'DELETE FROM user WHERE id = ?'
        c.execute(crud_delete_str, (id,))
        conn.commit()
    except sqlite3.OperationalError as e:
        print(e)


# create()
# add('abc', 2)
# delete(6)
# update(7, 'abc1', 2.1)
read()
conn.close()
