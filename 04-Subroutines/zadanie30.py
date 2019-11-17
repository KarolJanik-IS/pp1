#30
import random
def losowa():
    random.seed()
    return(random.randrange(1,50))
ilosc = 1000
parzyste = 0
nieParzyste = 0
for x in range(ilosc):
    if losowa()%2 == 0:
        parzyste += 1
    else:
        nieParzyste +=1
print(f'Dla {ilosc} liczb losowych całkowitych z przedziału <1,50>:')
print(f'Liczby parzyste: {(parzyste/ilosc)*100}%')
print(f'Liczby nieparzyste: {(nieParzyste/ilosc)*100}%')
#print(fmt.format("25,2525"))
#print(f'Liczby parzyste: {"{:6.6}".format((parzyste/ilosc)*100)}%')
#print('{:4.4}'.format("25,2525"))