#33
tab = ["zero","jeden","dwa","trzy","cztery","pięć","sześć","siedem","osiem","dziewięć"]
liczba = input("Podaj dowolną liczbę naturalną: ")
s = liczba + " - "
for x in range(0,len(liczba)):
    s = s + tab[int(liczba[x])] + " "
print(s)