#29. Napisz program, który umożliwi użytkownikowi zmierzenie się z komputerem. Komputer rzuca kostką do gry. Następnie użytkownik próbuje odgadnąć liczbę wyrzuconych oczek wprowadzając z klawiatury liczbę od 1 do 6. Jeśli użytkownik odgadł liczbę wyrzuconych oczek, komputer wyświetla napis True. Zastosuj generator liczb losowych. Pamiętaj o utworzeniu w pierwszej kolejności algorytmu rozwiązania przy użyciu komentarzy.
# znowu wyrażenie: "Pamiętaj o utworzeniu w pierwszej kolejności algorytmu rozwiązania przy użyciu komentarzy."
import random
random.seed() #inicjuję seed(ziarno) na podstawie którego generowane są liczby losowe
rzut1 = random.randrange(6)+1
guess = int(input("Podaj, ile oczek kostki wyrzucił komputer: "))
print("Komputer wyrzucił:",rzut1)
if rzut1 == guess :
    print("Zgadłeś: True")
else:
    print("Zgadłeś: False")


