import pandas as pd
import cx_Oracle

def ad_room():
       dsn = cx_Oracle.makedsn('localhost',1521,'xe')
       conn = cx_Oracle.connect('hotel','dbdb',dsn)
       cursor = conn.cursor()
       sql="""select room_id as "순서",
                     room_nm as "객실명",
                     room_count as "기준 인원수",
                     room_count + 1 as "최대 인원수",
                     to_char(room_sale, '999,999') as "1박 가격"
              from room
       """
       cursor.execute(sql)

       row = cursor.fetchall()
       colname = cursor.description


       cursor.close()
       conn.close()
       
       col = []
       for i in colname:
              col.append(i[0])

       adr = pd.DataFrame(row, columns = col)
       
       return row




