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

