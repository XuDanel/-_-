from util.dbUtil import get_conn
import pymysql
connection_info = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'weiming'
}
update_query = "UPDATE student_assignment SET grade = 0, comment ='Great work.' WHERE student_assignment_id = 41"
conn=pymysql.connect(**connection_info)
cur = conn.cursor()
cur.execute(update_query)
conn.commit()
conn.close()
