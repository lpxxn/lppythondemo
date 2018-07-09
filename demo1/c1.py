#! /usr/local/bin/python3

class myClass1:
    """第一个类"""
    i = 123
    __b = "bbb"

    def f(self):
        print(self.i)
        print(self.__b)
        print(self)
        print(self.__class__)
        return "Hello World"

    def __init__(self, a="none", b="none"):
        self.a = a
        self.__b = b


x = myClass1()
print(x.f())
x.i += 111
print(x.i)

print(x.a)
print(dir(myClass1))
print(dir(x))

print("-----------")


class MyClass2(myClass1):
    i = 2222

    def __init__(self, a="none", b="none"):
        super().__init__(a, b)
        self.a = a
        self.__b = b

    def f(self):
        print(self.i, "22222")
        print(self.__b)
        print(self)
        print(self.__class__)
        return "Hello World" + "   22222"
    pass


x = MyClass2(a="aa", b="bb")
print(x.f())
x.i += 111
print(x.i)

print(x.a)
print(dir(MyClass2))
print(dir(x))

print("-----------")


class MyClass3(myClass1):
    pass


x = MyClass3(a="aa", b="bb")
print(x.f())
x.i += 111
print(x.i)

print(x.a)
