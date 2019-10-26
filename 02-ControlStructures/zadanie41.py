#41
liczba = -1
suma = 0
ilosc = 0
while liczba != 0:
    liczba = int(input("Podaj liczbę"))
    if(liczba !=0):
        suma += liczba
        ilosc +=1
print(f'REZULTAT: Liczb={ilosc}, Suma={suma}, Średnia={suma/ilosc}')