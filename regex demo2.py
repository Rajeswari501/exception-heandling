import re
st=input("enter a string:")
result=re.search(r"raji",st)
print(result)
print(result.group(0))

