#02-13
x = int(input("Podaj x "))
y = int(input("Podaj y "))
if x>0 and y>0 :
    print("punkt znajduje się w 1 ćwiartce")
elif x<0 and y>0:
    print("punkt znajduje się w 2 ćwiartce")
elif x<0 and y<0 :
    print("punkt znajduje się w 3 ćwiartce")
elif x>0 and y<0:
    print("punkt znajduje się w 4 ćwiartce")
elif x == 0 and y != 0:
    print("Punkt znajduje się na osi Y")
elif y == 0 and x != 0:
    print("Punkt znajduje się na osi X")
else :
    print("Punkt znajduje się w początku układów współrzędnych")

