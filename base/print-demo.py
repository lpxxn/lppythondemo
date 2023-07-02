print("你好")

print("你好", end="")
print("abc")

import keyword
print("list all keyword list:")
print(keyword.kwlist)

import sys

print('========Python import mode========')
print('命令行参数:')
for i in sys.argv:
    print(i)

print('\n python path:', sys.path)


## type 数据类型
a = 1
print(type(a), a)

a = 'b'
print(type(a), a)

a = [1, '1']
print(type(a), a)

'''也可以用 isinstance 来判断'''
print("is a instance list: ", isinstance(a, list))

"""
isinstance 和 type 的区别在于：

type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
"""

class A:
    pass

class B(A):
    pass

print(isinstance(A(), A)) # True

print(type(A()) == A)  # True

print(isinstance(B(), A)) # True

print(type(B()) == A) # False

# 也可以用 issubclass
print(issubclass(bool, int))

print(issubclass(B, A))


