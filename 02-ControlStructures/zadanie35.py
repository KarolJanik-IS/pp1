#35
import math
print("ax2+bx+c=0")
a,b,c = int(input("a: ")),int(input("b: ")),int(input("c: "))
delta = (b**2) - (4*a*c)
pierwiastekzDelta = math.sqrt(delta)
x1 = (-b - pierwiastekzDelta)/(2*a)
x2 = (-b + pierwiastekzDelta)/(2*a)
print("Pierwiastki tego równania to:",x1,x2)