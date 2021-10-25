import time

from API.DemoApi.establish import Establish

# 优秀推客-团队成员有200个VIP，同时满足三条线，每条线有1个推客

class TestExcellentTer():
    def setup(self):
        self.establish = Establish()

    # 直推3个推客且团队成员有200个VIP
    def test_ex_ter_1(self):
        id = int(time.time() * 1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        for i in range(1, 3):
            self.establish.establish(i + id, id, 3)
        childids = self.establish.get_childid(id)
        for j in range(11, 208):
            child2 = self.establish.establish(j + id, childids[0], 2)
            assert child2.json()['errCode'] == 0
        self.establish.establish(3 + id, id, 3)
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 4

    # 直推3个优秀推客且团队成员有200个推客
    def test_ex_ter_2(self):
        id = int(time.time() * 1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        for i in range(1, 4):
            self.establish.establish(i + id, id, 4)
        childids = self.establish.get_childid(id)
        for j in range(11, 207):
            child2 = self.establish.establish(j + id, childids[0], 3)
            assert child2.json()['errCode'] == 0
        self.establish.establish(300 + id, id, 4)
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 4

    # 直推2个推客且团队成员有200个VIP
    def test_ex_ter_3(self):
        id = int(time.time() * 1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        for i in range(1, 3):
            self.establish.establish(i + id, id, 3)
        childids = self.establish.get_childid(id)
        for j in range(11, 208):
            child2 = self.establish.establish(j + id, childids[0], 2)
            assert child2.json()['errCode'] == 0
        self.establish.establish(300 + id, id, 2)
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 3

    # 直推3个推客且团队成员有199个VIP
    def test_ex_ter_4(self):
        id = int(time.time() * 1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        for i in range(1, 4):
            self.establish.establish(i + id, id, 3)
        childids = self.establish.get_childid(id)
        for j in range(11, 206):
            child2 = self.establish.establish(j + id, childids[0], 2)
            assert child2.json()['errCode'] == 0
        self.establish.establish(300 + id, id, 2)
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 3

    # 直推3个推客且团队成员有200个普通人
    def test_ex_ter_5(self):
        id = int(time.time() * 1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        for i in range(1, 4):
            self.establish.establish(i + id, id, 3)
        childids = self.establish.get_childid(id)
        for j in range(11, 208):
            child2 = self.establish.establish(j + id, childids[0], 1)
            assert child2.json()['errCode'] == 0
        self.establish.establish(300 + id, id, 1)
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 2

    # 直推200个VIP
    def test_ex_ter_6(self):
        id = int(time.time() * 1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        for j in range(1, 200):
            r = self.establish.establish(j + id, id, 2)
            assert r.json()['errCode'] == 0
        self.establish.establish(200 + id, id, 2)
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 3

    # 直推200个推客
    def test_ex_ter_7(self):
        id = int(time.time() * 1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        for j in range(1, 200):
            r = self.establish.establish(j + id, id, 3)
            assert r.json()['errCode'] == 0
        self.establish.establish(200 + id, id, 3)
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 4

    # 直推2个推客,直推1个推客且团队成员有200个VIP
    def test_ex_ter_8(self):
        id = int(time.time() * 1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)   # 建立根节点
        for i in range(1, 4):                   # 直推3个VIP
            self.establish.establish(i + id, id, 2)
        childids = self.establish.get_childid(id)
        self.establish.establish(4 + id, childids[0], 3)    # 第一个子节点加推客
        self.establish.establish(5 + id, childids[1], 3)    # 第二个子节点加推客
        for j in range(11, 207):
            child2 = self.establish.establish(j + id, childids[0], 2)
            assert child2.json()['errCode'] == 0
        self.establish.establish(6 + id, id, 3)     # 直推一个推客触发上级升级
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 4