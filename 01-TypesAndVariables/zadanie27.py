#27. Napisz program, który dla dwóch liczb naturalnych wprowadzonych z klawiatury wyznaczy ich największy wspólny podzielnik. Funkcja obliczająca największy wspólny podzielnik dostępna jest w  module math (https://docs.python.org/3/library/index.html).
import math
liczba1 = int(input("Podaj pierwszą liczbę naturalną: "))
liczba2 = int(input("Podaj drugą liczbę naturalną: "))
gcd = math.gcd(liczba1,liczba2)
print("Największy wspólny dzielnik tych liczb to:",gcd)

