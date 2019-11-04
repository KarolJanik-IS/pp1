#25
def jestImie(imie,imiona):
    for x in imiona:
        if imie == x:
            return 'imię zawarte jest w wykazie imion'
tablica = ['Janek','Ania','Wojtek','Zosia']
imie = 'Wojtek'
print(f'Imiona: {tablica}')
print(f'Imie: {imie}')
print(f'Rezultat: {jestImie(imie,tablica)}')