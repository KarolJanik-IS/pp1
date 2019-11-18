#40
parzysta = lambda x : x%2 == 0
#print(parzysta(2))
tab =[1,2,3,4,5,6,7,8]
tab2 = filter(parzysta,tab)
for x in tab2:
    print(x)