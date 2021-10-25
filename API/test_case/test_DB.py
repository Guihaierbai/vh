import pymssql
import pymysql


def test_DB():

    host = "47.100.54.254"
    user = "root"
    password = "12345678"
    database = "video-helper"
    port = 40000
    charset = 'utf8'

    conn = pymysql.connect(host="47.100.54.254", user="root", password="12345678", database="video-helper",
                           port=40000, charset='utf8')
    cursor = conn.cursor()
    cursor.execute("Select * From 'group_info'")
    data = cursor.fetchall()
    for row in data:
        print(row)