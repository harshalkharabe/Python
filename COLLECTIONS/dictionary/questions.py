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