#17 Napisz program, który obliczy sumę liczb parzystych oraz nieparzystych z przedziału <1,50>.
sumawszystkich=0
sumaparzystych=0
sumanieparzystych=0
for x in range(1,51):
    sumawszystkich +=x
for x in range(1,51):
    if x%2 == 0:
        sumaparzystych +=x
    else:
        sumanieparzystych +=x
print("Suma wszystkich liczb to:",sumawszystkich)
print("Suma liczb parzystych to:",sumaparzystych)
print("Suma liczb nieparzystych to:",sumanieparzystych)

