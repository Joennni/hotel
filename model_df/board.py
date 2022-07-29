import pandas as pd
import cx_Oracle

def board():
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('hotel','dbdb', dsn)
    cursor = conn.cursor()

    sql = """select post_id as "번호", 
                    decode(post_type,
                            1, '문의글',
                            0, '후기글') as "구분", 
                    post_title as "제목", 
                    mem_id as "글쓴이", 
                    post_date as "작성일", 
                    post_count as "조회수"
                    from post inner join member
                        on(mem_inid = post_mem)
            order by post_id desc"""
    cursor.execute(sql)
    row = cursor.fetchall()

    cursor.close()
    conn.close()

    return row


def get_Event():
    dsn= cx_Oracle.makedsn('localhost',1521,'xe')
    conn= cx_Oracle.connect('hotel','dbdb',dsn)
    cursor=conn.cursor()
    
    sql=""" select event_title, event_cont, event_start, event_end
        from event
        """
    cursor.execute(sql)
    
    row= cursor.fetchall()
    colname= cursor.description
    
    cursor.close()
    conn.close()
    
    col=[]
    for i in colname:
        col.append(i[0])
        
    df = pd.DataFrame(row, columns=col)
    return row





def bdw(post_mem, post_title, post_cont, post_date, post_hide):
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('hotel', 'dbdb', dsn)
    cursor = conn.cursor()
    
    sql = """insert into post (post_mem, post_room, post_title, post_cont, post_hide, post_date, post_count, post_type) values ('"""
    sql += post_mem
    sql += "','"
    sql += '1'
    sql += "','"
    sql += post_title
    sql += "','"
    sql += post_cont
    sql += "','"
    sql += str(post_hide)
    sql += "','"
    sql += str(post_date)
    sql += "','"
    sql += '1'
    sql += "','"
    sql += '1'
    sql += "')"
    cursor.execute(sql)
    conn.commit()
    
    cursor.close()
    conn.close()
     