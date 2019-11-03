#18
table = []
with open('numbers.txt','r') as file:
    for line in file:
        table.append(int(line))
table.sort()
print(*table, sep = " ")
