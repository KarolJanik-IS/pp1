#19
table = []
with open('universities.txt','r') as file:
    for line in file:
        table.append(line)
table.sort()
print(*table)
with open('universities.txt','w') as file:
    for x in table:
        file.write(x) #nie muszę dopisywać \n na końcu każdej linii, bo kiedy pobrałem linię i zapisałem je do tablicy/listy, zapisało je wraz z istniejącymi już \n
