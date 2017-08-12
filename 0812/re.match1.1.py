import re
#patt='\w+@(\w+\.)*\w+\.com'
#print re.match(patt,'nobody@xxx.com').group()
#patt =re.match(patt,'nobody@xxx.yyy.zzz.com').group()
#print patt
#m = re.match('(a(b))','ab').group()
#print m
m = re.search('^The','The end.').group()
print m
#m = re.search('^The','end. The').group()
#print m
m = re.search(r'\Bthe','bite the dog').group()
print m