import json
import time

from API.DemoApi.establish import Establish

# VIP-直推3个好友123

class TestVip():
    def setup(self):
        self.establish = Establish()

    # 直推3个普通人
    def test_vip_1(self):
        id = int(time.time() * 1000)
        print("rootid=%d" % id)
        r = self.establish.establish(id, None, 1)  # 建立根节点
        # print(json.dumps(r.json(), indent=2))
        for i in range(1, 4):
            self.establish.establish(i + id, id, 1)  # 根节点下添加3个普通成员
        r = self.establish.groupinfo(id)
        # print(json.dumps(r.json(), indent=2))
        assert r.json()['data']['data']['level'] == 2

    # 直推2个好友
    def test_vip_2(self):
        id = int(time.time() * 1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        for i in range(1, 3):
            self.establish.establish(i + id, id, 1)
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 1

    # 直推4个好友
    def test_vip_3(self):
        id = int(time.time() * 1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        for i in range(1, 5):
            self.establish.establish(i + id, id, 1)
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 2

    # 直推3个VIP
    def test_vip_4(self):
        id = int(time.time() * 1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        for i in range(1, 4):
            self.establish.establish(i + id, id, 2)
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 2

    # 直推3个推客
    def test_vip_5(self):
        id = int(time.time() * 1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        for i in range(1, 4):
            self.establish.establish(i + id, id, 3)
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 2

    # 直推3个优秀推客
    def test_vip_6(self):
        id = int(time.time() * 1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        for i in range(1, 4):
            self.establish.establish(i + id, id, 4)
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 2

    # 直推3个卓越推客
    def test_vip_7(self):
        id = int(time.time() * 1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        for i in range(1, 4):
            self.establish.establish(i + id, id, 5)
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 2
