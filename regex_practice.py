import re
text = "Call 9876543210 or 987-654-3210. Alternate: (91234 56780)" 
find=re.findall(r"\d{10}|d{3}-\d{3}-\d{4}|\d{5} \d{5}", text)
result={}
for i in find:
    number=i.replace("-","").replace(" ","")
    key=number[-4:]
    result[key]=number
print(result)
    
