""""
1. Create a Dictionary with at least
5 key value pairs of the Student ID and Name
1.1. Adding the values in dictionary
1.2. Updating the values in dictionary
1.3. Accessing the value in dictionary
1.4. Create a nested loop dictionary
1.5. Access the values of nested loop dictionary
1.6. Print the keys present in a particular dictionary
1.7. Delete a value from a dictionary
"""

student = {'Pranay':'21951a04e0','Rahul':'21951a04e5','Sahit':'21951a04f8',
           'Manda':'21951a04e6', 'cr':'21951a04d9'}

student['prateek']='21951a04e1'

student['sahit']='21951a04f6'

print(student['cr'])

n_student = {1:{'name':'Pranay','age':22},
             2:{'name':'rohan','age':23},
             3:{'name':'anil','age':21}}

print(n_student)

print(student.keys())

del student['sahit']

print(student)
