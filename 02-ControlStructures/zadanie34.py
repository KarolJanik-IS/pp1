#34
pesel = input("Podaj Pesel: ")
s = ""
if pesel[9] == "0" or pesel[9] == "2" or pesel[9] == "4" or pesel[9] == "6"or pesel[9] == "8":
    print("Płeć: kobieta")
else:
    print("Płeć: mężczyzna")
s = "19" + pesel[0:2]
s = int(s)
print("Wiek:",2018-s)