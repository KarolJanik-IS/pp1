#37
tab = [1,2,3,1,4,2]
def unikalne(tablica):
    s = []
    
    for x in tablica: 
        no = True
        for y in s:
            if y == x:
                no = False
        if no:
            s.append(x)
    s.sort()
    #print(s)
    s2 = []
    for x in s:
        iloscA = 0
        #print(x)
        for y in tablica:
            if x == y:
                iloscA += 1
            if iloscA >1:
                s2.append(x)
                break
            
    #print(s2)
    s3 = []
    for x in s:
        no = True
        for y in s2:
            if x == y:
                no = False
        if no:
            s3.append(x)
    #print(s3)
    return(s3)
print(f'Spośród wartości: {tab}, nie powtarzają się: {unikalne(tab)}')
#unikalne(tab)