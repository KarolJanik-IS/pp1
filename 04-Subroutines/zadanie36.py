#36
tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]
def suma(tablica):
    s = 0
    for x in tablica:
        if isinstance(x,int):
            s += x
        else:
            s += suma(x)
    return s
print(suma(tab))