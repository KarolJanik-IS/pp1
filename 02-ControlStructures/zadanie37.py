#37
a,b,c = int(input("Podaj pierwszą liczbę: ")),int(input("Podaj drugą liczbę: ")),int(input("Podaj trzecią liczbę: "))
d = 0
tab = [a,b,c]
tab.sort()
print("Mediana wynosi:", tab[1])