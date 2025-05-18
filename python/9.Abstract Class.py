"""
1. Create an abstract class with abstract and non-abstract methods.

2. Create a sub class for an abstract class.
Create an object in the child class for the
abstract class and access the non-abstract methods

3. Create an instance for the child class in child class
and call abstract methods

4. Create an instance for the child class in child class
and call non-abstract methods
"""

from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def non_abstract_method(self):
        print("This is a non-abstract method in abstract class.")

    @abstractmethod
    def abstract_method(self):
        pass
    
class SubClass(AbstractClass):
    def abstract_method(self):
        print("Implementation of abstract method in subclass.")

obj = SubClass()
obj.non_abstract_method()

class Child:
    def __init__(self):
        obj = SubClass()
        obj.abstract_method()
        
child_obj = Child()

class Child2:
    def __init__(self):
        obj = SubClass()
        obj.non_abstract_method()
        
child2_obj = Child2()





