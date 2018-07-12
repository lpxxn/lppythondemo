class People:
    def __init__(self):
        pass

    def sayHello(self):
        print('hello world')

    def say(self):
        self.sayHello()


class Student(People):
    def __init__(self):
        pass
        People.__init__(self)
        # super(Student, self).__init__(self)

    def sayHello(self):
        print('hello , i am a student')


if __name__ == "__main__":
    s1 = Student()
    s1.say()
