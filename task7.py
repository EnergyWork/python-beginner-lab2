import re

s = 'Тире-слово !Разве ? Собака , кошка ,попугай . Предложение ; точка с запятой ? \
    Обобщающее слово : слово1 , слово2 , слово3 ( привет ) , -дальше.. . [1 ] , выборка{ aqadaf }'

# simple
str1 = s
print(str1)
str1 = str1.replace('.','. ')
str1 = str1.replace('?','? ')
str1 = str1.replace('!','! ')
str1 = str1.replace(',',', ')
str1 = str1.replace(':',': ')
str1 = str1.replace(',',', ')
str1 = str1.replace(')',') ')
str1 = str1.replace('}','} ')
str1 = str1.replace(']','] ')
str1 = str1.replace('(',' (')
str1 = str1.replace('[',' [')
str1 = str1.replace('{',' {')
str1 = str1.replace('.  .','..')
str1 = str1.replace('-',' - ')
str1 = str1.replace('. .','..')
str1 = str1.replace('  ',' ')
print()
print(str1)

#regex

