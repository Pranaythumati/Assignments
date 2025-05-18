"""
1. Different ways creating a string
2. Concatenating two strings using + operator
3. Finding the length of the string
4. Extract a string using Substring
5. Searching in strings using index()
6. Matching a String Against a Regular Expression With matches()
7. Comparing strings
8. startsWith(), endsWith() and compareTo()
9. Trimming strings with strip()
10. Replacing characters in strings with replace()
11. Splitting strings with split()
12. Converting integer objects to Strings
13. Converting to uppercase and lowercase
"""
#1. Different ways creating a string

str1 = "Hello"
str2 = 'World'
str3 = """Triple quoted string"""
str4 = str("Using str constructor")


print(str1, str2, str3, str4)

#2. Concatenating two strings using + operator

a = "Hello"
b = "World"
c = a + " " + b
print("Concatenated String", c)


#3. Finding the length of the string

s = "Python"
print("Length:", len(s))

#4. Extract a string using Substring

s = "HelloWorld"
print("Substring (0 to 5):", s[0:5])


#5. Searching in strings using index()
s = "Hello World"
print("Index of 'World':", s.index("World"))
print("Index of 'r':", s.index("r"))


#6. Matching a String Against a Regular Expression With matches()
import re

pattern = r"Hella-z]+$"  # Only letters
s = "HelloWorld"
if re.match(pattern, s):
    print("Matches the pattern")
else:
    print("Does not match")



#7. Comparing strings

a = "hello"
b = "Hello"
print("a == b:", a == b)
print("a != b:", a != b)


#8. startsWith(), endsWith() and compareTo()

s = "HelloWorld"
print("Starts with 'Hello':", s.startswith("Hello"))
print("Ends with 'World':", s.endswith("World"))


#9. Trimming strings with strip()

s = "   Hello World   "
print("Trimmed string:", s.strip())


#10. Replacing characters in strings with replace()

s = "banana"
print("Replace 'a' with '@':", s.replace("a", "@"))

#11. Splitting strings with split()

s = "apple,banana,grape"
fruits = s.split(",")
print("Split list:", fruits)


#12. Converting integer objects to Strings

num = 123
s = str(num)
print("Converted string:", s, type(s))

#13. Converting to uppercase and lowercase

s = "Python"
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())










