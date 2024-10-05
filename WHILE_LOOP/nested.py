"""Nested while
A while loop inside while loop is called nested while.

Syntax:
while <condition>: # Outer Loop
while <condition>: # Inner Loop
    statement-1
    statement-2
    statement-3"""
# while loop is repeated until given condition is True, if condition is False stop
# executing while loop.

# print tables from 1 to 5 using while loop
# n = 1
# while n<=5:
#     i=1
#     while i<=10:
#         print(f"{n}x{i}={n*i}")
#         i+=1
    # n+=1

# Write a program to armstrong numbers from 100 to 999
num=100
while num<1000:
    num1 = num
    s = 0
    while num>0:
        r = num%10
        s = s+ (r**3)
        num = num//10
    if s==num1:
        print(num1)
    num = num1+1