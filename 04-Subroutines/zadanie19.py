#19
def suma(N):
    if N == 1:
        return 1
    else:
        return N + suma(N-1)
N = 500
print(suma(N))
