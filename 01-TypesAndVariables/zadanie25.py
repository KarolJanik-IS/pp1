#25. Numer rachunku bankowego składa się z 26 cyfr. Napiszprogram, który odczyta numerrachunku z klawiatury (wprowadzane tylko cyfry), a następniewyświetli go w formacie jakponiżej (wraz z odstępami). Przykładowy rezultat:
import math
print("Podaj numer rachunku bankowego: ")
num = input()
#print(a,b,c,p,Pole)
print("Numer rachunku:",num[0:2],num[2:6],num[6:10],num[10:14],num[14:18],num[18:22],num[22:26])
