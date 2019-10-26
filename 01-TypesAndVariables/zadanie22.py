#21.Dane są boki trójkąta a, b oraz c Napisz program, który dla podanych boków obliczy pole trójkąta wykorzystując wzór Herona. Wartości boków trójkąta odczytaj z klawiatury. Korzystając z programu oblicz pole trójkąta dla wielkości boków 3, 4 i 5. Porównaj rezultat z wynikiem uzyskanym przez innego studenta.
import math
print("Podaj boki trójkąta: ")
a,b,c = float(input()),float(input()),float(input())
p = (a+b+c)/2
Pole = math.sqrt(p*(p-a)*(p-b)*(p-c))
#print(a,b,c,p,Pole)
print("Pole trójkąta o tych bokach to: ",Pole)
