import time

import pymysql

from API.DemoApi.establish import Establish

# 卓越推客1-团队成员有2000个VIP，同时满足三条线，每条线不少于300个VIP
# 卓越推客2-团队成员总人数10000人，同时满足三条线，每条线不少于1000人

class TestBrilliantTer():
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

    # 团队成员有2000个VIP，同时满足三条线，每条线不少于300个VIP
    def test_bri_ter_1(self):
        rootid = self.establish.creat_rootid()
        print('rootid=%d' %rootid)
        i = 1
        while i < 4:
            child = self.establish.establish(i + rootid, rootid, 2)  # 根节点下添加3个VIP成员
            assert child.json()['errCode'] == 0
            i += 1
        childids = self.establish.get_childid(rootid)
        for a in range(4, 303):
            self.establish.establish(a + rootid, childids[0], 2)
        for b in range(304, 603):
            self.establish.establish(b + rootid, childids[1], 2)
        for c in range(1000, 2398):
            self.establish.establish(c + rootid, childids[2], 2)
        self.establish.establish(2399 + rootid, rootid, 2)
        r = self.establish.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 5

    # 团队成员有1999个VIP，同时满足三条线，每条线不少于300个VIP
    def test_bri_ter_2(self):
        rootid = self.establish.creat_rootid()
        print('rootid=%d' %rootid)
        i = 1
        while i < 4:
            child = self.establish.establish(i + rootid, rootid, 2)  # 根节点下添加3个VIP成员
            assert child.json()['errCode'] == 0
            i += 1
        childids = self.establish.get_childid(rootid)
        for a in range(4, 303):
            self.establish.establish(a + rootid, childids[0], 2)
        for b in range(304, 603):
            self.establish.establish(b + rootid, childids[1], 2)
        for c in range(1000, 2398):
            self.establish.establish(c + rootid, childids[2], 2)
        r = self.establish.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 5

    # 团队成员有2000个VIP，同时满足两条线，每条线不少于300个VIP
    def test_bri_ter_3(self):
        rootid = self.establish.creat_rootid()
        print('rootid=%d' %rootid)
        i = 1
        while i < 4:
            child = self.establish.establish(i + rootid, rootid, 2)  # 根节点下添加3个VIP成员
            assert child.json()['errCode'] == 0
            i += 1
        childids = self.establish.get_childid(rootid)
        for a in range(4, 303):
            self.establish.establish(a + rootid, childids[0], 2)
        for c in range(801, 2399):
            self.establish.establish(c + rootid, childids[2], 2)
        r = self.establish.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 5