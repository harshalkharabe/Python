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


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,6,9,8,7,4,5]
srow = 0
erow = len(matrix)-1
scol = 0
ecol = len(matrix[0])-1
op = []
while srow<=erow and scol<=ecol:
    #top row
    for i in range(scol,ecol+1):
        op.append(matrix[srow][i])

    #right col
    for i in range(srow+1,erow+1):
        op.append(matrix[i][ecol])

    #down row
    for i in range(ecol-1,scol-1,-1):
        if srow==erow:
            break
        op.append(matrix[erow][i])

    #left col
    for i in range(erow-1,srow,-1):
        if scol==ecol:
            break
        op.append(matrix[i][scol])

    srow+=1
    erow-=1
    ecol-=1
    scol+=1
print(op)