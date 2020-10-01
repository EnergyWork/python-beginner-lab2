import re

DEBUG = 1
if DEBUG:
    s = 'aa100a100a-100aaa11'
else:
    s = input("Исходная строка: ")

#simple

dig = ''
summa = 0
for i in s:
    if i.isdigit() or i is '-':
        dig += i
    else:
        summa += int(dig) if (dig != '' and dig != '-') else 0
        dig = ''
else:
    summa += int(dig) if (dig != '' and dig != '-') else 0
print(summa)

#regex
re_tmp = re.findall(r'-?\d+', s)
print(sum(map(int, re_tmp)))