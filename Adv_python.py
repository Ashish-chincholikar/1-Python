
# generator 
"""  """

gen = ( 
       x 
       for x in range(3)
       )
print(gen)
for num in gen:
    print(num)
############################

gen = (x
       for x in range(3)
       )
next(gen)
#----------------------------
gen = (x for x in range(3))
next(gen)
next(gen)
next(gen)
next(gen)#-->stop iteration error
# functions which returns multiple values

def range_even(end):
    for num in range(0 , end , 2):
        yield num

for num in range_even(20):
    print(num)
    
#---------------------------------
def range_even(end):
    for num in range(0 , end , 2):
        yield num
#instead of using loop to access the elements from the range_even()function
#we create a handel which contains the values recived by 
#rang_even() function    
gen = range_even(6)
next(gen)
next(gen)
next(gen)

#chaining itertors

def lengths(itr):
    for ele in itr:
        yield len(ele)

def hide(itr):
    
    for ele in itr: 
        yield ele*'*'
        
passwords = ["not-good" , "give'm-pass" , "00100=100"]
#passwords = ["ashish" , "suraj"]
#ans = lengths(passwords)# can't directly print ans 
# as it returns a generator object we use loop to 
#display the result
#for x in ans:
 #   print(x)
 #values 8 , 11 , 9 i.e iterator object will be passed to hide()function
for password in hide(lengths(passwords)):
    print(password)
    

#----------------------------------------------
lst = ["milk" , "bread" , "egg"]
for index in range(len(lst)):
    print(f"{index+1} - {lst[index]}")
    


# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 08:17:29 2023

@author: Ashish Chincholikar
"""

lst = ["milk" , "bread" , "egg"]
for index in range(len(lst)):
    print(f"{index+1} - {lst[index]}")
    
#same code can be implemented using enumerate
""" enumerate() method adds a counter to iterable and returns
it in a formo of enumerating object
output in the form of 
(index , iterable-item)"""
lst = ["milk" , "bread" , "egg"]
x = enumerate(lst , start=1)
for i in x:
    print(i)
for index , item in x:
    print(f"{index} {item}")
    
#-----------------------------------

lst = ["milk" , "bread" , "egg"]
for index , item in enumerate(lst , start=1):
    print(f"{index} {item}")
    
#-----------------------------------------
#zip() method is used to 
name = ["dada" , "mama" , "kaka"]
info = [1234 , 5678 , 9120]
lst = ["A" , "B" , "C"]
for nm , inf , lst in zip(name , info , lst):
    print(nm , inf , lst)
    
#-------------------------------------
name = ["dada" , "mama" , "kaka"]
info = [1234 , 5678 , 9120]
z =  zip(name , info)
print(set(z))
for i in z:
    print(i)
    
#---------------------------------------
#drawback of zip() method
#excess unmatched data items will not be printed
name = ["dada" , "mama" , "kaka" , "bhaiya"]
info = [1234 , 5678 , 9120]

for nm , inf in zip(name , info):
    print(nm , inf)
#--------------------------------------------
#zip_longest
#zip_longest -->removes the drawback of zip method
from itertools import zip_longest
name = ["dada" , "mama" , "kaka" , "bhaiya"]
info = [1234 , 5678 , 9120]

for nm,inf in zip_longest(name , info):
    print(nm , inf)
#-------------------------------------------
#the fillvalue parameter will help to fill the value 
# of the iterable that is getting mapped with the none value

from itertools import zip_longest
name = ["dada" , "mama" , "kaka" , "bhaiya"]
info = [1234 , 5678 , 9120]

for nm,inf in zip_longest(name , info , fillvalue = 0):
    print(nm , inf)
    
#------------------------------------------------
#for the output to be True all the values in the list must 
#be non zero 
lst = [1,2,3,7,5,5]
if(all(lst)):
    print("all are True")
else:
    print("useless")
    
#if any one of the value is zero then the output is False

lst = [1,2,3,0,5,5]
if(all(lst)):
    print("all are True")
else:
    print("useless")
    
# use of any
lst = [0 , 0 , 0 , 1 ]
if any(lst):
    print("it has some values")
else:
    print("useless")
    
# use of any
lst = [0 , 0 , 0 , 0 ]
if any(lst):
    print("it has some values")
else:
    print("useless")
    
#------------------------------------------------
#count 
#count by default starts from 0
from itertools import count
counter = count()
print(next(counter))
print(next(counter))


from itertools import count
counter = count(start=1)
print(next(counter))
print(next(counter))

#cycle - 
#suppose you have repeated task to be done in a cyclic way
#periodic way , repeated task

import itertools
instructions = ("eat" , "code" , "sleep")
#the output of this will result the elements 
# of the instruction tuple to be executed repeatedly

for instructions in itertools.cycle(instructions):
    print(instructions)
    
#repeat
from itertools import repeat
for msg in repeat("keep patience" , times = 3):
    print(msg)
    

#combinations - provides the combinations of the elements
#from the given list 
from itertools import combinations
players = ["john" , "jani" , "rahul"]
for i in combinations(players ,2):
    print(i)
    

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 08:21:41 2023

@author: 91721
"""

