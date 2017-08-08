def test_var_args(farg, *args):
    print("formal arg:", farg)
    for arg in args:
        print("another arg:", arg)


test_var_args(1, "two", 3)


def test_var_kwargs(farg, **kwargs):
    print("formal arg:", farg)
    for key in kwargs:
        print("another keyword arg: %s: %s" % (key, kwargs[key]))


def test_var_args(farg, *args, **kwargs):
    print("formal arg:", farg)
    for arg in args:
        print("another arg:", arg)
    print(kwargs)


test_var_args(1, "two", 3, myarg2="two", myarg3=3)
test_var_kwargs(farg=1, myarg2="two", myarg3=3)

import struct

if struct.calcsize("P") == 4:
    print('32位')
else:

    print('64位')

# 这是一种特殊的语法，在函数定义中使用*args和**kwargs传递可变长参数.
# *args用作传递非命名键值可变长参数列表（位置参数）;
# **kwargs用作传递键值可变长参数列表
