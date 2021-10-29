import json
import time

from API.DemoApi.establish import Establish

'''
各级别升级条件：
VIP-直推3个好友
推客-直推3个VIP且团队成员有30个VIP
优秀推客-直推3个推客且团队成员有200个VIP
卓越推客1-团队成员有2000个VIP，同时满足三条线，每条线不少于300个VIP
卓越推客2-团队成员总人数10000人，同时满足三条线，每条线不少于1000人
'''

class TestEstablish():
    def setup(self):
        self.establish = Establish()

    def test_vip(self):
        id = int(time.time()*1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        for i in range(1, 4):
            self.establish.establish(i + id, id, 2)  # 根节点下添加3个普通成员
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 2

    def test_talent(self):
        id = int(time.time()*1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        for i in range(1, 4):
            self.establish.establish(i + id, id, 2)  # 根节点下添加3个VIP成员
        childids = self.establish.get_childid(id)
        for j in range(11, 38):
            self.establish.establish(j + id, childids[0], 2)
        r = self.establish.groupinfo(id)
        # assert r.json()['data']['data']['level'] == 3

    def test_ter(self):
        id = int(time.time()*1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        for i in range(1, 4):
            self.establish.establish(i + id, id, 4)  # 根节点下添加3个推客成员
        childids = self.establish.get_childid(id)
        for j in range(11, 208):
            child2 = self.establish.establish(j + id, childids[0], 3)
            assert child2.json()['errCode'] == 0
        r = self.establish.groupinfo(id)
        assert r.json()['data']['data']['level'] == 4

    def test_org1(self):  # 2000VIP且3个直推团队每个团队至少有300个VIP
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
        for c in range(1000, 2399):
            self.establish.establish(c + id, childids[2], 2)
        # r = self.establish.groupinfo(id)
        # assert r.json()['data']['data']['level'] == 5

    def test_org2(self):  # 团队成员10000人且3个直推团队每个团队至少1000人
        id = int(time.time()*1000)
        print("rootid=%d" % id)
        self.establish.establish(id, None, 1)  # 建立根节点
        i = 1
        while i < 4:
            child = self.establish.establish(i + id, id, 2)  # 根节点下添加3个VIP成员
            assert child.json()['errCode'] == 0
            i += 1
        childids = self.establish.get_childid(id)
        for a in range(1, 1000):
            self.establish.establish(a + id, childids[0], 1)
        for b in range(1000, 1999):
            self.establish.establish(b + id, childids[1], 2)
        for c in range(2000, 9999):
            self.establish.establish(c + id, childids[2], 3)

    # def test_1(self):
    #     rootid = int('111' + str(int(time.time())))
    #     self.establish.establish(rootid, None, 1)  # 建立根节点
    #     i = 1
    #     while i < 4:
    #         k = i + int(time.time())
    #         child = self.establish.establish(k, rootid, 2)  # 根节点下添加3个VIP成员
    #         assert child.json()['errCode'] == 0
    #         i += 1
    #     r = requests.get('https://api-qa.meiyike.club/video-helper/group-info/groupInfo',
    #                      params={'rootId': rootid})
    #     # print(json.dumps(r.json(), indent=2))
    #     childid = []
    #     children_data = r.json()['data']['children']
    #     for k in children_data:
    #         if k['data']['id'] != []:
    #             childid.append(k['data']['id'])  # 获取3个直推好友ID
    #     print("rootid=%d" %rootid)
    #     print("\n")
    #     print("childid=%s" %childid)
    #
    def test_add(self):
        id = int(time.time())
        print(id)
        # r = self.establish.establish(id, 1728884171180800, 2)
        # print(json.dumps(r.json(), indent=2))
        # assert r.json()['errCode'] == 0
        for i in range(1, 30):
            r = self.establish.establish(i + id, 1728884171180800, 2)  # 根节点下添加3个普通成员
            assert r.json()['errCode'] == 0
            print(json.dumps(r.json(), indent=2))
        # childids = self.establish.get_childid(id)
        # print(childids)

    def test_add2(self):  # 循环添加30层
        id = int(time.time())
        print("id=%d" % id)
        r = self.establish.establish(id, 1634886718075, 1)
        # print(json.dumps(r.json(), indent=2))
        # for i in range(1, 30):
        #     parentid = r.json()['data']['accountId']
        #     # print("parentid=%d" % parentid)
        #     r = self.establish.establish(id + i, parentid, 1)
        #     # print(json.dumps(r.json(), indent=2))
        r = self.establish.groupinfo(1634886718075)
        assert r.json()['data']['data']['level'] == 5


