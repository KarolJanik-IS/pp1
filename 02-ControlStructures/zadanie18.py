#18. Napisz program, który wyświetli liczby od 1 do 30. Jeśli liczba jest podzielna przez 3 to zamiast niej wyświetl słowo ‘THREE’, jeśli liczba jest podzielna przez 5 to wyświetl słowo ‘FIVE’. Natomiast jeśli liczba jest podzielna zarówno przez 3 jak i przez 5 to wyświetl słowo ‘BINGO’. Zastosuj instrukcje iteracyjne. Przykładowy rezultat:
for x in range(1,31):
    if x%3 == 0 and x%5 == 0:
        print("BINGO")
    elif x%3 == 0:
        print("THREE")
    elif x%5 == 0:
        print("FIVE")
    else:
        print(x)