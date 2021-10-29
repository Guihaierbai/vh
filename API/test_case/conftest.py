import pymysql
import pytest


@pytest.fixture(scope='class')
def connDB():
    conn = pymysql.connect(host="47.100.54.254", user="root", password="12345678", database="video-helper",
                           port=40000, charset='utf8')
    cursor = conn.cursor()
    return cursor
