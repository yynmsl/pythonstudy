import re


s = 'This and that.'

m = re.findall(r'(th\w+)',s,re.I)
#print m
it = re.finditer(r'(th\w+)',s,re.I)
for i in it:
    print (i.group(1))