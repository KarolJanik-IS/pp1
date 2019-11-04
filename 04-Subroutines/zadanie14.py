#14
def wystepuje(liczba,tablica):
    print(f'Liczba: {liczba}')
    print(f'Tablica: {tablica}')
    for x in tablica:
        if liczba == x:
            print("Podana liczba występuje w tablicy")
            break
tab = [15,38,7,23,14]
licz = 23

wystepuje(licz,tab)
        