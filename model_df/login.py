import cx_Oracle

def login(id, pw):
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('hotel','dbdb', dsn)
    cursor = conn.cursor()

    sql = """select mem_inid, mem_id from member where mem_id = '"""
    sql += id
    sql += "' and mem_pw = '"
    sql += pw
    sql += "'"
    
    
    cursor.execute(sql)
    row = cursor.fetchone()
    
    return row
