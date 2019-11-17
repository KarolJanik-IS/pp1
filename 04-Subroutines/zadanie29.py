#29
import math
tab = [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]
#print(len(tab))
def mediana(tablica):
    tablica.sort()
    #print(len(tablica)/2)
    if len(tablica)%2 == 0:
        #print(tablica[int(len(tablica)/2)])
        #print("test")
        return((tablica[int(len(tablica)/2)] + tablica[int(len(tablica)/2) - 1])/2)
    else:
        #print(tablica[int(len(tablica)/2)])
        #print("test")
        #print(math.floor(len(tablica)/2))
        return(tablica[int(math.floor(len(tablica)/2))])

def dominanta(tablica):
    tablica.sort()
    a = tablica[0]
    d = tablica[0]
    iloscA = 0
    iloscD = 0
    for x in tablica:
        #print(x)
        
        if d == x:
            iloscD += 1
        elif a == x:
            iloscA += 1
        else:
            a = x
            iloscA = 1
        if iloscA > iloscD:
            d = a
            iloscD = iloscA
            
        
    #print("test")
    #print(a,d,iloscA,iloscD)
    return(d)

print(f'Mediana: {mediana(tab)}, Dominanta: {dominanta(tab)}')
#print(dominanta(tab))