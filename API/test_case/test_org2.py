import time

import pytest
import requests

from API.DemoApi.establish import Establish
ROOTID = 1727527134391040
CHILDID = [1759305684175104, 1759305984116992]
ID = int(time.time()*100000)

class TestOrg1():
    def setup(self):
        self.establish = Establish()

    def test_1(self):
        for i in range(500):
            self.establish.establish(i+ID, CHILDID[0], 1)
            # print(i+ID)

    def test_2(self):
        for i in range(500, 999):
            self.establish.establish(i+ID, CHILDID[0], 1)
            # print(i + ID)

    def test_3(self):
        for i in range(1000, 1500):
            self.establish.establish(i+ID, CHILDID[1], 1)
            # print(i + ID)

    def test_4(self):
        for i in range(1500, 1999):
            self.establish.establish(i+ID, CHILDID[1], 1)
            # print(i + ID)

    def test_k1(self):
        for i in range(2000, 2500):
            self.establish.establish(i+ID, CHILDID[1], 1)

    def test_k2(self):
        for i in range(2500, 3000):
            self.establish.establish(i+ID, CHILDID[1], 1)

    def test_k3(self):
        for i in range(3000, 3500):
            self.establish.establish(i+ID, CHILDID[1], 1)

    def test_k4(self):
        for i in range(3500, 4000):
            self.establish.establish(i+ID, CHILDID[1], 1)

    def test_k5(self):
        for i in range(4000, 4500):
            self.establish.establish(i+ID, CHILDID[1], 1)

    def test_k6(self):
        for i in range(4500, 5000):
            self.establish.establish(i+ID, CHILDID[1], 1)

    def test_k7(self):
        for i in range(5000, 5500):
            self.establish.establish(i+ID, CHILDID[1], 1)

    def test_k8(self):
        for i in range(5500, 6000):
            self.establish.establish(i+ID, CHILDID[1], 1)

    def test_k9(self):
        for i in range(6000, 6500):
            self.establish.establish(i+ID, CHILDID[1], 1)

    def test_k10(self):
        for i in range(6500, 7000):
            self.establish.establish(i+ID, CHILDID[1], 1)

    def test_k11(self):
        for i in range(7000, 7500):
            self.establish.establish(i+ID, CHILDID[1], 1)

    def test_k12(self):
        for i in range(7500, 8000):
            self.establish.establish(i+ID, CHILDID[1], 1)

    def test_k13(self):
        for i in range(8000, 8500):
            self.establish.establish(i+ID, CHILDID[1], 1)

    def test_k14(self):
        for i in range(8500, 9000):
            self.establish.establish(i+ID, CHILDID[1], 1)

    def test_k15(self):
        for i in range(9000, 9500):
            self.establish.establish(i+ID, CHILDID[1], 1)

    def test_k16(self):
        for i in range(9500, 9999):
            self.establish.establish(i+ID, CHILDID[1], 1)

    if __name__ == "__main__":
        pytest.main(["-s", "test_org1.py", '--workers=auto', '--tests-per-worker=auto'])