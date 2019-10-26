#50
import math
dziesietna = int(input("Podaj dowolną liczbę dziesiętną: "))
st = str(dziesietna)+"(10)="
s = ""
work = True

while work:
    if(dziesietna == 1):
        work = False
        s = s+"1"
    else:
        
        if dziesietna%2 == 0:
            s = s+"0"
            dziesietna = dziesietna/2
        else:
            s = s+"1"
            dziesietna = math.floor(dziesietna/2)
s = s[len(s)::-1]
st = st+s+"(2)"
print(st)


#    s = s +str(dziesietna%2)
#    dziesietna = math.floor(dziesietna/2)
#    if dziesietna == 1:
#        work = False
    
#s = s+"1"
