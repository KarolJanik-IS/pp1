#28. Promień koła ma wartość 5. Napisz program, który dla podanej wartości promienia obliczy i wyświetli wartość pola powierzchni i obwodu koła.
import math
promien = 5
pi = math.pi
polePowierzchni = pi * (promien * promien)
obwod = 2 * pi * promien
print("Pole koła o promieniu",promien,"wynosi ",polePowierzchni)
print("Obwód koła o promieniu",promien,"wynosi ",obwod)
