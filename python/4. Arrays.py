"""
1. Write a function to add integer values of an array
2. Write a function to calculate the average value of an array of integers
3. Write a program to find the index of an array element
4. Write a function to test if array contains a specific value
5. Write a function to remove a specific element from an array
6. Write a function to copy an array to another array
7. Write a function to insert an element at a specific position in the array
8. Write a function to find the minimum and maximum value of an array
9. Write a function to reverse an array of integer values
10. Write a function to find the duplicate values of an array
11. Write a program to find the common values between two arrays
12. Write a method to remove duplicate elements from an array
13. Write a method to find the second largest number in an array
14. Write a method to find the second largest number in an array
15. Write a method to find number of even number and odd numbers in an array
16. Write a function to get the difference of largest and smallest value
17. Write a method to verify if the array contains two specified elements(12,23)
18. Write a program to remove the duplicate elements and return the new array
"""

#1. Write a function to add integer values of an array

def add_integer(arr):
    summ = 0
    for i in range(0, len(arr)):
        summ+=arr[i]
    return summ

a=[1,1,1,1,1,4]
print(add_integer(a))


#2. Write a function to calculate the average value of an array of integers

def avg_int(arr):
    avg= (add_integer(arr) / len(arr))
    return avg

a=[1,2,3,4,5,6]
print(avg_int(a))


#3. Write a program to find the index of an array element

def find_index(arr,element):
    if element in arr:
        return arr.index(element)
    else:
        return False

a=[1,2,3,4,5,6]
print(find_index(a,3))

#4. Write a function to test if array contains a specific value

def find_element(arr, element):
    if element in arr:
        return "Element is present"
    else:
        return "Element is not present"


a=[1,2,3,4,5,6]
print(find_element(a,3))

#5. Write a function to remove a specific element from an array


def remove_element(arr, element):
    if element in arr:
        a.remove(element)
        return arr
    else:
        return "Element is not present"


a=[1,2,3,4,5,6]
print(remove_element(a,3))

#6. Write a function to copy an array to another array

def copy_array(arr):
    x= arr.copy()
    return x

a=[1,2,3,4,5,6]
print(copy_array(a))


#7. Write a function to insert an element at a specific position in the array

def insert_element(arr,position,element,):
    arr.insert(position,element)
    return arr

a=[1,2,3,4,5,6]
print(insert_element(a,3,9))


#8. Write a function to find the minimum and maximum value of an array

def max_min(arr):
    maxi=arr[0]
    mini=arr[0]
    for i in range(0,len(arr)):
        if maxi < arr[i]:
            maxi = arr[i]
        if mini > arr[i]:
            mini = arr[i]
    return maxi,mini

a=[1,2,9,4,5,6]
print(max_min(a))

#9. Write a function to reverse an array of integer values

def rev(arr):
    rev_arr = arr[::-1]
    return rev_arr

a=[1,2,9,4,5,6]
print(rev(a))

#10. Write a function to find the duplicate values of an array

def duplicates(arr):
    arr2=set()
    dup_arr=[]
    for i in arr:
        if i in arr2:
            dup_arr.append(i)
        else:
            arr2.add(i)
    return dup_arr

a=[1,2,9,4,4,2,1,6]
print(duplicates(a))

#11. Write a program to find the common values between two arrays

def common_val(a1,a2):
    return list(set(a1) & set(a2))

#or

def com_val(a1,a2):
    com=[]
    for i in range(0, len(a1)):
        for j in range(0, len(a2)):
            if a1[i]==a2[j]:
                com.append(a[i])
    return list(set(com))

a=[1,2,9,4,4,2,1,6]
b=[2,4,6,7,9]
print(com_val(a,b))

#12. Write a method to remove duplicate elements from an array

def remove_duplicates(arr):
    return list(set(arr))

a=[1,2,9,4,4,2,1,6]
print(remove_duplicates(a))

#13. Write a method to find the second largest number in an array
#14. Write a method to find the second largest number in an array

def second_largest(arr):
    arr=list(set(arr))
    arr.sort()
    return arr[-2]

a=[1,2,9,9,9,4,4,2,1,6]
print(second_largest(a))

#15. Write a method to find number of even number and odd numbers in an array

def count_evnodd(arr):
    even=0
    odd=0
    for i in range(0, len(arr)):
        if i % 2 == 0 and i !=0:
            even +=1
        elif i%2 != 0 and i !=0:
            odd +=1
    return (f"the count of even numbers is {even} and odd numbers is {odd}")

a=[0,1,1,2,9,9,9,4,4,2,1,6]
print(count_evnodd(a))

#16. Write a function to get the difference of largest and smallest value
    
def diff_max_min(arr):
    x=max_min(arr)
    summm=x[0]-x[1]
    return summm

a=[1,1,2,9,9,9,4,4,2,1,6]
print(diff_max_min(a))

#17. Write a method to verify if the array contains two specified elements(12,23)

def specified_val(arr,v1=int,v2=int):
    if v1 in arr and v2 in arr:
        return "values present"
    else:
        return "values not present"
    
a=[1,1,2,9,9,9,4,4,2,1,6]
print(specified_val(a,1,4))

#18. Write a program to remove the duplicate elements and return the new array
def remove_duplicates(arr):
    return list(set(arr))

a=[1,2,9,4,4,2,1,6]
print(remove_duplicates(a))



    
