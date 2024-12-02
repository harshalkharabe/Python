# functions
# Python is multi paradigm programming language. It allows writing programs
# using different programming approaches or paradigms. A programming
# paradigm defines set of rules and regulations of writing program or
# organizing instructions.

def fun():
    print("Hello, World!!")
fun()

def star():
    for i in range(20):
        print('*',end=' ')
    print()
print("Python")
star()
print("Programming")
star()
print("Language")

def add():
    a = 5
    b = 5
    print(f"Addition of {a} and {b} is {a+b}")

def sub():
    a = 5
    b = 50
    print(f"Substracion of {a} and {b} is {a-b}")

add()
sub()

# Local Variables
# A variable created inside function is called local variable.
# The scope of local variable is within function and lifetime is until execution
# of function.

def fun():
    a = 10 # local variable
    print(a)
fun()
# print(a) Error beacuse a is local variable you can not assecc it outsibe the block

# Global Variables
# The variables created outside the function are called global variables.
# These variables can accessible within one or more than one function. In
# order to share data between number of functions it is declared as global.

# a = 12 # global
# def fun():# we can use global variable insibe the function 
#     print(a)
# print(a)
# fun()

def fun1():
    print(a)
a = 100 # global varibale always define before function function call
fun1()                                                             
def fun2():
    print(a)
fun2()


# want to update the value of global variable in function

a = 100 # these is local varibale
def fun():
    a = 120 # these is local variable
    print(a)
fun()
print("After try to assign value in fun:",a)

x = 100
def fun():
    global x
    x = 120
    print(x)
fun()
print("After update value in fun:",x)


#function parameters
#required parameter
def fun(n1,n2):
    print(n1,n2)

#we pass 2 parameters at the time of calling function
fun(12,5)
# fun(12) it gives error 

def fun(name):
    print("Name :",name)
fun("Harshal")
fun("Aniket")

#function parameter
#keyword argument
def fun(name):
    print("Name :",name)
fun(name="Harshal")
fun(name="Kunal")

#function with default argument
def fun(n1,n2,n3=None):
    print(n1,n2,n3)
fun(12,"Harshal")
fun(13,"Aniket","BCA")
fun(14,"Kunal","MCA")

#how power function works
def power(num,pow):
    result = num**pow
    print("Power :",result)
power(3,3)

# How to define function with position only required arguments?
# A function is defined with special parameter whose name is /
# In order define function with position only argument, last parameter in
# function must be /
def fun(a,b,/):
    print("it takes only required arguments :",a,b)
fun(12,34)
# fun(12,b=34) it gives error

# How to define function with keyword only required arguments?
# A function is defined with special parameter whose name is *
# In function definition if * first parameter, the remaining parameters are
# keyword only required arguments
def fun(*,name,roll):
    print(name,roll,"it takes only keyword arguments")
fun(name="Harshal",roll=11)
# fun("paa",12) it gives error


# return keyword
# This keyword is used by function to return value to calling function or caller.
# return is called branching statement or passes control statement.
# After returning value to calling function, it terminates execution of function.
def fun(a,b):
    return a+b
result = fun(12,5)
print("Addition of a,b is",result)

def maximun(a,b):
    return a if a>b else b
result = maximun(12,5)
print(f"Maximun : {result}")
result = maximun(5,13)
print(f"Maximun : {result}")

def isprime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

# num = int(input("Enter num : "))
# print(f"{num} is prime : {isprime(num)}")

def ispalandrom(str):
    if str==str[::-1]:
        return True
    return False
# str1 = input("Enter string :")
# print(f"{str1} is palandrom {ispalandrom(str1)}")

def sort(lst,reverse=False):
    if reverse==False:
        for i in range(len(lst)):
            for j in range(len(lst)-1):
                if lst[j]>lst[j+1]:
                    lst[j],lst[j+1]=lst[j+1],lst[j]
                    
    elif reverse==True:
        for i in range(len(lst)):
            for j in range(len(lst)-1):
                if lst[j]<lst[j+1]:
                    lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
l1=[5,7,3,2,8,1,9,4]
print("Sorted list :",sort(l1))

#How to invoke or call inner function outside outer function?
# In order invoke inner function outside outer function, outer function must
# return reference of inner function

# def fun1():
#     print("Outer function")
#     def fun2():
#         print("Inner function")
#     return fun2
# res = fun1()
# res()

def box(function):
    def new_display():
        print("*************************")
        function()
        print('*************************')
    return new_display
@box
def display():
    print('Hello Python')

display()

def upper(function):
    def list_str(a):
        print("*"*10)
        function(a)
        print("*"*10)
    return list_str
@upper
def print_list_str(a):
    for s in a:
        print(s.upper())

l1 = ["Harshal","Pratham","Kunal","Sagar","Ani"]
print_list_str(l1)

def fun(x):
    print(x) # these is parameter value pass at the time of calling function
    x = 10
    print(x) # these is new local varibale of fun
