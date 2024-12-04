# JSON stands for Java Script Object Notation
# JSON is a text file
# JSON is format is used to exchange data in web application development.

# json module provides the following methods
# 1. dump()
# 2. load()
# 3. dumps()
# 4. loads()

# 1.dumps() : This function return json formatted string. This method does not allows to writing inside file

import json
students = {
    'sno':[1,2,3,4,5],
    'sname':["Harshal","Sagar","Aniket","Kunal","Prathamesh"],
    'smakrs':[250,340,360,480,230]
}
print(students,type(students))

s = json.dumps(students)
print(s,type(s))

# loads() : This function converts json string into python object type

students = {
    'sno':[1,2,3,4,5],
    'sname':["Harshal","Sagar","Aniket","Kunal","Prathamesh"],
    'smakrs':[250,340,360,480,230]
}
print(students,type(students))

s = json.dumps(students)
print("Dict to Json ",s,type(s))

dic = json.loads(s)
print("Json to dict ",dic,type(dic))


# dump() : This function convert object into json string and write inside file

students = {
    'sno':[1,2,3,4,5],
    'sname':["Harshal","Sagar","Aniket","Kunal","Prathamesh"],
    'smakrs':[250,340,360,480,230]
}
with open("file.json","w") as fileobj:
    json.dump(students,fileobj)
fileobj.close()


# load() : This function read json string from json file and return python object.
# Syntax: load(fobj)

with open("file.json","r") as fileobj:
    data = json.load(fileobj)
    
    for key,val in data.items():
        print(f"{key} --> {val}")
fileobj.close()
