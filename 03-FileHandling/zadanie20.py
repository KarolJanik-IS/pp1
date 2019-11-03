#20
tableEven = []
with open("numbers.txt","r") as file:
    for line in file:
        if int(line)%2 == 0 and int(line)>-1: #sprawdzam również czy są naturalne, nie wiem czy powinienem skoro wszystkie liczby podane w pliku są naturalne, ale jednak w treści zadania jest napisane że mają być naturalne więc sprawdzam
            tableEven.append(int(line))
with open("evennumbers.txt","w") as file:
    for x in tableEven:
        file.write(f'{str(x)}\n')