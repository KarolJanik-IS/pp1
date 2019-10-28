#12
produkt = input("Podaj produkt który chcesz dopisać do listy zakupów: ")
with open('shoppinglist.txt','a') as file:
    file.write(produkt + '\n')