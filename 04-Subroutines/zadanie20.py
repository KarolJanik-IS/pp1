#20
def potega(x,n):
    if n == 0:
        return 1
    else:
        return x * potega(x,n-1)
print(f'5 do potegi 3 wynosi {potega(5,3)}')