from datetime import date
import re

# simple 1998-10-30 -> 30/10/1998
date_tmp1 = date.today()
date_tmp1 = str(date_tmp1)
new_date1 = ''
for d in list(reversed(date_tmp1.split('-'))):
    new_date1 += d + '/'
else: 
    new_date1 = new_date1[:-1]
print(new_date1)

t1 = '/'.join(list(reversed(date_tmp1.split('-'))))
print(t1)

#regex
t2 = '/'.join(list(reversed(re.split(r'-', date_tmp1))))
print(t2)
