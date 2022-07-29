import email
import telnetlib
from unicodedata import name
from matplotlib.colors import TwoSlopeNorm
import pandas as pd
import cx_Oracle

def getReserve_list(mem, rmnum, c_in, c_out, adult, kid, baby, name, email, tel, cardno, cardpw):
    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')
    conn = cx_Oracle.connect('hotel','dbdb',dsn)
    cursor = conn.cursor()

    sql=""" insert into reserve(res_mem, res_rmnum, res_in, res_out, res_date, res_price, res_adult, res_kid, res_baby)
            values ('
    """
    sql+= mem
    sql+="','"
    sql+= rmnum
    sql+="','"
    sql+= str(c_in)
    sql+="','"
    sql+= str(c_out)
    sql+="','"
    sql+= '20220509'
    sql+="','"
    sql+= '510000'
    sql+="','"
    sql+= adult
    sql+="','"
    sql+= kid
    sql+="','"
    sql+= baby
    sql+="')"
    cursor.execute(sql)
    conn.commit()

    sql="""update member set mem_name = '"""
    sql += name
    sql += "', mem_email ='"
    sql += email
    sql += "', mem_tel ='"
    sql += tel
    sql += "', mem_cardno ='"
    sql += cardno
    sql += "', mem_cdpw = '"
    sql += cardpw
    sql += "'where mem_inid ='"
    sql += str(mem)
    sql += "'"
    cursor.execute(sql)
    conn.commit()
    
    sql="""select res_rmnum, rmnum_about, res_in, res_out, (res_adult + res_kid + res_baby)as 총인원수, mem_name
            from reserve inner join rmnum
                on (res_rmnum = rmnum_id)
                inner join room
                on (room_id = rmnum_room)
                inner join member
                on (mem_inid = res_mem) 
                where res_mem = '"""
    sql+= str(mem)
    sql+="'"

    cursor.execute(sql)

    row = cursor.fetchall()
    colname = cursor.description
    
    cursor.close()
    conn.close()
    
    col=[]
    for i in colname:
        col.append(i[0])

    df = pd.DataFrame(row, columns=col)
    return row


def getReserve_info1(mem):
    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')
    conn = cx_Oracle.connect('hotel','dbdb',dsn)
    cursor = conn.cursor()
    sql= """select res_rmnum, rmnum_about, res_in, res_out, (res_adult + res_kid + res_baby)as 총인원수, mem_name
            from reserve inner join rmnum
                on (res_rmnum = rmnum_id)
                inner join room
                on (room_id = rmnum_room)
                inner join member
                on (mem_inid = res_mem) 
                where res_mem = '"""
    sql+= str(mem)
    sql+="'"
    cursor.execute(sql)


    row = cursor.fetchall()


    colname = cursor.description



    cursor.close()


    conn.close()



    col=[]
    for i in colname:
        col.append(i[0])


    df1 = pd.DataFrame(row, columns=col)

    return row

# def getReserve_info2():
    
#     dsn=cx_Oracle.makedsn('localhost',1521,'xe')


#     conn = cx_Oracle.connect('hotel','dbdb',dsn)


#     cursor = conn.cursor()


#     sql= """select mem_id, mem_name, res_in, res_out, room_nm, rmnum_id
#             from reserve inner join rmnum
#                 on (res_rmnum = rmnum_id)
#                 inner join room
#                 on (room_id = rmnum_room)
#                 inner join member
#                 on (res_mem = mem_inid)
#             where extract(year from res_in)= 2022
#     """
#     cursor.execute(sql)


#     row = cursor.fetchall()


#     colname = cursor.description



#     cursor.close()


#     conn.close()



#     col=[]
#     for i in colname:
#         col.append(i[0])


#     df2 = pd.DataFrame(row, columns=col)

#     return row