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
