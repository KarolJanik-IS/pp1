#meh
import random
import turtle
turtle.setup(840, 640)
obraz = turtle.Screen()
xSize = 800
ySize = 600
obraz.screensize(xSize,ySize)
turtle.pu()
x0 = -400
y0 = -300
columnSize = 58
turtle.ht()
turtle.goto(x0,y0)
turtle.speed(0)
turtle.pd()
turtle.goto(x0,y0 +ySize)
turtle.goto(x0 + xSize,y0 +ySize)
turtle.goto(x0 + xSize,y0)
turtle.goto(x0,y0)
print(obraz.screensize())
def drawColumn(x,yHeight):
    turtle.pu()
    turtle.goto(x0+x,y0)
    turtle.pd()
    turtle.goto(x0+x,y0+yHeight)
    turtle.goto(x0+x+columnSize,y0+yHeight)
    turtle.goto(x0+x+columnSize,y0)
#drawColumn(20,50)
tab = []
for x in  range(10):
    tmp = random.randrange(20)+1
    drawColumn(x*(columnSize+20) + 20,tmp*20)
    tab.append(tmp)
tmp = 0
print(tab)
i = len(tab)
turtle.pensize(5)
for y in range(i):
    for x in range(len(tab)):
        if x!= len(tab)-1:
            if tab[x] > tab[x+1]:
                turtle.color("white")
                drawColumn(x*(columnSize+20) + 20,tab[x]*20)
                drawColumn((x+1)*(columnSize+20) + 20,tab[x+1]*20)
                tmp = tab[x]
                tab[x] = tab[x+1]
                tab[x+1] = tmp
                
                turtle.color("black")
                
                
                drawColumn(x*(columnSize+20) + 20,tab[x]*20)
                
                drawColumn((x+1)*(columnSize+20) + 20,tab[x+1]*20)
            if x == i-1:
                turtle.color("blue")
                drawColumn((x+1)*(columnSize+20) + 20,tab[x+1]*20)
    turtle.color("blue")
    drawColumn((0)*(columnSize+20) + 20,tab[0]*20)
    i -= 1
    print(tab)
print(tab)
