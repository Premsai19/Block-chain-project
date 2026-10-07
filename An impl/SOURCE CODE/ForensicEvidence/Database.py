import pymysql

def connection():
    con=pymysql.connect(host='localhost',user='root',password='root',database='forensic_evidence', charset='utf8')
    return con

