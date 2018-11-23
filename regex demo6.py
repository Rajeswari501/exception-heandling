# operators on regular expression
# import re
st=input("enter a string:")  #Iam
res=re.findall(r"\w",st)
print(res)  #['I', 'a', 'm']

print("===========================")

import re
st=input("Enter a string:") #Iam learning python
res=re.findall(r".",st)
print(res) #['I', ' ', 'a', 'm', ' ', 'l', 'e', 'a', 'r', 'n', 'i', 'n', 'g', ' ', 'p', 'y', 't', 'h', 'o', 'n']

print("=============================")

import re
st=input("enter  a string:")# Iam learning python
res=re.findall(r"\W",st)
print(res) # [' ', ' ', ' ']
print("==============================")


import re
st=input("Enter a string:") #Iam learning python
res=re.findall(r"\w*",st)
print(res) #['I', '', 'am', '', 'learning', '', 'python', '']
print("================================")


import re
st=input("enter a string:")#Iam raji
res=re.findall(r"\w+",st)
print(res)#['iam','raji']

