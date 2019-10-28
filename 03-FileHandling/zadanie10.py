#10
number = 0
with open('numbers.txt','r') as file:
    for line in file:
        number += int(line)
print("suma liczb z pliku numbers.txt: ",number)