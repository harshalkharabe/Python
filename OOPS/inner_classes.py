# Nested classes or Inner classes
# A class defined inside class is called nested class or inner class.
# Usage of nested classes or inner classes
# 1. Hiding class
# 2. Dividing functionality of class into number of classes
# Types of nested classes
# 1. Member class
# 2. Local class
# Member class
# A class defined inside class is called member class (OR) inside class block.

class Person:
    class __Address:# inner class member class
        def __init__(self) -> None:
            self.__Area=None
            self.__city=None
        def read(self):
            self.__Area=input("Enter area :")
            self.__city=input("Enter city :")
        def printAdd(self):
            print(f"Area : {self.__Area}")
            print(f"City : {self.__city}")
    
    def __init__(self) -> None:
        self.__person=None
        self.__add = Person.__Address()
    def read(self):
        self.__person=input("Enter name :")
        self.__add.read()
    def printInfo(self):
        print(f"Name : {self.__person}")
        self.__add.printAdd()

p1 = Person()
p1.read()
p1.printInfo()


class A:
    class B:
        def m1(self):
            print("m1 of class B")
    
    class __C:
        def m2(self):
            print("m2 of class __C")
    
    def m3(self):
        obj = A.__C()
        obj.m2()

obj1 = A.B()
obj1.m1()
obj2 = A()
obj2.m3()
