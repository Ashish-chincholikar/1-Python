#---------------EXCEPTION HANDLING---------------------

try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero")

#-----------------------------------------------------    
print("enter 2 numbers to divide")
print("enter q to quit ")
while True:
    first_num = input("enter the first number : ")
    if first_num=='q':
        break
    second_num = input("enter the second number :")
    if second_num == 'q':
        break
    
    ans = int(first_num)/int(second_num)
    
    print(ans)
    
#------------------------------------------------------
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
try:
    c = a/b
except ZeroDivisionError:
    print("can't divide by zero")

#----------------------------------------------------
obj = open('Ashish.txt' , 'r')
contents = obj.read()
print(contents)
#----------------------------------------------------
fname = input("Enter the name of the file to be opened : ")

try:
    obj = open(fname , 'r')
    contents = obj.read()
    print(contents)
except FileNotFoundError:
    print(f"file name {fname} is not avaliable")
    
