class Matrix:
    def __init__(self) -> None:
        self.matrix=[]
    
    def readmatrix(self):
        for i in range(2):
            row = []
            for j in range(2):
                val = int(input("Enter val :"))
                row.append(val)
            self.matrix.append(row)
    
    def printmatrix(self):
        for i in self.matrix:
            for j in i:
                print(j,end=' ')
            print()
    
    def __add__(self,other):
        temp = Matrix()
        for i in range(2):
            row = []
            for j in range(2):
                row.append(self.matrix[i][j]+other.matrix[i][j])
            temp.matrix.append(row)
        return temp
# m1 = Matrix()
# m2 = Matrix()
# print("Enter values for m1")
# m1.readmatrix()
# print("Enter values for m2")
# m2.readmatrix()
# print("Values of m1")
# m1.printmatrix()
# print("Values of m2")
# m2.printmatrix()

# m3 = m1+m2
# m3.printmatrix()


class players:
    def __init__(self) -> None:
        self.name = None
        self.score = None
    
    def readplayer(self):
        self.name = input("Enter name :")
        self.score = input("Enter score :")
    
    def printplayer(self):
        print(f"Name : {self.name}")
        print(f"Score : {self.score}")
    
    def __eq__(self, other) -> bool:
        if self.score==other.score:
            return True
        return False

# p1 = players()
# p2 = players()
# p1.readplayer()
# p2.readplayer()
# p1.printplayer()
# p2.printplayer()
# isequal = p1==p2
# print(f"Both players score are equal : {isequal}")



class A:
    def __init__(self) -> None:
        self.num1 = None
    
    def read(self):
        self.num1=int(input("Enter value :"))
    
    def info(self):
        return self.num1

    def __sub__(self,other):
        result = A()
        result.num1 = self.num1 - other.num1
        return result

a1 = A()
b1 = A()
a1.read()
b1=A()
b1.read()
c1 = a1-b1
print(b1.info())
print(a1.info())
print("Addition of a1-b1 :",c1.info())


class Floor:
    def __init__(self) -> None:
        self.num = None
    def read(self):
        self.num = int(input("Enter val :"))
    def __floordiv__(self,other):
        f3 = Floor()
        f3.num = self.num//other.num
        return f3.num

f1 = Floor()
f2 = Floor()
f1.read()
f2.read()
print("Floor division of these :",f1//f2)