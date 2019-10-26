#49
nrDniaTygodnia = 2
i = 1
j = 0
row = 0
s = ""
print("| PN | WT | SR | CZ | PT | SB | ND |")
while i<31:
    for x in range(0,7):
        if x == 0:
            if j<nrDniaTygodnia:
                s = s+"|    "
            else:
                s = s+"| "+str(i)+" "
        else:
            s = s+"| "+str(i)+" "
        i += 1
        s = s+"|"
        print(s)
        s = ""


        