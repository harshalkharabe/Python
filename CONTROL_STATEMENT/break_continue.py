"""Branching Statements
Python support 2 branching statements
1. break
2. continue
3. pass
Branching statements are used to control the execution of while loop or for
loop.
break
This keyword is used to terminated execution of while loop or for loop."""

# for i in range(1,6):
#     print("Hello")
#     break

for i in range(1,6):
    print("Hello")
    if i == 3:
        break
    print("Bye")

# while True:
#     username = input("Enter user name : ")
#     password = input("Enter password :")
#     if username=="omg" and password=="paa":
#         print(f"Welcome {username}")
#         break
#     else:
#         print(f"Wrong username or password")

# continue
# “continue” is a keyword
# This keyword is used in looping statements. It is used to continue looping
# statement.

for i in range(1,11):
    if i%2==0:
        continue
    print(i,end=' ')

print()

for i in range(1,6):
    print("Harshal")
    continue
    print("Aniket")

