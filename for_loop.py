max=input()
max=int(max)
for i in range(max):
    if i % 3 == 0:
        print(i)
        print('делится на 3')
    if i % 5 == 0:
        print(i)
        print('делится на 5')
    if i %3 == 0 and i %5 == 0:
        print(i)
        print('делится на 3 и на 5')