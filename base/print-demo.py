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

# String
str = '一二三四五六七八'
print(str)
print(str[0:-1]) # 第一个到倒数第二个
print("1:3", str[1:3])
'''+ 是连接字符串 *: 复制字符串'''
print("+", str + " !!!")
print("*", str * 2)

threeSingleQuote = '''\'\'\''''
threeQuote = '''\"\"\"'''

print('''\n 是转义,如果不想让\发生转义,可以在字符串前加上r,表示原始字符串, 也可以使用{0}...{0} 或者"""...""" :'''.format(threeSingleQuote))

print('hello\n haha', r'hello\n haha')
print(str[0], str[2], str[-1], str[-2])
