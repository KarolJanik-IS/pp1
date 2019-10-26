#43
a,b,c = int(input("Podaj pierwszą liczbę: ")),int(input("Podaj drugą liczbę: ")),int(input("Podaj trzecią liczbę: "))
tab = [a,b,c]
tab.sort()
s = "Liczby w kolejności rosnącej:"
for x in tab:
    s = s+" " + str(x)
print(s)