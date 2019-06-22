#! /usr/local/bin/python3

class people:
    name = ''
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def weight(self):
        return self.__weight + 5

    def __w(self):
        # 私有方法
        pass

    def speak(self):
        print("im %s  age %d" % (self.name, self.age))

    def test_thing(self, value=0):
        print("thpe of value", type(value))
        self.thing = value

    def len_thing(self):
        return len(self.thing)

class speaker():
    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("im %s sya topic of : %s" % (self.name, self.topic))


class sample(people, speaker):
    a = ''

    def __init__(self, n, a, w, t):
        people.__init__(self, n, a, w)
        speaker.__init__(self, n, t)


test = sample("Tom", 3, 5, "Miao")
print(test.weight())
test.test_thing("abdde")
print(test.len_thing())
test.test_thing(123)
# 报错了，上面都正常，也就是说 test_thing()里的value可以传任何值thing动态的
# print(test.len_thing())

# 需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
test.speak()
