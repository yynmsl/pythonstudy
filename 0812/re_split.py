import re
data = ('Mountain View,     CA 94040',
        'Sunnyvale,     CA',
        'Los Altos,     94023',
        'Cupertino     95014',
        'Palo Alto     CA')
for i in data:
    r = re.split(r'\s\s+',i)
    print r[1]