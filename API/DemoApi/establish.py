import time

import requests


class Establish():

    # 用户关系建立
    def establish(self, id, upid, level):
        header = {'appId': 'vh', 'appVersion': '1.0.0'}
        r = requests.get('http://api-qa.ketui.cn/video-helper/group-info/establish',
                         params={'id': id, 'upId': upid, 'level': level},
                         headers=header
                         )
        return r

    # 查询用户关系
    def groupinfo(self, rootid):
        header = {'appId': 'vh', 'appVersion': '1.0.0'}
        r = requests.get('http://api-qa.ketui.cn/video-helper/group-info/groupInfo',
                         params={'rootId': rootid},
                         headers=header
                         )
        return r

    # 获取直推好友ID
    def get_childid(self, rootid):
        r = self.groupinfo(rootid)
        childid = []
        child_data = r.json()['data']['children']
        for child in child_data:
            if child['data']['id'] != []:
                childid.append(child['data']['id'])  # 获取3个直推好友ID
        return childid

    # 建立根节点
    def creat_rootid(self):
        rootid = int(time.time() * 1000)
        self.establish(rootid, None, 1)  # 建立根节点
        f = open('rootid.txt', 'w')
        f.truncate(0)
        f.write(str(rootid))
        f.close()
        return rootid
