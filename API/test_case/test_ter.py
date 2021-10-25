import time

from API.DemoApi.establish import Establish

# 推客-直推3个VIP且团队成员有30个VIP

class TestTer():
    def setup(self):
        self.establish = Establish()

    # 直推3个VIP团队成员有30个VIP
    def test_ter_1(self):
        id = int(time.time() * 1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        for i in range(1, 3):
            self.establish.establish(i + id, id, 2)  # 根节点下添加2个VIP成员
        childids = self.establish.get_childid(id)
        for j in range(11, 38):
            self.establish.establish(j + id, childids[0], 2)
        self.establish.establish(3 + id, id, 2)
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 3

    # 直推3个推客团队成员有30个VIP
    def test_ter_2(self):
        id = int(time.time() * 1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        for i in range(1, 3):
            self.establish.establish(i + id, id, 3)
        childids = self.establish.get_childid(id)
        for j in range(11, 38):
            self.establish.establish(j + id, childids[0], 2)
        self.establish.establish(3 + id, id, 3)
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 3

    # 直推2个VIP团队成员有30个VIP
    def test_ter_3(self):
        id = int(time.time() * 1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        self.establish.establish(1 + id, id, 2)
        childids = self.establish.get_childid(id)
        for j in range(11, 38):
            self.establish.establish(j + id, childids[0], 2)
        self.establish.establish(2 + id, id, 2)
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 1

    # 直推3个VIP团队成员有29个VIP
    def test_ter_4(self):
        id = int(time.time() * 1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        for i in range(1, 3):
            self.establish.establish(i + id, id, 2)
        childids = self.establish.get_childid(id)
        for j in range(11, 36):
            self.establish.establish(j + id, childids[0], 2)
        self.establish.establish(3 + id, id, 2)
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 2

    # 直推3个VIP团队成员有30个普通成员
    def test_ter_5(self):
        id = int(time.time() * 1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        for i in range(1, 3):
            self.establish.establish(i + id, id, 2)
        childids = self.establish.get_childid(id)
        for j in range(11, 41):
            self.establish.establish(j + id, childids[0], 1)
        self.establish.establish(3 + id, id, 2)
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 2