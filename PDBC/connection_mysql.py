import mysql.connector

# steps:
# 1. Estabilish connection to database (creating sessions)
# mysql.connector.connect(database,user,password,host,port)
# database = name of database
# user = username of user
# password = password of database
# host = ip-address or hostname
# port = portno of database server

# connect() : returns connection with database

# connection = mysql.connect(database='harshalk',user='root',password='h@rshmysql')
# print('Connection Established',connection)
# cursor_obj = connection.cursor()
# print(cursor_obj)
# connection.close()

# methods of cursor object 
# 1. execute()--method of cursore object used to send sql commands to database
# syntax : cursor_obj.execute(query,parameters=None)
# 1.static sql statements -- before compilation
# 2.dynamic sql statements -- after compilation
# 2. executemany()

#inserting

# connection = mysql.connector.connect(database='harshalk',user='root',password='h@rshmysql')
# cur = connection.cursor()
# print("Connected Successfully.")
# query = "insert into Emp values(1,'Harshal','Python Developer',65000)"
# cur.execute(query)
# print("Employe added.")
# connection.commit()
# connection.close()


# connection = mysql.connector.connect(database='harshalk',user='root',password='h@rshmysql')
# cur = connection.cursor()
# print("Connected Successfully.")
# while True:
#     eno = input("Enter emp_no :")
#     ename = input("Enter emp_name :")
#     ejob = input("Enter emp_job :")
#     esal = input("Enter emp_salary :")
#     query = "insert into Emp values(%s,%s,%s,%s)"
#     cur.execute(query,params=(eno,ename,ejob,esal))
#     print("Employe added.")
#     connection.commit()
#     inp = input("You want to add Emp : ")
#     if inp.lower()=='no':
#         break
# connection.close()


# update employe

# connection = mysql.connector.connect(database='harshalk',user='root',password='h@rshmysql')
# print("Connected successfully.")
# cur = connection.cursor()
# empno = input("Enter emp number :")
# empsal = input("Enter emp salary :")
# query = "Update Emp set salary = (salary+%s) where emp_no = %s"
# cur.execute(query,params=(empsal,empno))
# row = cur.rowcount
# if row>0:
#     print("Salary Updated.")
#     connection.commit()
# else:
#     print("Invalid employee")
# connection.close()

#delete

# connection = mysql.connector.connect(database='harshalk',user='root',password='h@rshmysql')
# print("Connection Established.")
# cur = connection.cursor()
# eno = input("Enter emp number :")
# query = "Delete from Emp where emp_no = %s"
# cur.execute(query,params=(eno,))
# row = cur.rowcount
# if row>0:
#     print("Employee Deleted.")
#     connection.commit()
# else:
#     print("Employee Already Deleted")
# connection.close()


# reading 

connection = mysql.connector.connect(database='harshalk',user='root',password='h@rshmysql')
print("Connection Established.")
cur = connection.cursor()
query = "select * from Emp"
cur.execute(query)
result = cur.fetchall()
print(result)
for row in result:
    print(row)
connection.close()

print("==================================================================")
connection = mysql.connector.connect(database='harshalk',user='root',password='h@rshmysql')
print("Connection Established.")
cur = connection.cursor()
query = "select * from Emp where emp_no=1"
cur.execute(query)
result = cur.fetchone()
for row in result:
    print(row)
connection.close()


print("==================================================================")
connection = mysql.connector.connect(database='harshalk',user='root',password='h@rshmysql')
print("Connection Established.")
cur = connection.cursor()
query = "select * from Emp"
cur.execute(query)
result = cur.fetchmany(2)
print(result)
for row in result:
    print(row)
connection.close()


print("===================================================")
connection = mysql.connector.connect(database='harshalk',user='root',password='h@rshmysql')
print("Connection Established..!")
cur = connection.cursor()
query = "Select * from Emp"
cur.execute(query)
res = cur.fetchall()
for row in res:
    print(row)
connection.close()