class student:
    def __init__(self,n,a) -> None:
        self.name = n
        self.age = a
    
    def print_data(self):
        print(f"Name of student : {self.name}")
        print(f"Age of student : {self.age}")

s1 = student("Harshal",20)
s2 = student("Aniket",21)

s1.print_data()
s2.print_data()