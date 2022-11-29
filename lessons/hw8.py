import sqlite3
from sqlite3 import Error



def create_connection(db_file):
    conn = False

def create_table(conn, sql):
    try:
        cursor = conn.cursor







database = r'group_24.db'
def create_student(conn,student):
    sql = '''INSERT INTO student()
    VALUES(?,?,?,?,?)
    
'''

sql_create_student_table = '''
CREATE TABLE student(
id INTEGER PRIMARY KEY AUTOINCREMENT
full_name VARCHAR(50) NOT NULL,
MARK DOUBLE (5,2)  NOT NULL DEFOULT 0.0,
hobby TEXT DEFAULT NULL,
bith_day DATE NOT NULL,
married BOOLEAN DEFAULT FALSE 
);
'''
connection = create_connection(disable)
if connection is not None:
    print('всё работает')