import pandas as pd

f1 = pd.read_csv('C:/1-python/buzzers.csv')
#-------------------------------------------------------------
import os
with open('buzzers.csv') as raw_data:
    print(raw_data.read())
#-------------------------------------------------------------
#Reading CSV Data as lists

import csv
with open ('buzzers.csv') as raw_data:
    for line in csv.reader(raw_data):
        print(line)
        
#----------------------------------------------------------------
#reading CSV Data as Dictionaries

import csv
with open ('buzzers.csv') as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)
#-----------------------------------------------------------------
#--------------------------evening session------------------------
with open ('buzzers.csv') as data:
    flights = {}
    
    for line in data:
        k , v = line.split(",")
        #spliting the data from the file by using split() function 
        #and storing it in k and v variables
        flights[k] = v
        #updating the key:value pair in th dictionary
flights

""" 
{'ï»¿"TIME': 'DESTINATION"\n',
 '"09:35': 'FREEPORT"\n',
 '"17:00': 'FREEPORT"\n',
 '"09:55': 'WEST END"\n',
 '"19:00': 'WEST END"\n',
 '"10:45': 'TREASURE CAY"\n',
 '"12:00': 'TREASURE CAY"\n',
 '"11:45': 'ROCK SOUND"\n',
 '"17:55': 'ROCK SOUND"\n'}
now we write the code to remove the backslash \n
"""

