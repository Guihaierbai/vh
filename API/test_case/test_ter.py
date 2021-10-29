import time

import allure
import pymysql

from API.DemoApi.baseapi import BaseApi

# 推客-直推3个VIP且团队成员有30个VIP

class TestTer():
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

    @allure.title("直推3个VIP团队成员有30个VIP")
    def test_ter_1(self):
        rootid = self.api.creat_rootid()
        print('rootid=%d' %rootid)
        for i in range(1, 3):
            self.api.establish(i + rootid, rootid, 2)  # 根节点下添加2个VIP成员
        childids = self.api.get_childid(rootid)
        for j in range(11, 38):
            self.api.establish(j + rootid, childids[0], 2)
        self.api.establish(3 + rootid, rootid, 2)
        r = self.api.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 3

    @allure.title("直推3个推客团队成员有30个VIP")
    def test_ter_2(self):
        rootid = self.api.creat_rootid()
        print('rootid=%d' %rootid)
        for i in range(1, 3):
            self.api.establish(i + rootid, rootid, 3)
        childids = self.api.get_childid(rootid)
        for j in range(11, 38):
            self.api.establish(j + rootid, childids[0], 2)
        self.api.establish(3 + rootid, rootid, 3)
        r = self.api.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 3

    @allure.title("直推2个VIP团队成员有30个VIP")
    def test_ter_3(self):
        rootid = self.api.creat_rootid()
        print('rootid=%d' %rootid)
        self.api.establish(1 + rootid, rootid, 2)
        childids = self.api.get_childid(rootid)
        for j in range(11, 38):
            self.api.establish(j + rootid, childids[0], 2)
        self.api.establish(2 + rootid, rootid, 2)
        r = self.api.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 1

    @allure.title("直推3个VIP团队成员有29个VIP")
    def test_ter_4(self):
        rootid = self.api.creat_rootid()
        print('rootid=%d' %rootid)
        for i in range(1, 3):
            self.api.establish(i + rootid, rootid, 2)
        childids = self.api.get_childid(rootid)
        for j in range(11, 36):
            self.api.establish(j + rootid, childids[0], 2)
        self.api.establish(3 + rootid, rootid, 2)
        r = self.api.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 2

    @allure.title("直推3个VIP团队成员有30个普通成员")
    def test_ter_5(self):
        rootid = self.api.creat_rootid()
        print('rootid=%d' %rootid)
        for i in range(1, 3):
            self.api.establish(i + rootid, rootid, 2)
        childids = self.api.get_childid(rootid)
        for j in range(11, 41):
            self.api.establish(j + rootid, childids[0], 1)
        self.api.establish(3 + rootid, rootid, 2)
        r = self.api.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 2