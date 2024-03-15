
#data structures in python
"""list 
     tuple 
     set - does not allow
     dictionary"""    

tup = (4 , 9.45 , "ABCD" , True)
print(tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])

for x in tup:
    print(x)
# for accessing the elements of tuple the size of tuple and the 
# number of elements the range() function provides must be equal
# or else it gives index out of range error
for i in range(0,4):
    print(tup[i] , end = " ")
    
tup2 = ("apple" , "orange" , "apple" , "banana" , "apple" , "orange")
print(len(tup2))
print(tup2.count("apple"))
print(tup2.index("orange"))

if "banana" in tup2:
    print("banana is present in the tuple")
if "mango" not in tup2:
    print("mango is not present in the tuple")
    
#######################################
"""
list data structure
to add elements to the list
1. append() = takes one argument that is to be inserted , element is inserted after the last element of the original list
2. extend() = takes another ds as argument which will be inserted after the original list
3. insert() = takes 2 argument the element to be inserted and the index to which it is to be assigned
concatinate using + operator
"""
lst = [1 , 3.4 , "XYZ" , False]

print(f"lst[0]={lst[0]}")
print(f"lst[1]={lst[1]}")
print(f"lst[2]={lst[2]}")
print(f"lst[3]={lst[3]}")
print(lst[1:3:1])#slicing opertor
print(lst[:])
print(lst[-4:-1])
lst.append(5)#append() function
print(lst)
lst1 = [6,7,8]
lst.extend(lst1)#extend() function
print(lst)
lst.insert(1 , "PQRS")#insert() function requires 2 parameters
# the element to be inserted and the index to which it is to be assigned
print(lst)

#nested list is also possible
ls1 = [1,2,3]
ls2 = ["ABC" , "PQR" , "XYZ"]
ls3 = [3.4 , 9.5 , ls1 , ls2 , True]
print(ls3)
print(ls1+ls2)

""" create a list and find if consequtive duplicate element exists in it"""
ls = [1,2,3,4,5,6,7]
def find_duplicate(ls):
    for i in range(len(ls)-1):
        if(ls[i]==ls[i+1]):
            return True
    return False
    
res = find_duplicate(ls)
print(res)
 
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 08:16:14 2023

@author: Ashish Chincholikar
"""

lst = [1,2,3,4,5,6]
print(lst[-5:-1])
print(lst[-1:-5:-1])
"""
to remove the elements from the list the methods are : 
pop() - delets an item from the specified index from the list
remove() - takes one argument which is removed from the list
"""
lst.pop(2)
print(lst)
lst.remove(1)
print(lst)

# list concatination

ls1 = [1,2,3]
ls2 = [4,5,6]

ls = ls1 + ls2
print(ls)

# set data structure in python

st = {"apple" , "mango" , "orange"}
print(st)

for i in st:
    print(i)
    
for i in range(len(st)):
    print(i)

st.add("gauva")
print(st)

#update() method takes another data structure as its parmeter
st1= {"chikoo" , "banana"}
st.update(st1)
print(st)

st = {"apple" , "mango" , "orange"}
st.remove("chikoo")
print(st)

st.discard("chikoo")
print(st)

s = {1,2,3,4,5,6}
print(min(s))
print(max(s))

#set operations
s1 = {"apple" , "mango"}
s2 = {"mango" , "banana" , "chikoo"}
print("union : " , s1|s2)
print("intersection : " , s1 & s2)
print("difference : " , s1 - s2)


#dictionary data structure

capitals = {
    "Maharastra" : "mumbai" , 
    "UP" : "lucknow" , 
    "gujrat" : "ahmedabad"}

print(capitals)
#accessing itmes via keys
print("capitals[Maharastra]:" , capitals["Maharastra"])
# change the value associate with any key using the simple assignment operator
capitals['gujrat'] = 'Gandhi nagar'
print(capitals)
capitals["west bengal"] = "kolkata"
print(capitals)
# to remove the key value pair from dictionary
capitals.pop("Maharastra")
print(capitals)
del capitals['UP']
print(capitals)
# iterating over dictionary
# values , keys , items

for states in capitals:
    #print(states , end=",")
    print(capitals[states])

print(capitals.keys())
print(capitals.values())
 
#gives the key value pairs in the form of tuple appended in the list
print(capitals.items())

capitals = {
    "Maharastra" : "mumbai" , 
    "UP" : "lucknow" , 
    "gujrat" : "ahmedabad"}

print("mumbai" in capitals)
print(len(capitals))

#dictionaries can have values in the form of list or tuples
seasons = {'summer' : ('feb' , 'march' , 'april' , 'may'),
           'rain' : ('june' , 'july' , 'august' , 'september'),
            'winter' : ('oct' , 'nov' , 'dec')}

print(seasons['rain'])
print(seasons['rain'][0])

seasons_ls = {'summer' : ['feb' , 'march' , 'april' , 'may'],
           'rain' : ['june' , 'july' , 'august' , 'september'],
            'winter' : ['oct' , 'nov' , 'dec']}

print(seasons_ls['rain'])
print(seasons_ls['rain'][0])

for x in seasons_ls:
    print(x)

"""
Dictionary dont allow duplicate keys
Dictionary Methods
get() is a useful method to access the values of key in a 
dictionay

