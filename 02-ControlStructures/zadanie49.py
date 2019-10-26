#49
nrDniaTygodnia = 3
i = 1
j = 0
ran = 5
s = ""
print("| PN | WT | SR | CZ | PT | SB | ND |")
while i<31:
    if nrDniaTygodnia == 6:
        ran = 6
    for x in range(0,ran):
        for y in range(0,7):
            if x == 0:
                if y<nrDniaTygodnia:
                    s = s+"|    "
                else:
                    #s = s+"| "+str(i)+" "
                    if i<10:
                        s = s+"|  "+str(i)+" "
                    else:
                        s = s+"| "+str(i)+" "
                    i += 1
            else:
                if i<10:
                    s = s+"|  "+str(i)+" "
                else:
                    if i<31:
                        s = s+"| "+str(i)+" "
                    else:
                        s = s+"|    "
                i += 1
            
        s = s+"|"
        print(s)
        s = ""


        