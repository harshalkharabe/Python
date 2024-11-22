class person:
    def __init__(self) -> None:
        self.__name=None
    
    def setName(self):
        self.__name = input("Enter Name :")
    
    def getName(self):
        return self.__name
    
class customer(person):
    def __init__(self) -> None:
        # super().__init__()
        self.__balance=None
    
    def setBalance(self):
        self.__balance = int(input("Enter Balance :"))
    
    def getBalance(self):
        return self.__balance

obj = customer()
obj.setName()
obj.setBalance()
print("Name :",obj.getName())
print("Balance :",obj.getBalance())


class A:
    def __init__(self):
        self.x=100
        self.y=200
class B(A):
    def __init__(self):
        A.__init__(self)
        self.p=300
        self.q=400
objb=B()
print(objb.x,objb.y)
print(objb.p,objb.q)