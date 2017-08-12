import re

m = re.match('foo1', 'foo')

if m is not None:
    m.group()