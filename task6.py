import re

s = 'один один два три четыре четыре четыре пять шесть семь семь восемь девять десять десять'

def result(arr):
    prev = ''
    for i in arr:
        curr = i + (' (' + str(arr.count(i)) + ')' if arr.count(i) > 1 else '')
        if curr == prev:
            continue
        else:
            print(curr)
            prev = curr

#simple
arr = s.split()
result(sorted(arr, key=lambda x: len(x), reverse=True))

print('----------------------------------------')

#regex
arr = re.findall(r'\w+', s)
result(sorted(arr, key=lambda x: len(x), reverse=True))

