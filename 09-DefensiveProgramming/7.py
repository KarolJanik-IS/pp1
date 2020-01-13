wzrost = int(input("Podaj wzrost w cm"))
waga = float(input("Podaj wagę w kg"))
assert type(wzrost) == int,'Wzrost nie jest liczbą całkowitą'
assert type(waga) == float,'Waga nie jes tliczbą rzeczywistą'
assert wzrost < 220,"Wzrost jest zbyt zbyt wysoki"
assert wzrost > 150,"Wzrost jest zbyt niski"
assert waga > 40.0,"Waga jest zbyt niska"
assert waga < 150.0,"Waga jest zbyt wysoka"
print(f'{waga/(wzrost/100 * wzrost/100)}')