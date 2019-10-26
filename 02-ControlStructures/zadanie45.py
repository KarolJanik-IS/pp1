#45
N = int(input("Ile liczb pierwszych powinien znaleźć program?: "))
n = 0
i = 2
counter = 0
s = "Liczby pierwsze:"
while n<N:
    for x in range(1,i+1):
        if i%x == 0:
            counter += 1
    if counter == 2:
        s = s+" "+str(i)
        n += 1
    counter = 0
    i = i+1
print(s)