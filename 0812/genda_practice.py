import re
import os

f = os.popen('who','r')
for i in f:
    print re.split(r'\s|\t',i.rstrip())
f.close()