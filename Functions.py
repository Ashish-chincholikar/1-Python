# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 08:06:09 2023

@author: Ashish Chincholikar
"""


""" 
functions/methods in python : if you find yourself writting
a block of code more than once then include that block of 
code in a function
syntax : 
    def function_name(paramters):
        body of the function
        
    """
    

""" write a program to find if the number entered by the user
is a prime number or not"""

def check_prime(num):
    for i in range(2 , num):
        if(num%i==0):
            return(1)
        else:
            return(0)

num = int(input("Enter the number : "))
res = check_prime(num) 
if(res==1):
    print("not a prime number!")
elif(res==0):
    print("prime number!")        
    
# types of arguments/parameters
# 1 . positional arguments : here the position in which the 
#arguments are passed is of atmost importance
# else it can lead to useless code
 
def desc_pet(animal_type , pet_name):
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")

desc_pet('Dog' , 'Moti')
'''
I have a Dog
My Dog's name is Moti
'''

desc_pet('Moti' , 'Dog')
''' I have a Moti
My Moti's name is Dog'''
# here the code is useless because the parameters are 
# not passed in correct order

# 2 . default arguments : if we want we can assign a default
# value to the argument 
# note while calling the function dont pass any value for
# the argument which is being assigned the default value
    
def desc_pet(pet_name , animal_type = 'DOG'):
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")
    
desc_pet('Moti')

"""
Created on Tue Apr 11 08:04:05 2023

@author: Ashish Chincholikar

"""
#Return values from a function

def get_formated_string(fname , lname):
    full_name = f"{fname} {lname}" #2 string are concatinated
    return full_name

fname = input("Enter the first name : ")
lname = input("Enter the last name : ")
name = get_formated_string(fname, lname)
print(name)

# returning a dictionary
def build_person(fname , lname):
    person = {'first_name' : fname ,
              'last_name' : lname}
    return person

fname = input("Enter the first name : ")
lname = input("Enter the last name : ")
name = get_formated_string(fname, lname)
print(name)

# passing a list to a function
def greet_user(names):
    for user in names:
        print(f"Hello , {user.title()}")
        #print(msg)

names = ['Ashish' , 'Sanket' , 'sumit']
greet_user(names)  

# passing arbitary number of arguments
# varible length arguments

def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms' , 'green peppers' , 'extra chees')

def add(*n):
    print(n)
    print( sum(n))
add(1,2,3,4)


def make_pizza(*toppings):
    print("making pizza with the following toppings : ")
    for items in toppings:
        print(f"-{items}")

make_pizza('pepperoni' ,'mushrooms' , 'green peppers' , 'extra chees')

#one positional argument and one variable length argument

def make_pizza(size , *toppings):
    print(f"making a {size}-inch pizza with the following toppings : ")
    for items in toppings:
        print(f"-{items}")

make_pizza(16 , 'pepperoni' ,'mushrooms' , 'green peppers' , 'extra chees')



#Assignments

""" program to check if the entered strings are anagram or not"""

def are_anagram(str1 , str2):    
    a = list((str1.replace("" , " ").lower()))
    b = list((str2.replace("" , " ").lower()))
   
    if(len(a)!=len(b)):
        print("not a anagram string")
    elif(len(a) == len(b)):
        if(sorted(a) == sorted(b)):
            print("anagram string")

str1 = input("Enter the string 1 : ")
str2 = input("Enter the string 2 : ")
are_anagram(str1 , str2)

""" given a list find the sum of the elements who are divisible 
by 5 or 7"""

def ret_sum(lst):
    sum = 0
    for i in range(len(lst)):
        if(lst[i]%5==0 or lst[i]%7==0):#divisible by 5 or 7 check using mod operator
            sum = sum + lst[i]
            
    return sum
lst = [1,2,5,7,14,55,45,21,49,8,9]
res = ret_sum(lst)
print(res)

def ret_sum(lst):
    sum = 0
    k = 0
    while(k!=len(lst)):
        if(lst[k]%5==0 or lst[k]%7==0):#divisible by 5 or 7 check using mod operator
            sum = sum + lst[k]
        k = k + 1
    return sum
lst = [1,2,5,7,14,55,45,21,49,8,9]
res = ret_sum(lst)
print(res)

""" 
write a function to reverse the string


str1 = "ashish chincholikar"
a = str1.split()
print(a)

b = " ".join(reversed(a))
print(b)

"""

def rev_string(str1):
    if str1=="":
        print("you have entered wrong input")
    else:
        words = str1.split()
        rev_sentence = " ".join(reversed(words))
        print(rev_sentence)
        
str1 = input("Enter the string :")
rev_string(str1)    


"""Write a python code whether a year is a leap year or not"""
year = int(input("Enter the year:-"))
def is_leap(year):
    if (year % 400 == 0) and (year % 100 == 0):
        # print(f"{year} is a leap year")
        return True
    
    elif (year % 4 ==0) and (year % 100 != 0):
        # print(f"{year} is a leap year")
        return True
    else:
        # print(f"{year} is not a leap year")
        return False
x = is_leap(year)
print(x)

"""Generate and display password containing between 7 and 10 charecters"""
from random import randint
SHORTEST = 7
LONGEST = 10
MIN_ASCII = 33
MAX_ASCII = 126

#get a random password
#return a string containing a random password
def randomPassword():
    randomLength = randint(SHORTEST,LONGEST)
    result = " "
    for i in range (randomLength):
        randomChar = chr(randint(MIN_ASCII,MAX_ASCII))
        result = result + randomChar
    return result
print("Your random password is :- ",randomPassword())


"""Write python code to find fibonacci series, Write a python code to find the """

n = int(input("How many terms? "))
n1 = 0
n2 = 1
count = 0
while count < n:
    print(n1,end=" ")
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    count += 1

#generating random number for lottery
# randrange() function from the random module 
# returns random numbers from the specified range
# of given parameters
from random import randrange
min_num = 1
max_num = 49
num_nums = 6
ticket_nums = []

for i in range(num_nums):
    rand = randrange(min_num , max_num+1)
    while rand in ticket_nums:
        rand = randrange(min_num , max_num+1)
        
    ticket_nums.append(rand)
    
ticket_nums.sort()
#print(ticket_nums)

for n in ticket_nums:
    print(n , end = " ")

"""
rand = randrange(1 , 4)
print(rand)
"""

""" code to remove the outlires value 
outliers are the values which are at the extreme values
extreme values here can be thought as the values which
are more than the expected values in the given list or 
any data set"""

def removeOutlier(data , num_outliers):
    for i in range(num_outliers):
        retval.pop(-1)
        
    return retval 

values = [ 0 , 89 , 105 , 7 , 4 , 12 , 400 ,23]
retval = sorted(values)
print(retval)
removeOutlier(retval , 3)

""" 
    Assingment : write python code to determine wheater 
    you pass is good or not
    8 char 
    1 upper
    1 lower
    1 special symbols
    numbers
"""
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
        
    
password = input("Enter your Password : ")
ret_val = check_pass(password)
if(ret_val == True):
    print("you have a strong password ")
else:
    print("you have a weak password ")



