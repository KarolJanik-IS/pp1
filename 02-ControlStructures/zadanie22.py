#02-22
tab = [15,8,31,47,2,19]
suma = 0
il = 0
for i in tab :
    if i%2 !=0 :
        suma += i
        il += 1

print(f"Średnia arytmetyczna wynosi: {suma/il}")