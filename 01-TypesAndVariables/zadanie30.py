#30. Tablica zawiera wartości: 12,6, 4, 9 oraz 3. Napisz program, który wartości tablicy wyświetli w formie graficznej, jak poniżej:
tablica = [12,6,4,9,10]
i = 0
p = 0
s = ""
for x in tablica:
    while i<x:
        s = s+"*"
        i = i+1
    if x<10:
        print(f" {x}: {s}")
    else:
        print(f"{x}: {s}")
    i = 0
    s = ""

