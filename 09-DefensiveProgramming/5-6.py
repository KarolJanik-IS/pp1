#5
a = 5
b = 3
assert b!=0, 'Wartość b równa 0!'
assert type(a) == int, 'a nie jest integerem'
assert type(b) == int, 'b nie jest integerem'
print(f'{a}/{b}= {a/b}')