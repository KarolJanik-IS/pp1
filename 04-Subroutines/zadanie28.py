#28
import math
fmt = '{:>10}{:<1}{:<4}'
def rysujWykres(jezyki,wartosci):
    counter = 0
    for x in jezyki:
        
        s = ""
        for y in range(0,int(wartosci[counter]/2)):
            s += "#"
        #print(f'{x}: {s}')
        print(fmt.format(x,":",s))
        counter += 1
jezyki = ["Java","Python","Javascript","C++","C#","Ruby","Perl","PHP","C","Android"]
wartosci = [61,47,37,32,26,18,14,14,9,7]
rysujWykres(jezyki,wartosci)