# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 08:23:40 2023

@author: Ashish Chincholikar

"""

#file handling
""" open method in file handling takes one argument
that is the name of the file to be opened """
with open("test.txt") as obj:
    contents = obj.read()

print(contents)

# in order to remove the extra lines at the end of the file to be read
# rstrip() method removes strips or any whitespaces 
with open("test.txt") as obj:
    contents = obj.read()

print(contents.rstrip())

# relative path only consist of the file name that is to be worked upon
#absolute path consist the entire path of that file 
# ex : "c:/1-python/test.txt" 
#accessing the file using absolute path

fpath = "c:/1-python/test.txt"
with open(fpath) as obj:
    contents = obj.read()

print(contents.rstrip())

obj = open("test.txt" , "r")
contents = obj.read()
print(contents.rstrip())

#read the contents of the file line by line

with open("test.txt") as obj:
    for line in obj:
        #contents = obj.read()
        print(line)
"""This is my test file

this is my second line

this is my third line """
#remove the whitespaces using rstrip

with open("test.txt") as obj:
    for line in obj:
        print(line.rstrip())
        
#readlines() method takes each line from the file and
# stores it in a list 

with open("test.txt") as obj:
    lines = obj.readlines()

for line in lines:
    print(line.rstrip())
    
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 08:32:37 2023

@author: Ashish Chincholikar
"""
""" file handling in python
their are 3 modes in python for performing operations 
related to the file    
1 . read mode (r)
used when we want to read the contents from the file
the file must be present from which we want to read

2. write mode(w)
used to write data into the file 
if the mentioned file is not present then it creates 
a new file with that mentioned name
write() function truncates the data from the file
and then starts to write

3.append mode(a)
the append mode does not truncates the contents of the 
file but continues to write from the end of the file
if the file is not created then it creates a new file 
"""
file_name = 'test.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
    string = ''
    
    for line in lines:
        string += line.rstrip()
        print(len(string))
    print(string)
        
#writing the data into the file using write() function

f1 = open("test.txt" , 'w')
f1.write("This is my test file \n")
string = input("enter the data you want in the file")
f1.write(string + "\n")
f1.close()
f2 = open("test.txt" , 'r')
contents = f2.read()
print(contents)

""" -------------------------------------------------"""
f1 = open("test.txt" , 'w')
f1.write("This is my test file")
f1.write("My name is Ashish")
f1.close()
f2 = open("test.txt" , 'r')
contents = f2.read()
print(contents)
#_____________________________________________________
f1 = open("test.txt" , 'w')
f1.write("This is my test file \n")
f1.write("My name is Ashish \n")
f1.close()
f2 = open("test.txt" , 'r')
contents = f2.read()
print(contents)
#------------------------------------------------------

f1 = open("test.txt" , 'a')
f1.write("This is my test file \n")
f1.write("My name is Ashish \n")
f1.close()
f2 = open("test.txt" , 'r')
contents = f2.read()
print(contents)
f2.close()


    
