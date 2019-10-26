#23
nazwyocen = ["niedostateczy","mierny","dostateczny","dobry","bardzo dobry","celujący"]
ocena = int(input("Podaj ocenę:"))
if ocena != 1 and ocena != 2 and ocena != 3 and ocena != 4 and ocena != 5 and ocena != 6:
    print("Podana wartość nie jest oceną z zakresu 1-6")
else:
    print("Ocena słownie:", nazwyocen[ocena-1])
