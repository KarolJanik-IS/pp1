#02-11
login = "marek"
haslo = "m-123"
loginUser = input("Podaj login: ")
loginHaslo = input("Podaj hasło: ")
if login == loginUser and haslo == loginHaslo :
    print("Zalogowano")
else :
    print("Podany login lub hasło są nieprawidłowe")

