#30
numberOfTries = 0
correctPin ="0805"
while numberOfTries<3:
    inputPin = input("Podaj kod PIN: ")
    if inputPin == correctPin:
        print("Poprawny PIN. Karta płatnicza zaakceptowana.")
        break
    print("Kod PIN jest niepoprawny.")
    numberOfTries += 1
    if numberOfTries == 3:
        print("Karta płatnicza zostaje zablokowana")