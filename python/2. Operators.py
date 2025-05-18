"""
1. Write a function for arithmetic operators(+,-,*,/)
2. Write a method for increment and decrement operators(++, --)
3. Write a program to find the two numbers equal or not.
4. Program for relational operators (<,<==, >, >==)
5. Print the smaller and larger number

"""
#1. Write a function for arithmetic operators(+,-,*,/)

def arithmetic_operations(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division: Cannot divide by zero")

arithmetic_operations(20, 2)

#2. Write a method for increment and decrement operators(++, --)

def increment_decrement(x):
    print("Original:", x)
    x += 1  # Increment
    print("After increment:", x)
    x -= 1  # Decrement
    print("After two decrements:", x)


increment_decrement(8)

#3. Write a program to find the two numbers equal or not.
def equal(a, b):
    if a == b:
        print("The numbers are equal.")
    else:
        print("The numbers are not equal.")

equal(10, 10)
equal(10, 5)

#4. Program for relational operators (<,<==, >, >==)

def relational_operators(a, b):
    print(f"{a} < {b}:", a < b)
    print(f"{a} <= {b}:", a <= b)
    print(f"{a} > {b}:", a > b)
    print(f"{a} >= {b}:", a >= b)

relational_operators(11, 8)

#5. Print the smaller and larger number

def smaller_larger(a, b):
    if a < b:
        smaller = a
    else:
        smaller = b
    if a > b:
        larger = a
    else:
        larger = b
        
    print("Smaller number:", smaller)
    print("Larger number:", larger)

smaller_larger(15, 25)





