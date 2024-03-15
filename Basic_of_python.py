"""
Created on Tue Apr  4 16:41:03 2023
Basic of Python

@author: Ashish Chincholikar
"""

print("Hello World")

x = 1
print(x)

print(type(x))
#converting to int

age1=input("Enter your age : ")
print(type(age1))
age2=input("Enter your age : ")
age=age1+age2
print(age)
age3=int(age)
print(age3)
print(type(age3))

a=int(input("Enter your age "))
a1=int(input("Enter your age "))
a2=a+a1
print(a2)
print(type(a2))

int_v=100
f=float(int_v)
print(f)
a='10'
f=float(a)
print(f)
b=int(a)
print(b)
print(type(b))

# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:46:40 2023

@author: Ashish Chincholikar
"""
""" calculate BMI using formula and round off upto 2 digits"""
height = float(input("Enter your height in meters : "))
weight = float(input("Enter your weight in kg : "))
BMI = round(weight/(height*height),2)

print(BMI)

if(BMI<18.5):
    print(f"underweight and BMI is {BMI}")
elif(BMI>18.5 and BMI<25):
    print(f"Normal and BMI is {BMI}")
elif(BMI>25 and BMI<30):
    print(f"Overweight and BMI is {BMI}")
elif(BMI>30):
    print(f"obese and BMI is {BMI}")
   
""" write a python code using logical operator and if elif ,
so as to allow for roller coster also ask user age and charge 
tickets accordingly

inputs : height in cm (height>=120) eligible
in nested age < 12 ticket 5 dollers 7 , 12 , 50 ,
also ask for photo provide choice y/n for 3 doller"""

print("welcome to the Roller Coaster....")
height = int(input("Enter your height in cm : "))
ticket_cost = 0
flag = 1
if(height>=120):
    age = int(input("Enter your age:"))
    if(age>10 and age<12):
        ticket_cost = 5
        print("your ticket is 5 dollers")
    elif(age>12 and age<18):
        ticket_cost = 7
        print("your ticket is 7 dollers")
    elif(age>18 and age<45):
        ticket_cost = 12
        print("your ticket is 12 dollers")
    elif(age>45 and age<55):
        ticket_cost = 50
        print("your ticket cost is 50 dollers")
    else:
        flag = 2
        print(f"your age is {age} hence not permitted to the roller coaster")
    if(flag!=2):
        ch = input("do you want your photograph (y/n)")
        if(ch=='y' or ch=='Y'):
            print("photograph cost is 3 doller")
            ticket_cost = ticket_cost + 3
            print(f"total amount to be paid is {ticket_cost} doller")
        else:
            print(f"total amount to be paid is {ticket_cost} doller")
else:
    print("your height is not enough to meet the roller coaster criteria")

# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 16:48:06 2023

@author: Ashish Chincholikar
"""

num = int(input("enter any number : "))

for i in range(0,10):
    if (i==num):
        break;
    print(i," ",end="")
print("done")


for i in range(0,10):
    if (i==num):
        break;
    print(i," ",end="")
    print("done")
