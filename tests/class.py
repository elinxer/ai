

import tests.libs.TestClass as tc

"""
Python类使用方式说明

"""

res = tc.TestInit('Elinx', 22, 140)

print(res.speak())


s = tc.student('elinx', 22, 30, 3)
s.speak()


class TestC:

    tests = 1

    @staticmethod
    def test(self):
        return 1

    def test1(self):
        return self


print(TestC.test(self=1))

