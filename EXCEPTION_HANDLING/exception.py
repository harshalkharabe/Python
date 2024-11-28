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
while True:
    try:
        n1 = int(input("Enter value :"))
        n2 = int(input("Enter value :"))
        n3 = n1/n2
        print(f"{n1}/{n2} = {n3}")
        break
    except:
        print(f"Plz.. enter valid integer or don't enter zero")