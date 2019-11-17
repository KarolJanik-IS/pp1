#34
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1)+fib(n-2)
#print(fib(3))
for x in range(1,20):
        print(fib(x))