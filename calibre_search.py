import _sqlite3
import os

def calibre_search(library_path,book_name):
    database_path=library_path+'metadata.db'
    conn=_sqlite3.connect(database_path)
    c=conn.cursor()
    query="select path from books where title like \'%"+book_name+"%\';"
    c.execute(query)
    realpath="".join(tuple(c.fetchone())).replace(' ', '\ ')
    realpath=realpath.replace('[','\[')
    #realpath = realpath.replace('[', '\[')
    realpath = realpath.replace(']', '\]')
    realpath = realpath.replace('(', '\(')
    realpath = realpath.replace(')', '\)')
    #print(realpath)
    realpath="open "+library_path+realpath
    #print(realpath)
    os.system(realpath)

