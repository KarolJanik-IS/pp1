#40
import random
random.seed()
tab = [0,0,0,0,0,0]
for x in range(0,100):
    rzut = random.randrange(6)
    tab[rzut] += 1
print("Szóstka: ", tab[5])
print("Piątka: ", tab[4])
print("Czwórka: ", tab[3])
print("Trójka: ", tab[2])
print("Dwójka: ", tab[1])
print("Jedynka: ", tab[0])