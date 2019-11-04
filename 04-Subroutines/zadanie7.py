#7
def printDigits():
    i = 1
    d = 1
    for x in range(0,3):
        d = i+ x*3
        print(f'{d} {d+1} {d+2}')
printDigits()