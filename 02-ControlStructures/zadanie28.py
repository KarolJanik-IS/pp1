#28
a = int(input("Podaj a (wysokość) prostokąta: "))
b = int(input("Podaj b (szerokość) prostokąta: "))
s = ""
i = 0
working = True
while working:
    if i == 0 or i == a-1:
        for x in range(0,b):
            s = s + "*"
        i += 1
        if i == a:
            working = False
    else:
        s = s+"*"
        for x in range(0,b-2):
            s = s+" "
        s = s+"*"
        i += 1
    print(s)
    s = ""
