#File
# Every application required persistence or storing data permanently. The
# data can saved or stored permanently using two system
# 1. File system
# 2. Database system

# Basic steps to work with files
# 1. Open file
# 2. Read/Write
# 3. Close file

# Creating text file

# Writing data inside text file
# 1. write() method of file object
# 2. print() function

# fileobject = open('text.txt','w')
# fileobject.write("Hello I an Harshal Kharabe ")
# fileobject.write("I am from akola maharastra ")
# fileobject.write("Currently i am pursing my bachloer's degeree in computer application ")
# fileobject.write("Thank you! sir.")
# fileobject.close()


# fileobject = open('text1.txt','w')
# print("Thank you sir. for giving me these oportunity to express myself.",file=fileobject)
# print("My name is Harshal Vijay Kharabe.",file=fileobject)
# print("I am from akola maharastra",file=fileobject)
# print("Currently i persuing my bachleor's degree in computer application",file=fileobject)
# print('My technical skills are :',file=fileobject)
# print('Frontend : HTML CSS and Basic JS',file=fileobject)
# print('Backend : Storng command on Pyhton, NUmpy, Pandas, Django, FasAPI',file=fileobject)
# print('Databases : MySQL, PostgreSQL, Oracle',file=fileobject)
# print('Thank you! sir.',file=fileobject)
# fileobject.close()


# # Creating text file to store student marks details

# fileobject = open("text2.txt","w")
# while True:
#     roll_no = int(input("Enter roll number of student :"))
#     name = input("Enter name of student :")
#     backend_marks = int(input("Enter Backend marks :"))
#     frontend_marks = int(input("Enter Backend marks :"))
#     avg = (total := backend_marks+frontend_marks)/2
#     print(roll_no,name,backend_marks,frontend_marks,total,avg,file=fileobject)
#     ans = input("Do you want to add student : Yes/No :")
#     if ans.lower()=="no":
#         break

# fileobject.close()


# #Program for Writing the Data to the File----write()
# with open('text3.txt','a') as fobj:
#     fobj.write(str(101))
#     fobj.write("\tHarshal Kharabe")
#     fobj.write("\t"+str(77.89))
# fobj.close()

# #Program for Writing the Data to the File----writelines()
# data = {
#     10:"Python",
#     20:"java",
#     30:"DSA"
# }
# with open('text4.txt','a') as fobj:
#     fobj.writelines(str(data)+"\n")

#Program for Copying the Content of One File into Another File
def copyfile():
    try:
        fname = input("Enter file name :")
        with open(fname,'r') as sourcefile:
            copy_fname = input("Enter file name :")
            with open(copy_fname,'a') as targetfile:
                data = sourcefile.read()
                targetfile.write(data)
                print("Data copy successfully")
            targetfile.close()
        sourcefile.close()
    except FileNotFoundError:
        print("File Not Found.")

copyfile()