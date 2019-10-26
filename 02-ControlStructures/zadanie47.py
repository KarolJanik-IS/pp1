#47
import math
kwota = int(input("Podaj kwotę w zł: "))
piatki=0
dwojki=0
jedynki=0
r=0
print(f"Kwota {kwota} zł w monetach:")
piatki = math.floor(kwota/5)
r= kwota%5
dwojki = math.floor(r/2)
jedynki = math.floor(r%2)
print(f"5 zł - {piatki} szt")
print(f"2 zł - {dwojki} szt")
print(f"1 zł - {jedynki} szt")
