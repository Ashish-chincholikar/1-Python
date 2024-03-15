# list
lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)

# list comprehention
lst=[num for num in range (0,20)]
print(lst)

names=['dada','kaka','mama']
lst=[name.capitalize() for name in names]
print(lst)

names=['dada','kaka','mama']
lst=[name.upper() for name in names]
print(lst)
lst=[name.lower() for name in names]
print(lst)

# List comprehension with if statement
def is_even(num):
    return num%2==0
lst=[num for num in range (10) if is_even(num)]
print(lst)

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 08:07:30 2023

@author: Ashish Chincholikar
"""
# list comprehention
lst = [num for num in range(0,20)]
print(lst)
    
names = ["dada" , "mama" , "kaka"]
lst = [names.capitalize() for names in names]
print(lst)

# if should be on the right hand side of the for loop
def is_even(num):
    return num%2==0
lst = [num
       for num in range(10)
       if is_even(num)
       
       ]
print(lst)

#--------------------------------------------------
lst = [f"{x}{y}"
       for x in range(3)
       for y in range(3)
       ]
print(lst)
# works similar to nested for loop
# o/p elements in a list 
for x in range(3):
    for y in range(3):
        print(f"{x}{y}")
        
""" set comphrension """ 
st = {
      num 
      for num in range(3)
      }     
print(st)

""" dictionary comphrension """

dict = {x:x*x
        for x in range(3)
        
        }
print(dict)
