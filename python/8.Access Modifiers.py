"""
1. Create a class with PRIVATE fields, private method and a main method.
Print the fields in main method.
Call the private method in main method.
Create a sub class and try to access the private fields and
methods from sub class.

2. Create a class with PROTECTED fields and methods.
Access these fields and methods from any other class in the same package.

Also, Access the PROTECTED fields and methods from
child class located in a different package


3. Create a class with PUBLIC fields and methods.

Access the public methods and fields from any
class in the same package or different package.

"""

class public_type():
    def __init__(self):
        self.public_field="public field is printed"

    def public_method(self):
        print("public method is called")

class a():
    def access_public(self):
        obj=public_type()
        print(obj.public_field)
        obj.public_method()

call=a()
call.access_public()


class protected_type():
    def __init__(self):
        self._protectedfield="protected field is called"

    def _protected_method(self):
        print("protected method is called")

class b():
    def access_protected(self):
        obj2=protected_type()
        print(obj2._protectedfield)
        obj2._protected_method()

call2=b()
call2.access_protected()
        
class private_type():
    def __init__(self):
        self.__privatefield="private field is called"

    def __private_method(self):
        print("private method is called")

    def main(self):
        obj3=private_type()
        print(obj3.__privatefield)
        obj3.__private_method()

class C(private_type):
    def access_protected(self):
        try:
            print(self.__privatefield)
        except AttributeError:
            print("cannot access private member AttributeError is generated")

        try:
            self.__private_method()
        except AttributeError:
            print("cannot access private member AttributeError is generated")

call3=C()
call3.access_protected()
