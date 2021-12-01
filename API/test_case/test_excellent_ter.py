import allure
import pymysql
from API.DemoApi.baseapi import BaseApi

# 优秀推客-团队成员有200个VIP，同时满足三条线，每条线有30个VIP

class TestExcellentTer():
    def setup(self):
        self.api = BaseApi()

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

    @allure.title("3条线每条线30个VIP且团队成员有200个VIP")
    def test_ex_ter_1(self):
        rootid = self.api.creat_rootid()
        print('rootid=%d' %rootid)
        for i in range(1, 4):
            self.api.establish(i + rootid, rootid, 2)
        childids = self.api.get_childid(rootid)
        for j in range(11, 40):
            self.api.establish(j + rootid, childids[0], 2)
        for k in range(41, 70):
            self.api.establish(k + rootid, childids[1], 2)
        for l in range(71, 209):
            self.api.establish(l + rootid, childids[2], 2)
        self.api.establish(4 + rootid, rootid, 2)
        r = self.api.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 4

    @allure.title("3条线每条线30个推客且团队成员有200个推客")
    def test_ex_ter_2(self):
        rootid = self.api.creat_rootid()
        print('rootid=%d' % rootid)
        for i in range(1, 4):
            self.api.establish(i + rootid, rootid, 3)
        childids = self.api.get_childid(rootid)
        for j in range(11, 40):
            self.api.establish(j + rootid, childids[0], 3)
        for k in range(41, 70):
            self.api.establish(k + rootid, childids[1], 3)
        for l in range(71, 209):
            self.api.establish(l + rootid, childids[2], 3)
        self.api.establish(4 + rootid, rootid, 3)
        r = self.api.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 4

    @allure.title("2条线每条线30个VIP且团队成员有200个VIP")
    def test_ex_ter_3(self):
        rootid = self.api.creat_rootid()
        print('rootid=%d' % rootid)
        for i in range(1, 4):
            self.api.establish(i + rootid, rootid, 2)
        childids = self.api.get_childid(rootid)
        for j in range(11, 39):
            self.api.establish(j + rootid, childids[0], 2)
        for k in range(41, 70):
            self.api.establish(k + rootid, childids[1], 2)
        for l in range(71, 210):
            self.api.establish(l + rootid, childids[2], 2)
        self.api.establish(4 + rootid, rootid, 2)
        r = self.api.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 3

    @allure.title("3条线每条线30个VIP且团队成员有199个VIP")
    def test_ex_ter_4(self):
        rootid = self.api.creat_rootid()
        print('rootid=%d' % rootid)
        for i in range(1, 4):
            self.api.establish(i + rootid, rootid, 2)
        childids = self.api.get_childid(rootid)
        for j in range(11, 40):
            self.api.establish(j + rootid, childids[0], 2)
        for k in range(41, 70):
            self.api.establish(k + rootid, childids[1], 2)
        for l in range(71, 208):
            self.api.establish(l + rootid, childids[2], 2)
        self.api.establish(4 + rootid, rootid, 2)
        r = self.api.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 3

    @allure.title("3条线每条线30个普通人且团队成员有200个普通人")
    def test_ex_ter_5(self):
        rootid = self.api.creat_rootid()
        print('rootid=%d' % rootid)
        for i in range(1, 4):
            self.api.establish(i + rootid, rootid, 1)
        childids = self.api.get_childid(rootid)
        for j in range(11, 40):
            self.api.establish(j + rootid, childids[0], 1)
        for k in range(41, 70):
            self.api.establish(k + rootid, childids[1], 1)
        for l in range(71, 209):
            self.api.establish(l + rootid, childids[2], 1)
        self.api.establish(4 + rootid, rootid, 1)
        r = self.api.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 2

    @allure.title("直推200个VIP")
    # 直推200个VIP
    def test_ex_ter_6(self):
        rootid = self.api.creat_rootid()
        print('rootid=%d' %rootid)
        for j in range(1, 200):
            r = self.api.establish(j + rootid, rootid, 2)
            assert r.json()['errCode'] == 0
        self.api.establish(200 + rootid, rootid, 2)
        r = self.api.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 3

    @allure.title("直推200个推客")
    def test_ex_ter_7(self):
        rootid = self.api.creat_rootid()
        print('rootid=%d' %rootid)
        for j in range(1, 200):
            r = self.api.establish(j + rootid, rootid, 3)
            assert r.json()['errCode'] == 0
        self.api.establish(200 + rootid, rootid, 3)
        r = self.api.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 3
