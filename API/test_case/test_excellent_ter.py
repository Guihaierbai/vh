import time

import pymysql

from API.DemoApi.establish import Establish

# 优秀推客-团队成员有200个VIP，同时满足三条线，每条线有1个推客

class TestExcellentTer():
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

    # 直推3个推客且团队成员有200个VIP
    def test_ex_ter_1(self):
        rootid = self.establish.creat_rootid()
        print('rootid=%d' %rootid)
        for i in range(1, 3):
            self.establish.establish(i + rootid, rootid, 3)
        childids = self.establish.get_childid(rootid)
        for j in range(11, 208):
            child2 = self.establish.establish(j + rootid, childids[0], 2)
            assert child2.json()['errCode'] == 0
        self.establish.establish(3 + rootid, rootid, 3)
        r = self.establish.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 4

    # 直推3个优秀推客且团队成员有200个推客
    def test_ex_ter_2(self):
        rootid = self.establish.creat_rootid()
        print('rootid=%d' %rootid)
        for i in range(1, 4):
            self.establish.establish(i + rootid, rootid, 4)
        childids = self.establish.get_childid(rootid)
        for j in range(11, 207):
            child2 = self.establish.establish(j + rootid, childids[0], 3)
            assert child2.json()['errCode'] == 0
        self.establish.establish(300 + rootid, rootid, 4)
        r = self.establish.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 4

    # 直推2个推客且团队成员有200个VIP
    def test_ex_ter_3(self):
        rootid = self.establish.creat_rootid()
        print('rootid=%d' %rootid)
        for i in range(1, 3):
            self.establish.establish(i + rootid, rootid, 3)
        childids = self.establish.get_childid(rootid)
        for j in range(11, 208):
            child2 = self.establish.establish(j + rootid, childids[0], 2)
            assert child2.json()['errCode'] == 0
        self.establish.establish(300 + rootid, rootid, 2)
        r = self.establish.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 3

    # 直推3个推客且团队成员有199个VIP
    def test_ex_ter_4(self):
        rootid = self.establish.creat_rootid()
        print('rootid=%d' %rootid)
        for i in range(1, 4):
            self.establish.establish(i + rootid, rootid, 3)
        childids = self.establish.get_childid(rootid)
        for j in range(11, 206):
            child2 = self.establish.establish(j + rootid, childids[0], 2)
            assert child2.json()['errCode'] == 0
        self.establish.establish(300 + rootid, rootid, 2)
        r = self.establish.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 3

    # 直推3个推客且团队成员有200个普通人
    def test_ex_ter_5(self):
        rootid = self.establish.creat_rootid()
        print('rootid=%d' %rootid)
        for i in range(1, 4):
            self.establish.establish(i + rootid, rootid, 3)
        childids = self.establish.get_childid(rootid)
        for j in range(11, 208):
            child2 = self.establish.establish(j + rootid, childids[0], 1)
            assert child2.json()['errCode'] == 0
        self.establish.establish(300 + rootid, rootid, 1)
        r = self.establish.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 2

    # 直推200个VIP
    def test_ex_ter_6(self):
        rootid = self.establish.creat_rootid()
        print('rootid=%d' %rootid)
        for j in range(1, 200):
            r = self.establish.establish(j + rootid, rootid, 2)
            assert r.json()['errCode'] == 0
        self.establish.establish(200 + rootid, rootid, 2)
        r = self.establish.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 3

    # 直推200个推客
    def test_ex_ter_7(self):
        rootid = self.establish.creat_rootid()
        print('rootid=%d' %rootid)
        for j in range(1, 200):
            r = self.establish.establish(j + rootid, rootid, 3)
            assert r.json()['errCode'] == 0
        self.establish.establish(200 + rootid, rootid, 3)
        r = self.establish.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 4

    # 直推2个推客,直推1个推客且团队成员有200个VIP
    def test_ex_ter_8(self):
        rootid = self.establish.creat_rootid()
        print('rootid=%d' %rootid)
        for i in range(1, 4):                   # 直推3个VIP
            self.establish.establish(i + rootid, rootid, 2)
        childids = self.establish.get_childid(rootid)
        self.establish.establish(4 + rootid, childids[0], 3)    # 第一个子节点加推客
        self.establish.establish(5 + rootid, childids[1], 3)    # 第二个子节点加推客
        for j in range(11, 207):
            child2 = self.establish.establish(j + rootid, childids[0], 2)
            assert child2.json()['errCode'] == 0
        self.establish.establish(6 + rootid, rootid, 3)     # 直推一个推客触发上级升级
        r = self.establish.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 4