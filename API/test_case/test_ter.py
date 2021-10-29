import time

import pymysql

from API.DemoApi.establish import Establish

# 推客-直推3个VIP且团队成员有30个VIP

class TestTer():
    def setup(self):
        self.establish = Establish()

    def teardown_method(self):
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

    # 直推3个VIP团队成员有30个VIP
    def test_ter_1(self):
        rootid = self.establish.creat_rootid()
        print('rootid=%d' %rootid)
        for i in range(1, 3):
            self.establish.establish(i + rootid, rootid, 2)  # 根节点下添加2个VIP成员
        childids = self.establish.get_childid(rootid)
        for j in range(11, 38):
            self.establish.establish(j + rootid, childids[0], 2)
        self.establish.establish(3 + rootid, rootid, 2)
        r = self.establish.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 3

    # 直推3个推客团队成员有30个VIP
    def test_ter_2(self):
        rootid = self.establish.creat_rootid()
        print('rootid=%d' %rootid)
        for i in range(1, 3):
            self.establish.establish(i + rootid, rootid, 3)
        childids = self.establish.get_childid(rootid)
        for j in range(11, 38):
            self.establish.establish(j + rootid, childids[0], 2)
        self.establish.establish(3 + rootid, rootid, 3)
        r = self.establish.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 3

    # 直推2个VIP团队成员有30个VIP
    def test_ter_3(self):
        rootid = self.establish.creat_rootid()
        print('rootid=%d' %rootid)
        self.establish.establish(1 + rootid, rootid, 2)
        childids = self.establish.get_childid(rootid)
        for j in range(11, 38):
            self.establish.establish(j + rootid, childids[0], 2)
        self.establish.establish(2 + rootid, rootid, 2)
        r = self.establish.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 1

    # 直推3个VIP团队成员有29个VIP
    def test_ter_4(self):
        rootid = self.establish.creat_rootid()
        print('rootid=%d' %rootid)
        for i in range(1, 3):
            self.establish.establish(i + rootid, rootid, 2)
        childids = self.establish.get_childid(rootid)
        for j in range(11, 36):
            self.establish.establish(j + rootid, childids[0], 2)
        self.establish.establish(3 + rootid, rootid, 2)
        r = self.establish.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 2

    # 直推3个VIP团队成员有30个普通成员
    def test_ter_5(self):
        rootid = self.establish.creat_rootid()
        print('rootid=%d' %rootid)
        for i in range(1, 3):
            self.establish.establish(i + rootid, rootid, 2)
        childids = self.establish.get_childid(rootid)
        for j in range(11, 41):
            self.establish.establish(j + rootid, childids[0], 1)
        self.establish.establish(3 + rootid, rootid, 2)
        r = self.establish.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 2