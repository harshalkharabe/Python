# # Composition (HAS-A)
# # Composition is a process of creating object of one class inside another
# # class.

# class Address:
#     def __init__(self) -> None:
#         self.__street=None
#         self.__city=None
    
#     def readAddress(self):
#         self.__street = input("Enter street name : ")
#         self.__city = input("Enter city name : ")
    
#     def printAddress(self):
#         print(f"Street : {self.__street}")
#         print(f"City : {self.__city}")
    
# class Person:
#     def __init__(self) -> None:
#         self.__namme = None
#         self.address = Address()
    
#     def readPerson(self):
#         self.__namme = input("Enter name of person :")
#         self.address.readAddress()
    
#     def printPerson(self):
#         print("Details of person ")
#         print(f"Name : {self.__namme}")
#         self.address.printAddress()

# p1 = Person()
# p2 = Person()
# p1.readPerson()
# p2.readPerson()
# p1.printPerson()
# p2.printPerson()


# class Engine:
#     def start(self):#instance method
#         print("Engine start...")
#     def stop(self):#instance method
#         print("Engine stop...")

# class Car:
#     def __init__(self) -> None:
#         self.engin = Engine()
    
#     def start(self):
#         return self.engin.start()
    
#     def stop(self):
#         return self.engin.stop()
    
# c1 = Car()
# c1.start()
# c1.stop()


# Aggregation
# Aggregation is a special type of composition.
# In aggregation component object or contained object is not created inside
# composite class or container class, it is created outside the container class
# and inject to container class using methods

# class Author:
#     def __init__(self,name) -> None:
#         self.name=name
    
#     def getname(self):
#         print(f"Author name : {self.name}")

# class Book:
#     def __init__(self,bname,a1) -> None:
#         self.author = a1
#         self.book_name=bname
    
#     def getname(self):
#         self.author.getname()
#         print(f"Book name : {self.book_name}")

# a1 = Author("Harshal Kharabe")
# b1 = Book("Love Life",a1)
# b1.getname()

# class Course:
#     def __init__(self) -> None:
#         self.cname=input("Enter course name :")
#     def getcourse(self):
#         print(f"Course name : {self.cname}")
# class students:
#     def __init__(self,c) -> None:
#         self.sname = input("Enter student name :")
#         self.course = c
#     def getdetails(self):
#         print(f"Student name : {self.sname}")
#         self.course.getcourse()

# c1 = Course()
# s1 = students(c1)
# s1.getdetails()


# What is magic method or dunder method?
# Any method which is prefix and suffix with double underscore is called
# magic method or dunder method. This method is executed automatically.

#__str__()
class person:
    def __init__(self) -> None:
        print("Person is alive!!")
    def __str__(self):#oyerride method of object class
        return f"Me aahe string representation of object"
    
p1 = person()
print(p1)

class Date:
    def __init__(self,d,m,y) -> None:
        self.dd = d
        self.mm = m
        self.yy = y
        print(f"Date is in calander")
    def getdate(self):
        return f"{self.dd}/{self.mm}/{self.yy}"
    def __str__(self):
        res = self.getdate()
        return res
d1 = Date(11,12,2023)
print(d1)


class Maharastra:
    def __repr__(self) -> str:
        return ("Hello i am __repr__()")
    def __str__(self) -> str:
        return ("Hello i am __str__()")
m1 = Maharastra()
print(m1)
print(repr(m1))