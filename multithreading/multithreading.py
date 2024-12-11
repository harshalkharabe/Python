# Multitasking applications
# An application which allows performing more than one task simultaneously
# or concurrently is called multitasking applications.

#without using class
import threading
# def even():
#     for i in range(1,21):
#         if i%2==0:
#             print("Even",i)

# def odd():
#     for i in range(1,21):
#         if i%2!=0:
#             print("Odd",i)

# t1 = threading.Thread(target=even)
# t2 = threading.Thread(target=odd)
# t1.start()
# t2.start()



# class Even(threading.Thread):
#     def run(self):
#         for i in range(1,21):
#             if i%2==0:
#                 print("Even",i)

# class Odd(threading.Thread):
#     def run(self):
#         for i in range(1,21):
#             if i%2!=0:
#                 print("Odd",i)

# t1 = Even()
# t2 = Odd()
# t1.start()
# t2.start()


# join() method of thread class

import threading

def fun():
    for i in range(1,11):
        print("Learning Python!!")
    
t1 = threading.Thread(target=fun)
t1.start()
t1.join()
for i in range(1,11):
    print("After python learn Django!!")


total = 0
def calculate_sum():
    global total
    for i in range(1,11):
        total+=i

t1 = threading.Thread(target=calculate_sum)
t1.start()
t1.join()
print(f"Total sum : {total}")

#sleep() method not of Threading class
# sleep is in time class

import time

# def fun():
#     for i in range(1,6):
#         print("Bye")
#         time.sleep(1)

# t1 = threading.Thread(target=fun)
# t1.start()
# for i in range(5):
#     print("Hello")



# concept of revervation system
import threading

class Bus:
    def __init__(self):
        self.__seats = 50
        self.__lock = threading.Lock()
    
    def reserve(self,name,no_of_seat):
        self.__lock.acquire()
        if self.__seats>no_of_seat:
            for i in range(no_of_seat):
                self.__seats-=1
            print(f"{name} your seats are reserved remaining seats are {self.__seats}")
        else:
            print(f"{name} {no_of_seat} seats are not aviable",end=' ')
            print(f"{no_of_seat-self.__seats} seats are aviable")
        self.__lock.release()
    
class BusReservation(threading.Thread):
    def __init__(self,bus,name,ns):
        super().__init__()
        self.__bus = bus
        self.__name = name
        self.__ns = ns

    def run(self):
        self.__bus.reserve(self.__name,self.__ns)

b1 = Bus()
p1 = BusReservation(b1,"Harshal",12)
p2 = BusReservation(b1,"Aniket",112)
p1.start()
p2.start()
