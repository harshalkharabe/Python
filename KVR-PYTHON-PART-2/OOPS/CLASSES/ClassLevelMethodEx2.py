#ClassLevelMethodEx2.py
class Employee:
    @classmethod
    def getcompname(cls):# Class Level Method Name
        cls.compname="IBM" # OR Employee.compname="IBM"
        # Here compname is called Class Level Data Member
    @classmethod
    def getcity(cls):  # Class Level Method Name
        cls.city="HYD"   # Employee.city="HYD"
        #Here city is called Class Level Data Member

#Main Program
Employee.getcompname()
Employee.getcity()
print("Comp Name=",Employee.compname) # Accessing Class Level Data Members w.r.t Class Name
print("Comp Located City=",Employee.city) # Accessing Class Level Data Members w.r.t Class Name
print("------------------------------------------")