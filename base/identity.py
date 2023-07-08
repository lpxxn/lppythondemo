a = 1

print(type(a))
print(type(int))


class Cat:
    """构造函数"""
    def __init__(self, name):
        self.name = name
        print("Cat init")

    """析构函数"""
    def __del__(self):
        print("Cat del")

    def __str__(self):
        return "Cat name is %s" % self.name


cat = Cat("Tom")
print(cat)
print(type(cat))
print(type(Cat))
del cat
# print(cat) ## error cat is not defined

# __doc__ 获取类的文档字符串
print(Cat.__doc__)

# __name__ 类名
print(Cat.__name__)

# __module__ 类定义所在的模块
print(Cat.__module__)