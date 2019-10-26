#19. Napisz program wyświetlający N początkowych wyrazów ciągu arytmetycznego o różnicy równej 3. Wartość N odczytaj z klawiatury.
s = "Ciąg arytmetyczny o różnicy 3: "
N = int(input("Podaj liczbę N (ilość wyrazów ciągu arytmetycznego do wyświetlenia): "))
for x in range(0,N):
    s = s+ str(1+x*3) +" "
print(s)