import time

from API.DemoApi.establish import Establish

# 卓越推客1-团队成员有2000个VIP，同时满足三条线，每条线不少于300个VIP
# 卓越推客2-团队成员总人数10000人，同时满足三条线，每条线不少于1000人

class TestBrilliantTer():
    def setup(self):
        self.establish = Establish()

    # 团队成员有2000个VIP，同时满足三条线，每条线不少于300个VIP
    def test_bri_ter_1(self):
        id = int(time.time()*1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        i = 1
        while i < 4:
            child = self.establish.establish(i + id, id, 2)  # 根节点下添加3个VIP成员
            assert child.json()['errCode'] == 0
            i += 1
        childids = self.establish.get_childid(id)
        for a in range(4, 303):
            self.establish.establish(a + id, childids[0], 2)
        for b in range(304, 603):
            self.establish.establish(b + id, childids[1], 2)
        for c in range(1000, 2398):
            self.establish.establish(c + id, childids[2], 2)
        self.establish.establish(2399 + id, id, 2)
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 5

    # 团队成员有1999个VIP，同时满足三条线，每条线不少于300个VIP
    def test_bri_ter_2(self):
        id = int(time.time()*1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        i = 1
        while i < 4:
            child = self.establish.establish(i + id, id, 2)  # 根节点下添加3个VIP成员
            assert child.json()['errCode'] == 0
            i += 1
        childids = self.establish.get_childid(id)
        for a in range(4, 303):
            self.establish.establish(a + id, childids[0], 2)
        for b in range(304, 603):
            self.establish.establish(b + id, childids[1], 2)
        for c in range(1000, 2398):
            self.establish.establish(c + id, childids[2], 2)
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 5

    # 团队成员有2000个VIP，同时满足两条线，每条线不少于300个VIP
    def test_bri_ter_3(self):
        id = int(time.time()*1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        i = 1
        while i < 4:
            child = self.establish.establish(i + id, id, 2)  # 根节点下添加3个VIP成员
            assert child.json()['errCode'] == 0
            i += 1
        childids = self.establish.get_childid(id)
        for a in range(4, 303):
            self.establish.establish(a + id, childids[0], 2)
        for c in range(801, 2399):
            self.establish.establish(c + id, childids[2], 2)
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 5