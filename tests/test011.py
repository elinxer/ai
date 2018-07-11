
from tests.libs import CustomError as custom

"""
异常处理

except 是异常定义的方式, 使用的异常必须为Python自带或者自定义的

如除零错误 ZeroDivisionError

"""


def this_fails():

    """ 抛出异常方法, 在使用方法之前要先引入该方法,顺序要提前 """
    return 1 / 0


try:

    # this_fails()
    """
    raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。
    如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。
    """
    # raise NameError('指定抛出的异常信息')

    """ 抛出指定的自定义异常 """
    raise custom.CustomError('error info111111')

except Exception as err:
    print("Exception error: ", err)
    pass


