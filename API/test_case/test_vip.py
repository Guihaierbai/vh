import allure
import pymysql

from API.DemoApi.baseapi import BaseApi


# VIP-直推3个好友

class TestVip():
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

    @allure.title("直推3个普通人")
    def test_vip_1(self):
        rootid = self.api.creat_rootid()
        print('rootid=%d' %rootid)
        for i in range(1, 4):
            self.api.establish(i + rootid, rootid, 1)  # 根节点下添加3个普通成员
        r = self.api.groupinfo(rootid)
        # print(json.dumps(r.json(), indent=2))
        assert r.json()['data']['data']['level'] == 2

    @allure.title("直推2个好友")
    def test_vip_2(self):
        rootid = self.api.creat_rootid()
        print('rootid=%d' % rootid)
        for i in range(1, 3):
            self.api.establish(i + rootid, rootid, 1)
        r = self.api.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 1

    @allure.title("直推4个好友")
    def test_vip_3(self):
        rootid = self.api.creat_rootid()
        print('rootid=%d' % rootid)
        for i in range(1, 5):
            self.api.establish(i + rootid, rootid, 1)
        r = self.api.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 2

    @allure.title("直推3个VIP")
    def test_vip_4(self):
        rootid = self.api.creat_rootid()
        print('rootid=%d' % rootid)
        for i in range(1, 4):
            self.api.establish(i + rootid, rootid, 2)
        r = self.api.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 2

    @allure.title("直推3个推客")
    def test_vip_5(self):
        rootid = self.api.creat_rootid()
        print('rootid=%d' % rootid)
        for i in range(1, 4):
            self.api.establish(i + rootid, rootid, 3)
        r = self.api.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 2

    @allure.title("直推3个优秀推客")
    def test_vip_6(self):
        rootid = self.api.creat_rootid()
        print('rootid=%d' % rootid)
        for i in range(1, 4):
            self.api.establish(i + rootid, rootid, 4)
        r = self.api.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 2

    @allure.title("直推3个卓越推客")
    def test_vip_7(self):
        rootid = self.api.creat_rootid()
        print('rootid=%d' % rootid)
        for i in range(1, 4):
            self.api.establish(i + rootid, rootid, 5)
        r = self.api.groupinfo(rootid)
        assert r.json()['data']['data']['level'] == 2
