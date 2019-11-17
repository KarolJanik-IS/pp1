#35
def sumaCyfr(liczba):
    if len(str(liczba)) == 1:
        return int(liczba)
    else:
        return int(str(liczba)[:1])+sumaCyfr(str(liczba)[1:])
print(sumaCyfr(123))
print(sumaCyfr(64))
print(sumaCyfr(12345))