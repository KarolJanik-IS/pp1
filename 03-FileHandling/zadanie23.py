#23
import re
suma = 0
#cyfry = []
with open("land.txt","r") as file:
    for line in file:
        cyfry = re.findall('\d',line)
        for x in cyfry:
            #print(x)
            suma += int(x)
print(f'Suma cyfr występujących w pliku land.txt wynosi: {suma}')