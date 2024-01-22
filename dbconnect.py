import MySQLdb

def connection():
    conn = MySQLdb.connect("localhost","root","2628","pes_students")
    c = conn.cursor()
    return c,conn