#21
table = []
with open("numbersinrows.txt","r") as file:
    for line in file:
        #table.append(line.split(","))
        s = line.split(",")
        for x in s:
            table.append(int(x))
iloscLiczb = len(table)
sumaLiczb = sum(table)
print(f'W pliku znajduje się {iloscLiczb} liczb, ich suma wynosi {sumaLiczb}')