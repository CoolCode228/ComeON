a = input()
b = input()
c = input()
d = input()
print('Пользовател вывел числа в столбик:',a,b,c,d)
min = a 
if b < a:
    min = b 
if min > c:
    min = c 
if  min > d:
    min = d 
print(min)