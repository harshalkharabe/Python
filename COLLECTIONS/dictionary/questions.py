# Dictionary
dict1 = {
            "name":"Harsh",
            "class":"3rd Year",
            "course":"Python FS",
            "faculty":"Satish Gupta"
        }
print(dict1)

# How to read dictionary values
# using key

print(dict1["name"])
print(dict1["class"])
print(dict1["course"])
print(dict1["faculty"])

# using for loop

for i in dict1:
    print(i,"-->",dict1[i]) # for loop only gives key based on key we can access values

# get(key, default=None)
# Return the value for key if key is in the dictionary, else default. If default is
# not given, it defaults to None, so that this method never raises a  KeyError .
# Syntax: dictionary-name.get(key,default=None)

print(dict1.get("")) # if key is not exist then don't give error
print(dict1.get("name"))
print(dict1.get("class"))
print(dict1.get("course"))
print(dict1.get("faculty"))

# setdefault(key, default=None)
# If key is in the dictionary, return its value. If not, insert key with a value
# of default and return default. default defaults to None.

print(dict1.setdefault("college","SKC"))
print(dict1) # if the key you want to read is not exist in dictionary then it add to dict
# if you don't give value then it took none value of that key

print(dict1.setdefault("firstname"))
print(dict1)

d1 = {"Harsh":123,"Ani":3435}
n = d1.keys()
print(n)

l1=[3,4,2,7,8,9,1,5,6,4,2]
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]>l1[j]:
            l1[i],l1[j]=l1[j],l1[i]
print(l1)


# Write a program to create dictionary to
# store n players details
# without comprehension
# n = int(input("How many players : "))
# players = {}
# for i in range(n):
#     name = input()
#     score = int(input())
#     players[name]=score
# print(players)

# #using comprehension
# d1 = {input("Name : "):int(input("Score : ")) for i in range(n)}
# print(d1)

d1 = {n:n*n for n in range(1,11)}
print("Square Dictionary :",d1)

d2 = {n:n**3 for n in range(1,11)}
print("Cude Dictionary :",d2)

d3 = {n:[n*i for i in range(1,11)] for n in range(1,6)}
print("Table Dictionary :",d3)

# Sort Python Dictionary by Key or Value – Python
dict1={3:30,5:50,2:20,4:40,1:10}
l1 = dict1.keys()
print(l1)
l1 = sorted(l1)
d1 = {key:dict1[key] for key in l1}
print("Sorted dict : ",d1)

# Python dictionary with keys having multiple inputs
d1 = {}
d1[(1,2,3)]=[10,20,30]
print(d1)

# Python program to find the sum of all items in a dictionary
# Input : {‘a’: 100, ‘b’:200, ‘c’:300}
# Output : 600

d1 = {'a': 100, 'b':200, 'c':300}
sum = 0
for i in d1:
    sum += d1[i]
print("Total : ",sum)

# ======================using values()====================
d1 = {'a': 100, 'b':200, 'c':300}
sum = 0
l1 = d1.values()
for i in l1:
    sum+=i
print("Total :",sum)

# Python – Group Similar items to Dictionary Values List
'''
Input : test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
Output : {4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]}
Explanation : Similar items grouped together on occurrences.
'''
test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
s1 = set(test_list)
d1 = {n:[i for i in test_list if i==n] for n in s1}
print("Result : ",d1)

d1 = {'name':'Harshal','age':21,'course':'python'}
print(d1.popitem()) # return key:value in tuple
print(d1)
# print(d1.pop('course')) # it only return value of that key
# it also gives error if not not exist
# print(d1)
del d1['age'] # if key not exist then keyerror
print(d1)