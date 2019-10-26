#28. Napisz program, który wyświetli rezultaty trzech rzutów kostką do gry oraz sumę wyrzuconych oczek. Zastosuj generator liczb losowych. Pamiętaj o utworzeniu w pierwszej kolejności algorytmu rozwiązania przy użyciu komentarzy.
# znowu wyrażenie: "Pamiętaj o utworzeniu w pierwszej kolejności algorytmu rozwiązania przy użyciu komentarzy."
import random
random.seed() #inicjuję seed(ziarno) na podstawie którego generowane są liczby losowe
rzut1 = random.randrange(6)+1
rzut2 = random.randrange(6)+1
rzut3 = random.randrange(6)+1
print("Rzut 1:",rzut1,"Rzut 2:",rzut2,"Rzut 3:",rzut3)
print("Suma rzutów kostką: ", rzut1+rzut2+rzut3)