with open ('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    
    for line in data:
        k , v = line.strip().split(",")
        #spliting the data from the file by using split() function 
        #and storing it in k and v variables
        flights[k] = v
        #updating the key:value pair in th dictionary
flights
#--------------------------------------------------------------------
#pre-requisite for decorators

def plus_one(number):
    return number+1

plus_one(5)
#-------------------------------------------------------------------
#defining function within a function : nested function
def plus_one(number):
    
    def add_one(number):
        number1 = number + 1
        return number1
    
    result = add_one(number)
    return result

plus_one(5)
#add_one(5)
#-------------------------------------------------------------------
#passing function as an arguments to other functions
def plus_one(number):
    result1 = number + 1
    return result1

def function_call(function):
# the function plus_one() is recived in the function parameter
# and now using function function() i.e using the plus_one()
# explicity we pass argument value to that function and 
# result will be printed 
    result = function(5)
    return result

function_call(plus_one)
#plus one function is given as the parameter to the function
#function_call()

#---------------------------------------------------------------
#function returning another function
#when a function is returning a function then we assign the 
#returning function to a variable

def hello_function():
    def say_hi():
        return "hi"
    
    return say_hi

hello = hello_function()
#here we recive say_hi() function which is begin returned by hello_function()
# and we recive it in hello variable
# hence hello is containg the say_hi() function 
# and now if we call hello() function then 
# it explicitly calls the say_hi() function which was returned previously 
hello()

"""
Created on Fri Apr 28 08:17:00 2023

@author: Vaibhav Bhorkade
"""
def add(a,b,c):
    sum=a+b+c
    return sum
add(1,2,3)
#   lambda Function 
add= lambda a,b,c:a+b+c
add(1,2,3)

# lambda Function
def mul(a,b,c):
    multi=a*b*c
    return multi
mul(2,3,4)

mul= lambda a,b,c:a*b*c
mul(2,3,4)

######## arbitatiry parameter
val=lambda *args:sum(args)
val(1,2,3,4,5,6,7,8,9,10)
val(1,2,3,4,5,6)

##------ *args ----###
def myfun(*args):
    for i in args:
        print(i)
myfun('hi','hello')
# lambda

myfun=lambda *args:args
myfun('hi','hello')

##
def person(name,*data):
    print(name)
    print(data)
    
## keyword argument **data     
def person(name,**data):
    print(name)
    print(data)
person(name='vaibhsv',age=21,place='mumbai')


###########################################
def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
        
person(name='vaibhsv',age=21,place='mumbai')

###########################################

val= lambda **data:sum(data.values())
val(a=2,b=6,c=5,d=0)

###########################################

pers=lambda **data:[(j)for i,j in data.items()]
pers(name="gaurav",age=26,place='shree Ram')
##############################################

list1=[1,2,3,4]
sq=lambda list1:[i**2 for i in list1]
print(sq(list1))
list1

#############################################

#Assignments
#----------------------evening session------------------
#generate a password consisting 1 adjective , 1 noun , 
#1 number and 1 special character 
#use random function to select a element 
#from a list of elements in each case

import string
import random 

adjective = ["sleepy" , "slow" , "fat" , "thin" , "fluffy"]
nouns = ["apple" , "mango" , "chikoo" , "pineapple"]
#selecting a value from the list adjective
adj = random.choice(adjective)
#selecting a value from the list nouns
non = random.choice(nouns)
#selecting a number as a value from the range 1 to 100
num = random.randrange(1 , 100)
#selecting a punctuation using string module inbuilt function
spchar = random.choice(string.punctuation)

# concating all the different selections and making 
# a all new password
fpass = adj + non + str(num) + spchar
print(f"final password is : {fpass}")

#====================================================
#string.punctuation has 32 punctuations
import string
import random 

while True:
    adjective = ["sleepy" , "slow" , "fat" , "thin" , "fluffy"]
    nouns = ["apple" , "mango" , "chikoo" , "pineapple"]
    
    adj = random.choice(adjective)
    non = random.choice(nouns)
    num = random.randrange(1 , 100)
    spchar = random.choice(string.punctuation)
    fpass = adj + non + str(num) + spchar
    print(f"password is : {fpass}")
    
    res = input("would you like to have another password (y/n) ")
    if(res== 'n'):
        break
"""
#how many punctuations in string.punctuations    
x = string.punctuation
print(type(x))
print(x)
j=0
for i in x:
    print(i)
    j+=1

print(j)
"""

""" ip from user 
list of adjective , nouns 
and pass the obtained password
to the check_pass() function from the previous assignment 
"""
import random
import string

is_upper = False
is_lower = False
is_num = False
def check_pass(password):
    for i in password:
        if(i>='A' and i<='Z'):
            is_upper = True
        elif(i>='a' and i<='z'):
            is_lower = True
        elif (i>="0" and i<="9"):
            is_num=True
    if (len(password)>8) and is_upper and is_lower and is_num:
        return True
    else:
        return False
        
adjective = []
noun = []

n = int(input("how many adjectives and nouns you want : "))
for i in range(0,n):
    a = input() 
    adjective.append(a)

for j in range(0 , n):
    n = input() 
    noun.append(n)

adj = random.choice(adjective)
non = random.choice(noun)
num = random.randrange(1 , 100)
spchar = random.choice(string.punctuation)
fpass = adj + non + str(num) + spchar
print(f"password is : {fpass}")

ret_val = check_pass(fpass)
if(ret_val == True):
    print("you have a strong password ")
else:
    print("you have a weak password ")
    

#--------------evening session--------------

import random

users = ["admin" , "employee" , "manager" ,"worker" , "staff"]
user = random.choice(users)
print(user)

if user=="admin":
    print("hello Admin , would you like to see a status report")
elif user=="employee":
    print("hello employee")
elif user=="manager":
    print("hello manager")
elif user=="worker":
    print("hello Worker")
else:
    print("hello")

#----------------------------------------------

users = ["admin" , "employee" , "manager" ,"worker" , "staff"]
for user in users:
    if user=="admin":
        print("hello Admin , would you like to see a status report")
    elif user=="employee":
        print("hello employee")
    elif user=="manager":
        print("hello manager")
    elif user=="worker":
        print("hello Worker")
    else:
        print("hello")

################################################
current_users = ["ali" , "ahmed" , "fahad" , "aun" , "rana"]
new_users = ["ali" , "rana" , "bilal" , "huzi" , "dula"]

for new_user in new_users:
    if new_user in current_users:
        print("person will need to enter a new username")
    else:
        print("the username is available")  
        
################################################
import hashlib
#32
a = "Ashish@123"
hasha = hashlib.sha256(a.encode('utf-8')).hexdigest()
print(hasha)
len(hashlib.sha256("Ashish@123".encode('utf-8')).digest())
#hashlib.sha256(b"Nobody inspects the spammish repetition").hexdigest()
""" 
selection of user
selection of pass

 ip pass : verify password
create hashcode for your password
store in list

ip from user username and pass 
create hashcode for this pass

#store the password in the form of list in json file
#WAC 
once user is giving user name and password
check username and password from list

once verified then prompt the user
that u have been allowed the acess

if wrong pass given count the attempt the number of
time the user is allowed to attempt of the pass
and print message accordingly



"""

############################################################################
import hashlib
#function check_pass() to validated the critera for the password
current_users = ["admin" , "employee" , "manager" ,"worker" , "staff"]
new_users = []
current_passwords = ['a9ca9211239ad70becbea405977149b1f4eb15a89a0335f18e928a3d6b0fa1d9']
new_pass = []


def login(USER):
    
    p = input("Enter your password ")
    ret_val = check_pass(p)#calling the check_pass() function to check if the entered
    #pass is matching our criteria
    if(ret_val == True):    
        hashpass = hashlib.sha256(p.encode('utf-8')).hexdigest()
        new_pass.append(hashpass)
        
    for npass in new_pass:
        if npass in current_passwords: 
            #password is matching
            
            print(f"{USER} you are logged in sucessfully")
       
        
is_upper = False
is_lower = False
is_num = False
def check_pass(password):
    for i in password:
        if(i>='A' and i<='Z'):
            is_upper = True
        elif(i>='a' and i<='z'):
            is_lower = True
        elif (i>="0" and i<="9"):
            is_num=True
    if (len(password)>8) and is_upper and is_lower and is_num:
        return True
    else:
        return False
        
    
#selection of username
print("Do your Registration!")
u = input("Enter username ")
new_users.append(u)
for new_user in new_users:
    if new_user in current_users:
        if new_user=="admin":
            print("Username is already exist")
            print("please login ")
            login("admin")
        
        elif new_user=="employee":
            print("Username is already exist")
            print("please login ")
            login("employee")
            
        elif new_user=="manager":
            print("Username is already exist")
            print("please login ")
            login("manager")
        
        elif new_user=="worker":
            print("Username is already exist")
            print("please login ")
            login("worker")
            """
    if new_user in current_users:
        print("Username is already exist")
        print("please login ")
        #user already exit 
        #ask user to login
        login()"""                    
    else:
        print("the username is available")  
    
        #selection of password
        p = input("Enter your password ")
        ret_val = check_pass(p)#calling the check_pass() function to check if the entered
        #pass is matching our criteria
        if(ret_val == True):    
            hashpass = hashlib.sha256(p.encode('utf-8')).hexdigest()
            new_pass.append(hashpass)
        else:
            print("you have a weak password")
            print("select a strong password")
  
    
        for npass in new_pass:
            if npass in current_passwords:
                print("password already taken")
                print("Enter a new password !")
            else:
                print("REGISTRATION DONE SUCESSFULLY")  
        


