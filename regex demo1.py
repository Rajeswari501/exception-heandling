#reg exp on match()method
import re
st=input("Enter a string:")
result=re.match(r"raji",st)
print(result)
print(result.group(0))
print(result.start())
print(result.end())

