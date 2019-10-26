#29
tab = [15,8,31,47,2,19]
i = 0
s = "tab:"
for x in tab:
    s = s+" "+str(x)
print(s)
tab.reverse()
s = "tab in reverse:"
for x in tab:
    s = s+" "+str(x)
print(s)
