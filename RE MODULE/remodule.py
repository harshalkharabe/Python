#Regular expression

#2 ways to define regular expression
# 1. using r'string' (row string)
# 2. using compile method of re 

import re
s1 = r'Harshal kharabe'
print(type(s1)) # --> <class 'str'>
s2 = re.compile("Harshal Kharabe")
print(type(s2)) # --> <class 're.Pattern'>

# searching methods of re module

# 1.re.search()

s1 = "Python java Python python"
data = re.search("Python",s1)
print(data) # Python is 2 times in s1 but it returns only 1 

data = re.search("java",s1)
print(data)

data = re.search("python",s1)
print(data)

data = re.search("ythonjj",s1)
print(data)

# 2. re.match()

s1 = "Python java Python python"
data = re.match(s1,"java")
print(data) # it checks only at staring of string

data = re.match("python",s1)
print(data)

data = re.match("Python",s1)
print(data)

# 3. re.findall()

s1 = "Python java Python python"
data = re.findall("python",s1)
print(data) # it returns in list and all occurens of 

s1 = "Python java Python python"
data = re.findall("Python",s1)
print(data) # it returns in list

data = re.findall('java',s1)
print(data)


s1 = "Python"
is_equal = re.fullmatch("python",s1)
print(is_equal) # it is similar to == operator

s1 = "Python"
is_equal = re.fullmatch("Python",s1)
print(is_equal)


# special characters 

# . (Dot)
print("-------------------------------------------------------------------------")
s1 = "naresh suresh harshal kunal kishore rajesh ramesh"
data = re.findall(r"k.",s1)
print(data)

data = re.findall(r".a",s1)
print(data)

data = re.findall(r".r.",s1)
print(data)

data = re.findall(r"...",s1)
print(data)

#  ^ (cap)
print("-------------------------------------------------------------------------")
list1 = ["harshal","narsah","kunal","suresh","rakesh","rajesh","kishor"]
for i in list1:
    data = re.search(r"^r",i)
    if data != None:
        print(i)

list1 = ["harshal","narsah","kunal","suresh","rakesh","rajesh","kishor"]
for i in list1:
    data = re.search(r"^n",i)
    if data != None:
        print(i)

list1 = ["harshal","narsah","kunal","suresh","rakesh","rajesh","kishor"]
for i in list1:
    data = re.search(r"^",i)
    if data != None:
        print(i)

# $ (dollar)
print("-------------------------------------------------------------------------")
list1 = ["harshal","narsah","kunal","suresh","rakesh","rajesh","kishor"]
for name in list1:
    data = re.search(r'l$',name)
    if data!=None:
        print(name)

list1 = ["harshal.in","narsah.tech","kunal.com","suresh.in","rakesh.in","rajesh.tech","kishor.com"]
for i in list1:
    data = re.search(r".com$",i)
    if data!=None:
        print(i)


print("-------------------------------------------------------------------------")
# * (star)

s1 = "abb a abbb a abb ab bb"
data = re.findall(r'ab*',s1)
print(data) # 'ch*' means need 0 or more (ch)characters


print("-------------------------------------------------------------------------")
# + (plus)

s1 = "abb a abbb a abb ab bb"
data = re.findall(r'ab+',s1)
print(data) # 'ch+' means need 1 or more characters(ch)


print("-------------------------------------------------------------------------")
# ? (question)
s1 = "abb a abbb a abb ab bb"
data = re.findall(r'ab?',s1)
print(data) # ['ab', 'a', 'ab', 'a', 'ab', 'ab'] it need 0 or 1 character


print("-------------------------------------------------------------------------")
# {m} (curly braces)

s1 = ["naresh","suresh","rajesh","kishore","ramesh"]
for name in s1:
    data = re.fullmatch(r'.{6}',name)
    if data!=None:
        print(name)
print()
s1 = ["naresh","suresh","rajesh","kishore","ramesh"]
for name in s1:
    data = re.fullmatch(r'r.{5}',name)
    if data!=None:
        print(name)
print()
s1 = ["naresh","suresh","rajesh","kishore","ramesh"]
for name in s1:
    data = re.fullmatch(r'r.{4}h$',name)
    if data!=None:
        print("name :",name)
