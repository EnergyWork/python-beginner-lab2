"""TAKS 4"""
import re

DEBUG = 1
if DEBUG:
    STRING = '1(a(a))(aaa)(a)2345(aaa)(a(aa))67(((((a(a))))))89'
else:
    STRING = input("Исходная строка: ")

# simple
s_tmp1 = STRING
que = []
i = 0
while i != len(s_tmp1):
    if s_tmp1[i] == '(':
        que.append(i)
        i += 1
    elif s_tmp1[i] == ')':
        s_tmp1 = s_tmp1.replace(s_tmp1[que[-1]:i + 1], '')
        i = que.pop(-1)
    else:
        i += 1
print(s_tmp1)

# regex
s_tmp = STRING
while re.findall(r'\((?:[^)(]|\([^)(]*\))*\)', s_tmp):
    s_tmp = re.sub(r'\((?:[^)(]|\([^)(]*\))*\)', '', s_tmp)
print(s_tmp)
