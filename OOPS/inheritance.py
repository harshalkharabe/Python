# simple inheritance
# class person:
#     def __init__(self) -> None:
#         self.__name=None
    
#     def setName(self):
#         self.__name = input("Enter Name :")
    
#     def getName(self):
#         return self.__name
    
# class customer(person):
#     def __init__(self) -> None:
#         # super().__init__()
#         self.__balance=None
    
#     def setBalance(self):
#         self.__balance = int(input("Enter Balance :"))
    
#     def getBalance(self):
#         return self.__balance

# obj = customer()
# obj.setName()
# obj.setBalance()
# print("Name :",obj.getName())
# print("Balance :",obj.getBalance())


# class A:
#     def __init__(self):
#         self.x=100
#         self.y=200
# class B(A):
#     def __init__(self):
#         A.__init__(self)
#         self.p=300
#         self.q=400
# objb=B()
# print(objb.x,objb.y)
# print(objb.p,objb.q)


# multi-level inheritance
# class Person:
#     def __init__(self) -> None:
#         self.__name=None
#     def setname(self):
#         self.__name = input()
#     def getname(self):
#         return self.__name
# class Emp(Person):
#     def __init__(self) -> None:
#         self.__job=None
#     def setjob(self):
#         self.__job = input()
#     def getjob(self):
#         return self.__job
# class Sal(Emp):
#     def __init__(self) -> None:
#         self.__sal=None
#     def setsal(self):
#         self.__sal = input()
#     def getsal(self):
#         return self.__sal

# obj = Sal()
# obj.setname()
# obj.setjob()
# obj.setsal()
# print("Name :",obj.getname())
# print("Job :",obj.getjob())
# print("Salary :",obj.getsal())


#multiple inheritance
class person:
    def __init__(self,name) -> None:
        self.name=name
    def getname(self):
        return self.name
class emp:
    def __init__(self,job) -> None:
        self.job=job
    def getjob(self):
        return self.job
class worker(person,emp):
    def __init__(self,name,job,sal) -> None:
        super().__init__(name)
        emp.__init__(self,job)
        self.sal=sal
    def getsal(self):
        return self.sal
w1 = worker("Harsh Kharabe","Python Developer",300000)
print("Name :",w1.getname())
print("Job :",w1.getjob())
print("Salary :",w1.getsal())


#Herarchical inheritance
class A:
    def __init__(self) -> None:
        print("These is A class")
class B(A):
    def __init__(self) -> None:
        super().__init__()
        print("These is B class")
class C(A):
    def __init__(self) -> None:
        super().__init__()
        print("These is C class")

c = C()
b = B()


#Hybrid inheritance
class A:
    def m1(self):
        print("Method of A class")
class B(A):
    def m2(self):
        print("Method of B class")
class C(B):
    def m3(self):
        print("Method of C class")
class D(B,A):
    def m4(self):
        print("Method of D class")

obj = D()
obj1 = C()
obj.m1()
obj.m2()
obj.m4()
# obj.m3()
obj1.m1()
obj1.m2()
obj1.m3()