a = 12
fun(a)


def box(fun):
    def new_student_info(dic):
        print("*"*10)
        fun(dic)
        print("*"*10)
    return new_student_info

@box
def stud_info(dict1):
    for i,j in dict1.items():
        print(f"{i} --> {j}")

dic = {"name":"Harshal","age":21}
stud_info(dic)


def closers(val):
    def power(p):
        return val**p
    return power

power1 = closers(5)
print(power1(3))
print(power1(4))
print(power1(5))
power2 = closers(7)
print(power2(3))
print(power2(4))
print(power2(5))
power3 = closers(6)
print(power3(3))
print(power3(4))
print(power3(5))


def fun(num):
    if num:
        return True
    return False

l1 = [1,2,3,3]
l2 = list(filter(fun,l1))
print(l2)

def stars(fun):
    def new_fun():
        print("*"*20)
        fun() # info()
        print("*"*20)
    return new_fun

def info():
    print("Hello, Python")

n = stars(info)
n() # new_fun()


t1 = (num for num in range(1,11))
t1 = tuple(t1)
for i in t1:
    print(i)  # it is like tuple comprehension


#FILTER FUNCTION
def even(num):
    if num%2==0:
        return True
    else:
        return False
    
l1 = [1,2,3,4,5,6,7,8,9,10]
n = list(filter(even,l1))
print(n)

n = list(filter(lambda num:num%2==1,l1)) # using lambda
print(n)

#Decorator
def decorator(fun):
    def new_division(n1,n2):
        if n2==0:
            return 0
        else:
            return fun(n1,n2)
    return new_division

@decorator
def div(n1,n2):#new_division
    return n1/n2

n1 = int(input("Val :"))
n2 = int(input("Val :"))
print("Division : ",div(n1,n2))


#Generators 
def gen(l1):
    for i in l1:
        yield i

l1=[1,2,3,4,5]
a = gen(l1)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# for i in a:
#     print(i)


a = (i for i in range(1,11)) # we don't use yield here
a = tuple(a)
for i in a:
    print(i)
# for i in a:
#     print(i)


def fun(s):
    for i in s:
        yield i

s = "Prathamesh"
v = fun(s) #Prathamesh
print(next(v))


# l1 = [num%2==0 for num in range(1,11)]
# print(l1)

#function overloading is not aalowed in python 
def fun1():
    print('Inside function 1')

def fun1(x):
    print("Inside fun 2")

fun1(3)

#lambda function
#filter functio
# is a higher order function which takes function as a input known as higher order function

a = list(filter(lambda x:x%2==0,[12,1,34,56,78]))
print(a)

list1=[1,2,3,4,5,6,7,0,0,0,0]
b = list(filter(None,list1)) # it return true values
print(b)

#map function
# map(function, iterable, *iterables)

names = ["Harshal","Aniket","Prathamesh","Kunal","Sagar","Ram"]
l1 = list(map(str.upper,names))
print(l1)

l1 = ["10","20","30","40","50"]
l2 = list(map(int,l1))
print(l2)

l1 = [12,34,56,78,90]
l2 = [8,21,59,88,20]
l3 = list(map(lambda x,y:x+y,l1,l2))
print(l3)

#Recursion :
# Calling function itself is called function recursion or recursive function call.
# In function recursion calling function and called function both are same.
# Function recursion uses stack (LIFO) for evaluating recursion calls.
# Complex algorithms are solved in simple way using function recursion.

# def func():
#     print("Function 1")
#     func()

# import sys
# print("Maximum limit :",sys.getrecursionlimit()) # to find max recursion limit

# sys.setrecursionlimit(10)
# print("Maximum limit :",sys.getrecursionlimit()) # to find max recursion limit
# func()

# recursion consist of 3 statements 
# initialization statement
#conditio statement
#updation statement

def fun(num):
    if num>0:
        fun(num-1)
    print(f"Inside {num}")
fun(5)

# Write a program to find factorial of input number
# def find_factorial(num):
#     if num==0:
#         return 1
#     return num*find_factorial(num-1) # 5*find_factorial(4)

# n=int(input("Enter num to find fact :"))
# print(find_factorial(n))

# Write a program to find count of digits in a given number
c = 0
def count_digit(num):
    global c
    if num>0:
        c+=1
        count_digit(num//10)
    return c
print(f"Total len of num : {count_digit(12389)}")


def findKthLargest(nums, k):
    l1 = list(set(nums))
    print(l1)
    l1.sort()
    return l1[-k]

print(findKthLargest([3,2,3,1,2,4,5,5,6],4))

def myAtoi(s: str) -> int:
    s1 = ''
    for i in range(len(s)):
        if s[i]==' ':
            continue
        elif s[i].isalpha():
            break
        elif s[i]>='0' or s[i]<='9':
            s1 += s[i]
            print(s1)
    n = int(s1)
    return n

