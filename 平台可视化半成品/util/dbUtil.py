import pymysql

connection_info = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'weiming'
}

def get_conn():
    conn=pymysql.connect(**connection_info)
    return conn
