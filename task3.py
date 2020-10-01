import re

DEBUG = 1
if DEBUG:
    s = 'ggggggkkkrolagg'
else:
    s = input("Исходная строка: ")

#simple
st = ''
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        st += s[i:i+1] + '*'
        i += 2
    else:
        st += s[i:i+1]
else:
    st += s[-1]
print(st)

#regex
re_tmp = re.findall(r'((\w)\2*)', s)
st = ''
for o in re_tmp:
    st += o[0] + '*'
print(st[:-1])