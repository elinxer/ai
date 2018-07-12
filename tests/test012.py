
"""
import 说明

from package_name.name import module_name

import导入的是整个包中的某个模块


from tests.libs(这是包的路径) import tests(这个是文件名)

from tests.libs(这是包的路径) import tests(这个是文件名) as 别名

"""


#from tests.libs import tests

import tests.libs.tests as t

print(t.f())

x = t.TestClass()

print(x.f())
