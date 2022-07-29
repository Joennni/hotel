import pandas as pd
import cx_Oracle


def select_basic():
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('hotel', 'dbdb', dsn)
    cursor = conn.cursor()
    
    sql = """"""
    
    cursor.execute(sql)
    row = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return row

def iu_basic():
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('hotel', 'dbdb', dsn)
    cursor = conn.cursor()
    
    sql = """"""
    
    cursor.execute(sql)
    conn.commit()
    
    cursor.close()
    conn.close()
    
    
def adminMemberShow():
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('hotel', 'dbdb', dsn)
    cursor = conn.cursor()
    
    sql = """select mem_inid as A, mem_id, mem_inid, mem_name, mem_email, 
            '0' || to_char(mem_tel),
            decode(trunc(mem_regno / 100000), 0, to_date(20000000 + mem_regno, 'yyyymmdd'), to_date(19000000 + mem_regno, 'yyyymmdd')) as mem_bir, 
            decode(mem_gender, 1, '남성', '여성') as mem_gender, 
            mem_add, mem_date
            from member
            order by mem_inid asc"""

    
    cursor.execute(sql)
    row = cursor.fetchall()
    
    cursor.close()
    conn.close()    
    
    return row

def adminMemberDelete(id):
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('hotel', 'dbdb', dsn)
    cursor = conn.cursor()
    
    sql = """delete from reserve where res_mem = """
    sql += id
    cursor.execute(sql)
    
    sql = """delete from post where post_mem = """
    sql += id
    cursor.execute(sql)
    
    sql = """delete from member where mem_inid = """
    sql += id
    cursor.execute(sql)
    
    conn.commit()
    
    sql = """select mem_inid as A, mem_id, mem_inid, mem_name, mem_email, 
            '0' || to_char(mem_tel),
            decode(trunc(mem_regno / 100000), 0, to_date(20000000 + mem_regno, 'yyyymmdd'), to_date(19000000 + mem_regno, 'yyyymmdd')) as mem_bir, 
            decode(mem_gender, 1, '남성', '여성') as mem_gender, 
            mem_add, mem_date
            from member
            order by mem_inid asc"""

    
    cursor.execute(sql)
    row = cursor.fetchall()
    
    cursor.close()
    conn.close()    
    
    return row


def join(id, pw, m_name, m_email, tel, regno, gender):
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('hotel', 'dbdb', dsn)
    cursor = conn.cursor()
    
    sql = """insert into member (mem_id, mem_pw, mem_name, mem_email, mem_tel, mem_regno, mem_gender, mem_date, mem_add, mem_staff, mem_cardno, mem_cdpw) values('"""
    sql += id
    sql += "','"
    sql += pw
    sql += "','"
    sql += m_name
    sql += "','"
    sql += m_email
    sql += "','"
    sql += tel
    sql += "','"
    sql += regno 
    sql += "','"
    sql += gender    
    sql += "','"
    sql += '20220506'    
    sql += "','"
    sql += '세종시 조치원'    
    sql += "','"
    sql += '0'    
    sql += "','"
    sql += ''    
    sql += "','"
    sql += ''   
    sql += "')"
    cursor.execute(sql)
    conn.commit()
    
    sql = """select mem_name, mem_id, mem_date from member where mem_id = '"""
    sql += id
    sql += "'"
    cursor.execute(sql)
    row = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    
    return row

def update(id):
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('hotel', 'dbdb', dsn)
    cursor = conn.cursor()
    
    sql = """select mem_name, mem_id, mem_pw, mem_regno, 
    decode(mem_gender, 1, '남성', '여성'), 
    mem_tel, mem_email  from member where mem_id = '"""
    sql += id
    sql += "'"

    cursor.execute(sql)
    row = cursor.fetchone()
 
    cursor.close()
    conn.close()
    
    return row

def update_suc(id, pw, regno, tel, email):
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('hotel', 'dbdb', dsn)
    cursor = conn.cursor()
    
    sql = """update member set mem_pw = '"""
    sql += pw
    sql += "', mem_regno = '"
    sql += regno
    sql += "', mem_tel = '"
    sql += tel
    sql += "', mem_email = '"
    sql += email
    sql += "' where mem_inid = "
    sql += id
    
    cursor.execute(sql)
    conn.commit()
    
    cursor.close()
    conn.close()