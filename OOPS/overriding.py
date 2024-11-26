# class Employee:
#     def __init__(self) -> None:
#         self.ename=None
#     def read(self):
#         self.ename = input("Enter employee name :")
#     def get(self):
#         print(f"Employee Name : {self.ename}")
# class SalariedEmp(Employee):
#     def __init__(self) -> None:
#         super().__init__()
#         self.salary = None
#     def read(self):
#         super().read()
#         self.salary=int(input("Enter salary :"))
#     def get(self):
#         super().get()
#         print(f"Employee Salary : {self.salary}")
# s1 = SalariedEmp()
# s1.read()
# s1.get()

# class student:
#     def __init__(self,r,n) -> None:
#         self.rollno = r
#         self.name = n
    
#     def __str__(self) -> str:
#         return f"Roll number : {self.rollno} Name : {self.name}"

# st1 = student(12,"Prathamesh")
# print(st1)

# class student:
#     def __new__(cls,*args, **kwargs):
#         obj = super().__new__(student)
#         return obj # return reference of object
#     def __init__(self) -> None:
#         print("Object created!!")

# s1 = student()
# print(s1)
# we can create any number of object we want

class Student:
    c=0
    def __new__(cls,*args, **kwargs):
        if Student.c==0:
            obj = super().__new__(Student)
            Student.c+=1
            return obj
        else:
            return None
    def __init__(self) -> None:
        print("Created object")

s1 = Student()
s2 = Student()
s3 = Student()
print(s1)
print(s2)
print(s3)