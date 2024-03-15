# JSON - JavaScript Object NOtation  
import json
numbers=[2,3,4,5,7,11,13]
filename='numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers ,f)

a=open('numbers.json')
a.read()

#Saving data json is useful
username=input("What is your name : ")
filename='username.json'
with open(filename,'w') as f:
    json.dump(username, f)
print(f"We'll remenber you mean when you back {username}")

import json
filename='username.json'
with open(filename) as f:
    username=json.load(f)
print(f"Welcome back , {username} !")

filename='username.json'
try:
    with open(filename) as f:
        username=json.load(f)
except FileNotFoundError:
    username=input("What is your name ?")
    with open(filename,'w') as f:
        json.dump(username,f)
        print(f"We will Remember you when you come back, {username}")
else:
    print(f"Welcome back ,{username}")
