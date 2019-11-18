#4
import math
x = 3.7
y = 4

sqrtX = math.sqrt(x)
print(f'Pierwiastek kwadratowy z {x} wynosi {sqrtX}')
powX = pow(x,y)
print(f'{x} do potęgi {y} wynosi {powX}')
sqrtXY = pow(x,1.0/y)
print(f'Pierwiastek stopnia {y} z {x} wynosi: {sqrtXY} ')
circleY = math.pi * pow(y,2)
print(f'Pole koła o promieniu {y} wynosi {circleY} ')
def silniaY(y):
    i = y
    while y > 1:
        y = y-1
        i = i*y
    return i
print(f'Silnia y ={ silniaY(y)}')
nmlcX = math.floor(x)
print(f'Największa możliwa liczba całkowita mniejsza od x ={ nmlcX}')