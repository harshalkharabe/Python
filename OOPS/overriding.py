class student:
    def __init__(self,r,n) -> None:
        self.rollno = r
        self.name = n
    
    def __str__(self) -> str:
        return f"Roll number : {self.rollno} Name : {self.name}"

st1 = student(12,"Prathamesh")
print(st1)