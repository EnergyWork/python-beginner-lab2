import re

s = input("Исходная строка: ")
k = input("После какой буквы: ")
r = input("Добавить:")
print(s.replace(k, k + r))
print(re.sub(r"[{k}]".format(k=k), k + r, s))