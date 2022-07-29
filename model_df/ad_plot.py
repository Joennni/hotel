import pandas as pd
import cx_Oracle

import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
import platform

def get_Plot():
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')
    conn=cx_Oracle.connect('hotel','dbdb',dsn)
    cursor=conn.cursor()
    sql="""select extract(month from res_in) as month, sum(res_kid) as kid
    from reserve
    group by extract(month from res_in)
    order by month
    """
    cursor.execute(sql)

    row=cursor.fetchall()
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[]
    for i in colname:
        col.append(i[0])

    df= pd.DataFrame(row, columns=col)



    if platform.system() == 'Windows':
        path = 'c:/Windows/Fonts/malgun.ttf'
        font_name = font_manager.FontProperties(fname=path).get_name()
        rc('font',family = font_name)

    elif platform.system() == 'Darwin':
        rc('font',family ='AppleGothic')

    else:
        print('Check your OS system')

    plt.figure(figsize=(12,6))
    plt.plot(df['MONTH'], df['KID'])
    plt.title('월별 아이손님의 추이')
    plt.xlabel('month')
    plt.ylabel('kids')
    
    plt.savefig('C:/Users/user/hotel/hotelapp/static/hotelapp/img/plot.png')
    #plt.show()

def monthlycount():
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('hotel', 'dbdb', dsn)
    cursor = conn.cursor()
    
    sql = """select extract(month from res_in) as inDate, sum(res_adult + res_kid + res_baby) as count
        from reserve
        group by extract(month from res_in)
        order by inDate asc"""
    
    cursor.execute(sql)
    row = cursor.fetchall()
    
    colname = cursor.description

    cursor.close()
    conn.close()

    col = []
    for i in colname:
        col.append(i[0])
        
    df = pd.DataFrame(row, columns = col)
    
    plt.rc('font', family = 'Malgun Gothic')
    plt.figure(figsize=(12, 6))
    plt.bar(df['INDATE'], df['COUNT'])
    plt.title('월별 방문객')
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    plt.xlabel('월')
    plt.ylabel('방문객')
    plt.savefig("C:/Users/user/hotel/hotelapp/static/hotelapp/img/monthlycount.png", dpi=300)


def test():
    dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
    conn = cx_Oracle.connect('hotel','dbdb',dsn)
    cursor = conn.cursor()

    sql ="""select mem_add as "고객의 지역",
                sum(res_adult+res_kid +res_baby) as "총 방문객 수"
            from member inner join reserve
                    on(mem_inid = res_mem)
            group by mem_add"""
    cursor.execute(sql)
    row = cursor.fetchall()

    colname = cursor.description

    cursor.close()
    conn.close()

    col = []
    for i in colname:
        col.append(i[0])

    bd = pd.DataFrame(row, columns = col)


    if platform.system() == "Windows":
        path = "c:/Windows/Fonts/malgun.ttf"
        font_name = font_manager.FontProperties(fname=path).get_name()
    elif platform.system() == "Darwin":  
        rc("font", family = "AppleGothic")
    else:
        print("Check your Os system")
        
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    
    plt.rc('font', family = 'Malgun Gothic')
    plt.figure(figsize = (12,6))
    plt.bar(bd["고객의 지역"], bd["총 방문객 수"])
    plt.title("지역별 방문객의 수")
    plt.xlabel("고객의 지역")
    plt.ylabel("총 방문객 수")
    plt.savefig("C:/Users/user/hotel/hotelapp/static/hotelapp/img/local_visit.png")

