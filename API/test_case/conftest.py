import pymysql
import pytest

from API.DemoApi.baseapi import BaseApi


@pytest.fixture(scope='function', autouse=False)
def setup():
    establish = BaseApi()
    yield establish
    conn = pymysql.connect(host="47.100.54.254", user="root", password="12345678", database="video-helper",
                           port=40000, charset='utf8')
    cursor = conn.cursor()
    f = open("./rootid.txt")
    rootid = f.read()
    f.close()
    sql = "DELETE FROM group_info where account_id = {} or up_ids like '%{}%'".format(rootid, rootid)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    print("删除")
