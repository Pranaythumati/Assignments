"""
A, B and C are classes
A is a super class. B is a sub class of A. C is a sub class of B.
Create three methods in each class,
2 methods are specific to each class and
third method (override method) should be in all three Classes A, B and C

Create a class with main method.
Create an object for each class A, B and C in main method and
call every method of each class using its own object/instance.

Call an overridden method with super class reference to B and C class’s objects
Runtime Polymorphism with Data Members/Instance variables, Repeat the above process only for data members
"""

class A():
    def methodA1(self):
        print("methodA1")
    def methodA2(self):
        print("methodA2")
    def method3(self):
        print("common method of A")

class B(A):
    def methodB1(self):
        print("methodB1")
    def methodB2(self):
        print("methodB2")
    def method3(self):
        print("common method of B")

class C(B):
    def methodC1(self):
        print("methodC1")
    def methodC2(self):
        print("methodC2")
    def method3(self):
        print("common method of C")

class main():
    print("object A")
    ObjA= A()
    ObjA.methodA1()
    ObjA.methodA2()
    ObjA.method3()

    print("object B")
    ObjB= B()
    ObjB.methodB1()
    ObjB.methodB2()
    ObjB.method3()

    print("object C")
    ObjC= C()
    ObjC.methodC1()
    ObjC.methodC2()
    ObjC.method3()

    print("calling an overridden method")
    ref = B()
    ref.method3()

    ref = C()
    ref.method3()

    
main()   
    
