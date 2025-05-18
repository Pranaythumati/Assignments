"""
1. Define a static variable and access that through a class
2. Define a static variable and access that through a instance
3. Define a static variable and change within the instance
4. Define a static variable and change within the class
"""

#1. Define a static variable and access that through a class
class static:
    var = 10
    # Static variable


print(static.var)

#2. Define a static variable and access that through a instance

obj=static()
print(obj.var)

#3. Define a static variable and change within the instance

obj.var=33
print(obj.var)
print(static.var)

#4. Define a static variable and change within the class

static.var=22
print(static.var)
