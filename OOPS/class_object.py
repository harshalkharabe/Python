
# The methods defined inside class are 3 types
# 1. Instance method/object level method
# 2. Class method
# 3. Static method

# class student:
#     def __init__(self,n,a) -> None:
#         self.name = n
#         self.age = a
    
#     def print_data(self):
#         print(f"Name of student : {self.name}")
#         print(f"Age of student : {self.age}")

# s1 = student("Harshal",20)
# s2 = student("Aniket",21)

# s1.print_data()
# s2.print_data()


# class Customer:
#     def __init__(self,accno,accname,accbal) -> None:
#         self.account_number = accno
#         self.account_name = accname
#         self.account_balance = accbal

#     def check_balance(self):
#         print(f"Current balance of {self.account_name} user is {self.account_balance}")
#         return
    
#     def deposit(self,amount):
#         self.account_balance+=amount

#     def withdraw(self,amount):
#         if amount<self.account_balance:
#             self.account_balance-=amount
    
#     def print_customer(self):
#         print(f"Account holder name {self.account_name}")
#         print(f"Account number {self.account_number}")
#         print(f"Account total balance {self.account_balance}")

# a1 = Customer(int(input("Enter account number :")),input("Enter holder name :"),int(input("Enter balance :")))
# a1.print_customer()
# a1.withdraw(int(input("Enter amount to withdraw :")))
# a1.check_balance()
# a1.print_customer()
# a1.deposit(int(input("Enter amount to deposit :")))
# a1.check_balance()
# a1.print_customer()


# Write a program to read details n players
# each player is having name,runs

# class Players:
#     def __init__(self,pname,pscore) -> None:
#         self.player_name = pname
#         self.player_score = pscore
    
#     def print_players_data(self):
#         print(f"{self.player_name} score {self.player_score} runs today!!")
#         return

# players_list = []
# n = int(input("Enter how many players data you want to stored :"))
# for i in range(n):
#     p = Players(input("Enter player name :"),int(input("Enter player score :")))
#     players_list.append(p)
# print(players_list)
# for player in players_list:
#     player.print_players_data()


# Access Modifiers
# Access modifiers are used to define accessibility of members of the
# class
# 1. Private
# 2. Protected
# 3. Public
# The members of the class can be declared as private, public or
# protected. Default members of the class public.

class student:
    def __init__(self,rollno,name,course) -> None:
        self.__rollnumber = rollno # private varibale
        self.__student_name = name # private varibale
        self.__student_course = course # private varibale
    
    def student_data(self):
        print(f"Student roll number {self.__rollnumber}")
        print(f"Student name {self.__student_name}")
        print(f"Student course {self.__student_course}")

s1 = student(11,"Harshal Kharabe","Python")
s2 = student(12,"Ani","Java")
s1.student_data()
print("-"*25)
s2.student_data()


class Example:
    def __init__(self) -> None:
        self.x = 12 # public variable
        self.__y = 21 # private varibale
    
    def access_private(self):
        print(self.__y)
    
e1 = Example()
print("Data of public variable ",e1.x)
# print("Data of private variable ",e1.__y) #it gives an error beacuse 
# # private varibale is not accessible outside the class
e1.access_private()


# class Area:
#     def __init__(self,h,b) -> None:
#         self.__height = h
#         self.__base = b
    
#     def find_area(self):
#         print("Height of triangle : ",self.__height)
#         print("Base of triangle : ",self.__base)
#         return self.__height*self.__base*0.5
    
# t1 = Area(int(input("Enter height :")),int(input("Enter base :")))
# # t1.find_area()
# print("Are of triangle :",t1.find_area())

class stud:
    college_name = "SKC"
    def __init__(self,r,n) -> None:
        self.roll = r
        self.name = n
    def print_data(self):
        print(f"Roll no :",self.roll)
        print(f"Name of Students :",self.name)
        print(f"College name : {stud.college_name}")

s1 = stud(11,"Harshal Kharabe")
s2 = stud(12,"Aniket Bhudke")
s1.print_data()
s2.print_data()

class bank:
    bank_name = "State Bank of india Hiwarkhed"
    def __init__(self,accno,name,balance) -> None:
        self.accno = accno
        self.name = name
        self.balance = balance
    
    def bank_info(self):
        print(f"Bank name : {bank.bank_name}")
        print(f"Account number : {self.accno}")
        print(f"Account holder name : {self.name}")
        print(f"Account Balance : {self.balance}")
    
b1 = bank(101,"Harshal Kharabe",12098326)
b2 = bank(102,"Aniket Bhudke",32100450)
b1.bank_info()
b2.bank_info()


class Math:
    @staticmethod
    def isprime(num):
        for i in range(2,num):
            if num%2==0:
                return False
        return True

    @staticmethod
    def power(num,p):
        return num**p
    
    @staticmethod
    def reverse(num):
        rev = 0
        while num>0:
            d = num%10
            rev = (rev*10)+d
            num //= 10
        return rev

print("Number is prime :",Math.isprime(19))
print("Number is prime :",Math.power(5,2))
print("Number is prime :",Math.reverse(123))
m = Math()
print("Number is prime :",m.isprime(17))
print("Number is prime :",m.power(2,5))
print("Number is prime :",m.reverse(981))


#class methods
class person:
    __count = 0
    def __init__(self,n,a) -> None:
        self.name = n
        self.age = a
        person.__count+=1
    def printPerson(self):
        print(f"Name of person : {self.name}")
        print(f"Age of person : {self.age}")
    
    @classmethod
    def count_of_person(cls):
        print("Total person :",cls.__count)

p1=person("Aniket",20)
p2=person("Kunal",21)
p3=person("Sagar",19)

p1.printPerson()
p2.printPerson()
p3.printPerson()
person.count_of_person()