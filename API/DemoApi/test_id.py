import time

import pytest
import requests

from API.DemoApi.establish import Establish
ROOTID = 1111628476297
CHILDID = [1628476298, 1628476300, 1628476301]
ID = int(time.time()*100000)

class TestOrg1():
    def setup(self):
        self.establish = Establish()

    def test_1(self):
        file = open('1.txt', 'w')
        for i in range(500):
            r = self.establish.establish(i+ID, CHILDID[0], 1)
            assert r.json()['errCode'] == 0
            file.write(str(i+ID))
            file.write('\r\n')
        file.close()

    def test_2(self):
        file = open('2.txt', 'w')
        for i in range(500, 999):
            r = self.establish.establish(i+ID, CHILDID[0], 1)
            assert r.json()['errCode'] == 0
            file.write(str(i + ID))
            file.write('\r\n')
        file.close()

    def test_3(self):
        file = open('3.txt', 'w')
        for i in range(1000, 1500):
            r = self.establish.establish(i+ID, CHILDID[1], 1)
            assert r.json()['errCode'] == 0
            # print(i + ID)
            file.write(str(i + ID))
            file.write('\r\n')
        file.close()

    def test_4(self):
        file = open('4.txt', 'w')
        for i in range(1500, 1999):
            r = self.establish.establish(i+ID, CHILDID[1], 1)
            assert r.json()['errCode'] == 0
            # print(i + ID)
            file.write(str(i + ID))
            file.write('\r\n')
        file.close()

    if __name__ == "__main__":
        pytest.main(["-s", "test_org1.py", '--workers=auto', '--tests-per-worker=auto'])