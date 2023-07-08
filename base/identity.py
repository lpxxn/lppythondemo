a = 1

print(type(a))
print(type(int))
print(id(a))
print(id(int))


class Cat:
    """构造函数"""

    def __init__(self, name):
        self.name = name
        self.__private_name = name
        print("Cat init")

    """析构函数"""

    def __del__(self):
        print("Cat del")

    """重写__str__方法"""

    def __str__(self):
        return "Cat name is %s" % self.name

    """重写__call__方法, 实例对象后面加括号，触发执行, 也可以直接调用实例对象的__call__方法, 但是不建议这么做, 会让人迷惑, 一般用于装饰器"""

    def __call__(self, *args, **kwargs):
        print("Cat call, args: %s, kwargs: %s, name: %s" % (args, kwargs, self.name))
        print("args[0]: %s" % args[0])
        print("kwargs['name']: %s" % kwargs['name'])

    """重写__len__方法, 返回长度"""

    def __len__(self):
        return len(self.name)

    """重写__iter__方法, 返回迭代器"""

    def __iter__(self):
        return iter([1, 2, 3])

    def __getitem__(self, item):
        if item == 1:
            return self.name
        elif item == "name":
            return self.name + " !"
        else:
            return None

    def __setitem__(self, key, value):
        print("setitem key: %s, value: %s" % (key, value))
        if key == "name":
            self.name = value

    def __add__(self, other):
        if isinstance(other, Cat):
            return [self, other]
        elif isinstance(other, list):
            return other.append(self)


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

# __bases__ 类的所有父类构成元素（包含了一个由所有父类组成的元组）
print(Cat.__bases__)
print(int.__bases__)
print(type.__bases__)

# __call__ 实例对象后面加括号，触发执行
cat = Cat("Tom1")
cat("a", "b", name="Tom")

# __dict__ 类的属性（包含一个字典，由类的数据属性组成）
print("cat dict", cat.__dict__)  ## cat dict {'name': 'Tom1', '_Cat__private_name': 'Tom1'}
print("Cat dict", Cat.__dict__)

# __main__ 表示当前执行模块
# 如果是被其他模块 import 的，则显示实际的模块名
print(__name__)

# __len__ 重写__len__方法, 返回长度
print(len(cat))

# __iter__ 重写__iter__方法, 返回迭代器
for i in cat:
    print(i)

print(cat[1])
print(cat["name"])
print(cat["name1"])

# _add__ 重写__add__方法, 返回迭代器
cat1 = Cat("Tom2")
print(cat + cat1)
print(cat + [1, 2, 3])
