# while True:
#     try:
#         n1 = int(input("Enter number :"))
#         n2 = int(input("Enter number :"))
#         n3 = n1/n2
#         print(f"{n1}/{n2} = {n3}")
#         break
#     except (ZeroDivisionError,ValueError):
#         print("invalid integer plz.. enter valid integer")
#         print("Can't divide number by 0")

# while True:
#     try:
#         n1 = int(input("Enter number :"))
#         n2 = int(input("Enter number :"))
#         n3 = n1/n2
#         print(f"{n1}/{n2} = {n3}")
#         break
#     except ZeroDivisionError:
#         print("Can't divide number by 0")
#     except ValueError:
#         print("invalid integer plz.. enter valid integer")


#login application
#without handling exception
# users = {'Aniket':'ani123',
#         'Harshal':'harsh123',
#         'Kunal':'kun123'
#         }

# user = input("Enter user :")
# password = input("Enter password :")
# if users[user]==password:
#     print(f"{user} login successfully.")
# else:
#     print(f"Invalid password")

# #login logic
# #handling exception

# users = {'Aniket':'ani123',
#         'Harshal':'harsh123',
#         'Kunal':'kun123'
#         }
# try :
#     username = input("Enter username :")
#     password = input("Enter password :")
#     if users[username]==password:
#         print(f"{username} is login successfully.")
#     else:
#         print("Invalid Password")
# except KeyError:
#     print(f"{username} is not found is users.")


# marks = {'Harshal':[90,32,85],
#         'Prathm':[30,45,80],
#         'Kunal':[89,45,79]
#         }
# while True:
#     try:
#         name = input("Enter student name :")
#         m = marks[name]
#         total = sum(m)
#         result = "Pass"
#         for subject in m:
#             if subject<40:
#                 result="Fail"
#                 break
#         print(f"Name of student : {name}")
#         print(f"Marks of student : {m}")
#         print(f"Total Marks of student : {total}")
#         print(f"Result of student : {result}")
#         break
#     except Exception:
#         print("Something went wrong.")


# Error with empty except
# while True:
#     try:
#         n1 = int(input("Enter value :"))
#         n2 = int(input("Enter value :"))
#         n3 = n1/n2
#         print(f"{n1}/{n2} = {n3}")
#         break
#     except:
#         print(f"Plz.. enter valid integer or don't enter zero")

# from bcrypt import gensalt, hashpw, checkpw

# def hash_password(plain_password: str) -> str:
#     """Hash the plain password using bcrypt."""
#     salt = gensalt()
#     hashed_password = hashpw(plain_password.encode('utf-8'), salt)
#     return hashed_password.decode('utf-8')

# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     print("Password verification :",plain_password.encode('utf-8'),hashed_password.encode('utf-8'))
#     return checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

# plain_pass = "harsh123"
# hash_pass = hash_password(plain_pass)
# print("Harsh password :",hash_pass,type(hash_pass))
# plain_pass = "harsh123"
# is_equal = verify_password(plain_pass,hash_pass)
# print(is_equal)

# raise keyword
# This keyword is used for generating exception or raising exception or error.
# Generating error is nothing but creating error object and giving to python
# runtime system (PVM).

def division(n1,n2):
    if n1==0 or n2==0:
        raise ValueError()
    else:
        return n1/n2

try:
    n1 = int(input("Enter num :"))
    n2 = int(input("Enter num :"))
    n3 = division(n1,n2)
    print(n3)
    print(f"{n1}/{n2} = {n3}")
except :
    print("plz.. enter valid integer")


# User defined error types or exception types
# When existing error types does not fulfill application requirement we build
# our own error types, which are called user defined error types or exception
# types.
# Creating error type is nothing creating class.

class ZeroMultiplyError(Exception):
    pass

def mul(n1,n2):
    if n1==0 or n2==0:
        raise ZeroDivisionError()
    else:
        return n1*n2

try:
    n1 = int(input("Enter val :"))
    n2 = int(input("Enter val :"))
    n3 = mul(n1,n2)
    print(f"{n1}*{n2} = {n3}")
except ValueError:
    print("Enter valid integer")
except ZeroDivisionError:
    print("cannot multiply number by 0")


users = {"Harshal":"h123","Aniket":"a123","Kunal":"k123"}
class LoginError(Exception):
    def __init__(self, msg=None):
        super().__init__()
        self.__msg = msg
    def __str__(self) -> str:
        return self.__msg
def login(unmae,pwd):
    if unmae in users and users[unmae]==pwd:
        return f"Welcome {unmae}"
    else:
        raise LoginError("Invalid username or password")
    
try:
    name = input("Enter username :")
    pwd = input("Enter password :")
    is_login = login(name,pwd)
    print(is_login)
except LoginError as lgerror:
    print(lgerror)


class InsuffBalError(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.__msg = "Invalid Balance"
    
    def __str__(self) -> str:
        return self.__msg

class Account:
    def __init__(self,ano,aname,abalance) -> None:
        self.__accno = ano
        self.__accname = aname
        self.__accbalance = abalance
    
    def deposit(self,amount):
        self.__accbalance += amount
    
    def withdraw(self,amount):
        if amount>self.__accbalance:
            raise InsuffBalError()
        else:
            self.__accbalance-=amount
    def printinfo(self):
        print(f"Account no : {self.__accno}\nAccount Holder name : {self.__accname}\nAccount Balance : {self.__accbalance}")

try:
    a1 = Account(101,"Harshal Kharabe",50000)
    # a1.deposit(30000)
    print("Amount deposit successfully!")
    a1.withdraw(30000)
    print("Amount withdraw successfully!")
    a1.printinfo()
except InsuffBalError as iserror:
    print(iserror)

# try..except..else block
# else block is executed when there is no error/exception within try block.

try:
    n1 = int(input("Enter number :"))
    n2 = int(input("Enter number :"))
    n3 = n1/n2
    print(f'{n1}/{n2} = {n3}')
except ZeroDivisionError:
    print("Something went wrong.")
else:
    print("I am Else block")
    
#try..except..else..finally

try:
    n1 = int(input("Enter number :"))
    n2 = int(input("Enter number :"))
    n3 = n1/n2
    print(f'{n1}/{n2} = {n3}')
except ZeroDivisionError:
    print("Something went wrong.")
else:
    print("I am Else block if exception occured in try block that time i am not execute")
finally:
    print("I am finally i always execute")