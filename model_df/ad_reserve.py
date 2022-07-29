import pandas as pd
import cx_Oracle

def ad_Reserve():
    dsn= cx_Oracle.makedsn('localhost',1521,'xe')
    conn= cx_Oracle.connect('hotel','dbdb',dsn)
    cursor=conn.cursor()
    
    sql=""" select res_id, mem_name, mem_email, mem_tel, rmnum_id, room_type, res_adult, res_kid, res_baby, res_in, res_out, res_date, res_price 
    from reserve inner join member
    on (res_mem = mem_inid)
    inner join rmnum
    on (res_rmnum = rmnum_id)
    inner join room
    on (room_id = rmnum_room)
    order by res_in desc
    """
    cursor.execute(sql)
    
    row= cursor.fetchall()
    colname= cursor.description
    
    cursor.close()
    conn.close()
    
    col=[]
    for i in colname:
        col.append(i[0])
        
    re = pd.DataFrame(row, columns=col)
    return row

def ad_Search(type, in_date = '0', out_date = '0', rmnum = '0'):
    dsn= cx_Oracle.makedsn('localhost',1521,'xe')
    conn= cx_Oracle.connect('hotel','dbdb',dsn)
    cursor=conn.cursor()
    
    sql="""select res_id, mem_name, mem_email, mem_tel, rmnum_id, room_type, res_adult, res_kid, res_baby, res_in, res_out, res_date, res_price 
    from reserve inner join member
    on (res_mem = mem_inid)
    inner join rmnum
    on (res_rmnum = rmnum_id)
    inner join room
    on (room_id = rmnum_room)
    where
    """
    if type == 1:
        sql += "res_in >= '"
        sql += in_date
        sql += "' and res_in <= '"
        sql += out_date
    elif type == 2:
        sql += "rmnum = "
        sql += rmnum
    
    sql += "' order by res_in desc"
    
    cursor.execute(sql)
    
    row = cursor.fetchall()
    return row