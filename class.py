"""class Animal:
    def speak(self):
        print("Animal Speaking")
class Dog(Animal):
    def bark(self):
        print("dog barking")
class DogChild(Dog):
    def eat(self):
        print("Eating bread...")
d= DogChild()
d.bark()
d.speak()
d.eat()"""
'''class Calculation1:
    def Summation(self,a,b):
        return a+b;
class Calculation2:
    def Multiplication(self,a,b):
        return a-b;
class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b;
d=Derived()
print(d.Summation(10,20))
print(d.Multiplication(10,20))
print(d.Divide(10,20))'''
class Compute:
    def area(self,x=None,y=None):
        if x!=None and y!=None:
            return x*y
        elif x!=None:
            return x*x
        else:
            return 0
obj=Compute()
obj.area()
obj.area(6)
obj.area(2,8)
