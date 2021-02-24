import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath(__file__))

def create_post(name, content):
    con = sql.content(path.join(ROOT,'hima.db'))
    cur = con.cursor()
    cur.execute('inser into post(name, content) values(?,?)',(name, content))
    con.commmit()
    con.close()

def get_posts():
    con = sql.connect(path.join(ROOT,'hima.db'))
    cur = con.cursor
    cur.execute('select * from post')
    posts = cur.fetchall()
    return posts