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