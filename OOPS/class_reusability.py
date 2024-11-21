# Composition (HAS-A)
# Composition is a process of creating object of one class inside another
# class.

class Address:
    def __init__(self) -> None:
        self.__street=None
        self.__city=None
    
    def readAddress(self):
        self.__street = input("Enter street name : ")
        self.__city = input("Enter city name : ")
    
    def printAddress(self):
        print(f"Street : {self.__street}")
        print(f"City : {self.__city}")
    
class Person:
    def __init__(self) -> None:
        self.__namme = None
        self.address = Address()
    
    def readPerson(self):
        self.__namme = input("Enter name of person :")
        self.address.readAddress()
    
    def printPerson(self):
        print("Details of person ")
        print(f"Name : {self.__namme}")
        self.address.printAddress()

p1 = Person()
p2 = Person()
p1.readPerson()
p2.readPerson()
p1.printPerson()
p2.printPerson()


class Engine:
    def start(self):#instance method
        print("Engine start...")
    def stop(self):#instance method
        print("Engine stop...")

class Car:
    def __init__(self) -> None:
        self.engin = Engine()
    
    def start(self):
        return self.engin.start()
    
    def stop(self):
        return self.engin.stop()
    
c1 = Car()
c1.start()
c1.stop()