"""
1. Write a program to print “Bright IT Career” ten times using for loop
2. Write a java program to print 1 to 20 numbers using the while loop.
3. Program to equal operator and not equal operators
4. Write a program to print the odd and even numbers.
5. Write a program to print largest number among three numbers.
6. Write a program to print even number between 10 and 20 using while
7. Write a program to print 1 to 10 using the do-while loop statement.
8. Write a program to find Armstrong number or not
9. Write a program to find the prime or not.
10. Write a program to palindrome or not.
11. Program to check whether a number is EVEN or ODD using switch
12. Print gender (Male/Female) program according to given M/F using switch
"""

#1. Write a program to print “Bright IT Career” ten times using for loop

for i in range(10):
    print("Bright IT Career")

#2. Write a program to print 1 to 20 numbers using the while loop.

a=0
while (a < 21):
    print(a)
    a+=1
    
#3. Program to equal operator and not equal operators

a = 10
b = 20
print("For equal operator", a == b)
print("For not equal operator", a != b)

#4. Write a program to print the odd and even numbers.

x=int(input("Enter the number upto which you want to calculate"))
for i in range(1, x+1):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")

#or

x= int(input("Enter the number"))
if x % 2 == 0:
    print(i, "is Even")
else:
    print(i, "is Odd")

#5. Write a program to print largest number among three numbers.

a = int(input("Enter number1"))
b = int(input("Enter number2"))
c = int(input("Enter number3"))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

#6. Write a program to print even number between 10 and 20 using while

i = 10
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

#7. Write a program to print 1 to 10 using the do-while loop statement.

i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break

#8. Write a program to find Armstrong number or not

num = int(input("enter number"))
summ = 0
temp= str(num)
for i in range(0,len(temp)):
    summ+=(int(temp[i]))**len(temp)
if num == summ:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


#9. Write a program to find the prime or not.

num = int(input("Enter number"))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

#10. Write a program to palindrome or not.

text=input("enter text")
text=str(text)
rev=text[::-1]
if text == rev:
    print("palindrome")
else:
    print("not a palindrome")

#11. Program to check whether a number is EVEN or ODD using switch

def even_odd(n):
    match n % 2:
        case 0:
            print("Even")
        case 1:
            print("Odd")

even_odd_switch(7)


#12. Print gender (Male/Female) program according to given M/F using switch

def print_gender(ch):
    match ch.upper():
        case 'M':
            print("Male")
        case 'F':
            print("Female")
        case _:
            print("Invalid input")

print_gender('F')

