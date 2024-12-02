# Abstract class
# Abstract class defines set of rules and regulations (OR) abstract class
# define protocol which has to be followed every derived class or sub class.
# Abstract class is collection of abstract methods, non abstract methods and
# variables (Instance variables, class variables)
# Abstract class defines the specifications which have to implemented or
# followed by derived class or sub class.

import abc

class Animal(abc.ABC):
    def __init__(self) -> None:
        print("Animal is created!")
    
    @abc.abstractclassmethod
    def sleep(self):pass

class Dog(Animal):
    def sleep(self):
        print("Dog is sleep at day")

class Cat(Animal):
    def sleep(self):
        print("Cat is sleep at night")

d1 = Dog()
c1 = Cat()
d1.sleep()
c1.sleep()


class Debitcard(abc.ABC):
    @abc.abstractclassmethod
    def withdraw(self):pass

class SBIdebitcard(Debitcard):
    def withdraw(self):
        print("it is SBI debit card")

class HDFCdebitcard(Debitcard):
    def withdraw(self):
        print("it is HDFC debit card")

class ATM:
    def insert(self,card):
        card.withdraw()

card1 = SBIdebitcard()
card2 = HDFCdebitcard()
atm = ATM()
atm.insert(card1)
atm.insert(card2)


class sim(abc.ABC):
    @abc.abstractclassmethod
    def connect(self):pass

class Jio(sim):
    def connect(self):
        print("Connected Successfully to JIO sim")

class Airtel(sim):
    def connect(self):
        print("Connected Successfully to AIRTEl sim")

class Mobile:
    def insertsim(self,sim):
        sim.connect()

j1 = Jio()
a1 = Airtel()
m1 = Mobile()
m1.insertsim(a1)
m1.insertsim(j1)


