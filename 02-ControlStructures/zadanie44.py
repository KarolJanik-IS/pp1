#44
limit = int(input("Podaj limit prędkości (km/h): "))
predkosc = int(input("Podaj prędkość pojazdu (km/h): "))
mandat = 0
if (predkosc - limit) >10:
    mandat = 5*10 + (predkosc - (limit+10))*15
else:
    mandat = (predkosc -limit)*5
print("Mandat (zł):",mandat)
