#17
import random
random.seed
def rzucKostka():
    return random.randrange(1,7)
r1 = rzucKostka()
r2 = rzucKostka()
r3 = rzucKostka()
print(f'Wyrzucone oczka: {r1} {r2} {r3}')
print(f'Suma oczek: {r1+r2+r3}')