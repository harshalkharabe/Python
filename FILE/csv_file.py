# CSV stands for Comma Separated Values
# The so-called CSV (Comma Separated Values) format is the most common
# import and export format for spreadsheets and databases. 
# CSV standard, which is used to exchange data between two different
# applications.
# To work with csv files, python provides a predefined module “csv”.

# syntax : csv.writer(csvfile)

import csv

# fileobj = open('csv_file.csv','w',newline='')
# csvobj = csv.writer(fileobj)
# while True:
#     roll_no = int(input("Enter roll number :"))
#     name = input("Enter name :")
#     course = input("Enter course name :")
#     info = [roll_no,name,course]
#     csvobj.writerow(info)
#     ans = input("Do you want to add student :")
#     if ans.lower() == "no":
#         break
# fileobj.close()

# write a program to read data from marks.csv
fileobj = open('csv_file.csv','r')
csvobj = csv.reader(fileobj)
students = list(csvobj)
for stud in students:
    print(stud)
fileobj.close()

# syntax : csv.DictWriter(f, fieldname=None)

# fileobj = open('sales.csv','w',newline='')
# csvobj = csv.DictWriter(fileobj,fieldnames=['id','name','salary'])
# csvobj.writeheader()
# while True:
#     id = int(input("Enter id : "))
#     name = (input("Enter name : "))
#     salary = (input("Enter salary : "))
#     data = {
#         'id':id,
#         'name':name,
#         'salary':salary
#     }
#     csvobj.writerow(data)
#     ans = input("Do you want to add :")
#     if ans.lower()=="no":
#         break
# fileobj.close()

# Syntax : csv.DictReader(f, fieldnames=None)

fileobj = open('sales.csv','r')
csvobj = csv.DictReader(fileobj)
for row in csvobj:
    print(row)
fileobj.close()

