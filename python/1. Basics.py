"""
1. Write a program to print your name.
2. Write a program for a Single line comment and multi-line comments
3. Define variables for different Data Types int, Boolean, char, float, double and print on the Console.
4. Define the local and Global variables with the same name and print both variables and understand the scope of the variables

"""

# Write a program to print your name.

print ("Pranay") 

# Write a program for a Single line comment and multi-line comments.

# Single line comment
"""
Multi-line
comments are written in
this format using Quotes
"""

# Define variables for different Data Types int, Boolean, char, float, double and print on the Console.

a = 9
print("The type of the variable is ", type(a))
b = False
print("The type of the variable is: ", type(b))
c = 7.0
print("The type of the variable is", type(c))
String = 'Hello world'
print("The type of the variable is", type(String))

"""
Define the local and Global variables with the same name and
print both variables and understand the scope of the variables
"""

# Global variable
x = 10

def Scope_function():
    # Local variable with the same name
    x = 5
    print("Local Variable value:", x)

Scope_function()

# Print global variable
print("Global variable value:", x)
