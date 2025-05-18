"""
1. Write a class with a default constructor, one argument constructor
and two argument constructors. Instantiate the class to call
all the constructors of that class from a main class
2. Call the constructors(both default and argument constructors) of super class from a child class
3. Apply private, public, protected and default access modifiers
to the constructor
4. Write a program which illustrates the concept of attributes of a constructor.

"""
class MyClass:
    def __init__(self, a=None, b=None):
        if a is None and b is None:
            print("Default constructor called")
        elif b is None:
            print("One-argument constructor called with a")
        else:
            print("Two-argument constructor called with a , b")


obj1 = MyClass()           # Default constructor
obj2 = MyClass(10)         # One-argument constructor
obj3 = MyClass(10, 20)     # Two-argument constructor

class SuperClass:
    def __init__(self):
        print("SuperClass Default Constructor")

    def __init__(self, a=None):
        if a:
            print("SuperClass Arg Constructor with a")
        else:
            print("SuperClass Default Constructor")

class SubClass(SuperClass):
    def __init__(self):
        super().__init__()  # Call superclass constructor
        print("SubClass Constructor")


s1 = SubClass()
s2 = SuperClass(100)

class AccessModifiers:

    def __init__(self):  
        print("Public constructor")

    def _protected_constructor(self):  
        print("Protected constructor")

    def __private_constructor(self):  
        print("Private constructor")


obj = AccessModifiers()
obj._protected_constructor()
obj._AccessModifiers__private_constructor()

class Student:
    def __init__(self, name, age):
        self.name = name    # attribute of constructor
        self.age = age      # attribute of constructor

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


s1 = Student("Pranay", 21)
s1.display()


