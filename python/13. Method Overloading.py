"""
1. Write two methods with the same name but different number of parameters
of same type and call the methods

2. Write two methods with the same name but different number of parameters
of different data type and call the methods

3. Write two methods with the same name and same number of parameters of
same type

"""
"""
Python does not support method overloading due to its ynamic typing
and the way it handles arguments. but we can mak the functionality of method
overloading possible by using Variable-length arguments
"""
class overload:
    def add(self,a=int,b=int,c= None):
        if c == None:
            print("the sum of 2 numbers is :",a+b)
        else:
            print("the sum of 3 numbers is:",a+b+c)

call1=overload()
call1.add(2,3)
call1.add(2,3,4)

class Example:
    def calculate(self, a, b):
        print(f"Sum: {a + b}")


obj = Example()
obj.calculate(10, 20)

