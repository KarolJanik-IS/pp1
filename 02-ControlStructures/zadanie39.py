#39
a = 0
b = 1
c = 0
print(f'{a} {b} ')
for x in range(0,48):
    print(f'{a+b}')
    c = a
    a = b
    b = c+b