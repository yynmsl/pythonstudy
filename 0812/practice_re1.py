import re

m = re.search(r'b.t|h.t', 'hat').group()
print m

m = re.search(r'\w+ \w+','yang yang').group()
print m
m = re.search(r'^([A-Z]|[a-z]|_)\w+','__').group()
print m
m = re.search(r'^\d+ (\w+ )*(\w+)','3135 Bordeaux Drive').group()
print m
m = re.search(r'^w+.\w+.(com|edu)','www.baidu.edu').group()
print m
m = re.search('\d+','123123123').group()
print m
m = re.search(r'\d+.\d+','1231.123').group()
print m
m = re.search(r'\d\+\d+i','3+2i').group()
print m
m = re.search(r'^([A-Z]|[a-z]|[0-9]){9}@(qq|163).com','626825701@qq.com').group()
print m
m = re.search(r'^w{3}.\w+(\.com)$','www.google.com').group()
print m

print type(m)
m = re.search(r' \w+','<type str>').group()
print m
m = re.search(r'1[1-3]{1}','11').group()
print m
m = re.search(r'[0-9]{4}-[0-9]{6}-[0-9]{5}|[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}','1111-111111-14111').group()
print m