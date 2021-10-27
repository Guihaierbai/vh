import pymssql
import pymysql


def test_DB():
    # host = "47.100.54.254"
    # user = "root"
    # password = "12345678"
    # database = "video-helper"
    # port = 40000
    # charset = 'utf8'
    #
    # # conn = pymssql.connect(host, user, password, database, port, charset)
    conn = pymysql.connect(host="47.100.54.254", user="root", password="12345678", database="video-helper",
                           port=40000, charset='utf8')
    cursor = conn.cursor()
    # cursor.execute("SELECT account_id FROM group_info")
    # data = cursor.fetchall()
    # for row in data:
    #     print(row)
    cursor.execute("DELETE FROM group_info where account_id = {}".format(1635322324985))