#26
def podatek(dochod):
    if dochod > 5000:
        return (dochod-5000)*0.32 + 5000*0.17
    else:
        return dochod*0.17
dochod = int(input("Podaj dochód: "))
print(f'Podatek należny: {podatek(dochod)}')