"""

dict2 ={
        'brand' : 'maruti',
        'model' : 'brezza',
        'year' : '2021',
        'year' : '2020'
        }
print(dict2.get('brand'))
#if the key are duplicate then it considers the value for the 
#last defined key-value pair
print(dict2)
#here key-value pair 'year':2020 is considered

#to access key's
for x in dict2:
    print(x)
    
#to access values
for x in dict2:
    print(dict2[x])
    
for x in dict2.values():
    print(x)
    
for x,y in dict2.items():
    print(x,y)
    
#copy() method to make a copy of the original dictionary

dict1 = dict2.copy()
print(dict1)


#Assignments

"""
1.if any duplicate exist anywhere in the list
2.palindrom , box of star , mario pyramid , also in reverse 
diamond """
num = int(input("enter the no of rows you want : "))
for i in range(num):
    for j in range(num):
        print("*" , end=" ")
    print()

#lower triangle
num = int(input("enter the no of rows you want : "))
for i in range(num):
    for j in range(i+1):
        print("*" , end =" ")
    print()

# uppper triangle
num = int(input("enter the no of rows you want : "))
for i in range (num):
    for j in range(num-i):
        print("*" , end = " ")
    print()
    
"""Regular Pyramid"""
row = int
for i in range(1, row+1):
     for j in range(row - i):
         print(' ', end=' ')
     for k in range(2 * i - 1):
         print('#', end=' ')
     print()
    


""" find if the given string is palindrom or not 
and find the minimum and maximum element from the list"""


def check_palindrom(str1):
    Revstr1 = str1[len(str1)::-1]
    if (str1==Revstr1):
        print(f"{str1} is palindrom string")
    else:
        print(f"{str1} is not a palindrom string")

str1 = input("Enter a string to check palindrom : ")
check_palindrom(str1)


""" program to find the min and the max element from the list """
ls = [1,2,3,4,5,6,0,7]
def find_min(ls):
    min = ls[0]
    for i in range(1 ,len(ls)-1):
        if(ls[i]<min):
            min = ls[i]
        
    print("min is " , min)

def find_max(ls):
    max = ls[0]
    for i in range(1 ,len(ls)-1):
        if(ls[i]>max):
            max = ls[i]
    print("max is " , max)

find_min(ls)        
find_max(ls)


""" program to create a pyramid of stars """

n = 4
for i in range(0  , 2*n-1):
    for spaces in (0 , 2*n-1//2):
        print("_")
    print("*")
    