"""
1. Write a program to generate Arithmetic
Exception without exception handling
2. Handle the Arithmetic exception using try-catch block
3. Write a method which throws exception,
Call that method in main class without try block
4. Write a program with multiple catch blocks
5. Write a program to throw exception with your own message
6. Write a program to create your own exception
7. Write a program with finally block
8. Write a program to generate Arithmetic Exception
9. Write a program to generate FileNotFoundException
10. Write a program to generate ClassNotFoundException
11. Write a program to generate IOException
12. Write a program to generate NoSuchFieldException
"""
#1. Write a program to generate Arithmetic Exception without exception handling
a = 10
b = 0
c = a / b  # Raises ZeroDivisionError
print(c)

#2. Handle the Arithmetic exception using try-catch block
try:
    a = 10
    b = 0
    c = a / b
except ZeroDivisionError:
    print("Caught an arithmetic exception")

#3. Write a method which throws exception, Call that method in main class without try block

def raise_exception():
    raise ArithmeticError("Manual Arithmetic Error")

raise_exception()


#4. Write a program with multiple catch blocks

try:
    x = int("abc")  # ValueError
    y = 10 / 0      # ZeroDivisionError
except ValueError:
    print("ValueError occurred")
except ZeroDivisionError:
    print("ZeroDivisionError occurred")
except Exception:
    print("General Exception:")

#5. Write a program to throw exception with your own message

try:
    raise Exception("This is my custom error message")
except Exception as e:
    print("Exception caught:", e)

#6. Write a program to create your own exception

class MyCustomError(Exception):
    pass

def check_value(val):
    if val < 0:
        raise MyCustomError("Negative values are not allowed")

try:
    check_value(-5)
except MyCustomError as e:
    print("Caught custom exception:", e)

#7. Write a program with finally block
try:
    a = 10 / 0
except ZeroDivisionError:
    print("Handled division by zero")
finally:
    print("This is the finally block. Always executes.")

#8. Write a program to generate Arithmetic Exception
a = 5
b = 0
print(a / b)  # ZeroDivisionError


#9. Write a program to generate FileNotFoundException

with open("nonexistent_file.txt", "r") as f:
    content = f.read()

#11. Write a program to generate IOException
try:
    with open("readonly_file.txt", "w") as f:
        f.write("Test")  # If the file is read-only or locked, IOError may occur
except IOError as e:
    print("IOError occurred:", e)









