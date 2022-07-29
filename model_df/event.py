import pandas as pd
import cx_Oracle

def get_event():
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('hotel','dbdb', dsn)
    cursor = conn.cursor()

    sql = """select event_title, event_start, event_end, event_sale
            from event"""
    cursor.execute(sql)
    row = cursor.fetchall()
    colname = cursor.description

    cursor.close()
    conn.close()


    return row
