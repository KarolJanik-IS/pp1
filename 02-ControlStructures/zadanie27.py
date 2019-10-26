#27
a = 5
i = 1
rising = True
s = ""
while i > 0:
    if i > a:
        rising = False
    if rising:
        s = s+"*"
        i += 1
    else:
        s = s[0:len(s)-1]
        i -= 1
    print(s)