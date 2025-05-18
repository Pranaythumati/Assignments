"""
1. Write a program to read text file
2. Write a program to write text to .txt file using InputStream
3. Write a program to read a file stream
4. Write a program to read a file stream supports random access
5. Write a program to read a file a just to a particular index using seek()
6. Write a program to check whether a file is having read access
and write access permissions
"""
#1. Write a program to read text file
def read_text_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)


read_text_file('test.txt')

#2. Write a program to write text to .txt file using InputStream
def write_text_file(filename):
    text = input("Enter text to write into the file: ")
    with open(filename, 'w') as file:
        file.write(text)
    print("Text written successfully.")


write_text_file('test.txt')

#3. Write a program to read a file stream
def read_file_stream(filename):
    with open(filename, 'rb') as file:
        byte = file.read(1)
        while byte:
            print(byte.decode(errors='ignore'), end='')
            byte = file.read(1)


read_file_stream('test.txt')

#4. Write a program to read a file stream supports random access

def random_access_read(filename):
    with open(filename, 'rb') as file:
        file.seek(5)  # Move to 5th byte
        print("From byte 5:", file.read(10).decode(errors='ignore'))  # Read next 10 bytes


random_access_read('test.txt')

#5. Write a program to read a file a just to a particular index using seek()


def seek_and_read(filename, index):
    with open(filename, 'r') as file:
        file.seek(index)
        data = file.read(10)
        print(f"Data from index {index}:", data)


seek_and_read('test.txt', 5)

#6. Write a program to check whether a file is having read access

import os

def check_permissions(filename):
    print(f"Checking permissions for {filename}")
    print("Readable:", os.access(filename, os.R_OK))
    print("Writable:", os.access(filename, os.W_OK))


check_permissions('test.txt')













