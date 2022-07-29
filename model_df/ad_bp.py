import pandas as pd
import cx_Oracle

def get_Prod():
    dsn = cx_Oracle.makedsn('localhost',1521, 'xe')
    conn= cx_Oracle.connect('hotel','dbdb',dsn)
    
    cursor= conn.cursor()
    sql = """ select *
            from prod
    """
    cursor.execute(sql)
    
    row= cursor.fetchall()
    colname = cursor.description
    
    cursor.close()
    conn.close()
    
    col=[]
    for i in colname:
        col.append(i[0])
    
    prod= pd.DataFrame(row, columns=col)
    
    return row

def get_Buyer():
    dsn = cx_Oracle.makedsn('localhost',1521, 'xe')
    conn= cx_Oracle.connect('hotel','dbdb',dsn)
    
    cursor= conn.cursor()

    sql = """ select buyer_id, buyer_name, buyer_add, '0'||buyer_tel, nvl(prod_type,'거래 전'), buyer_email, buyer_charger, buyer_bank, buyer_bankno, buyer_bankname 
            from buyer left join prod
                on(buyer_id = prod_buyer)
    """
    cursor.execute(sql)
    
    row= cursor.fetchall()
    colname = cursor.description
    
    cursor.close()
    conn.close()
    
    col=[]
    for i in colname:
        col.append(i[0])
    
    buyer= pd.DataFrame(row, columns=col)
    
    return row
