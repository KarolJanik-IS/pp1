#46
import random
random.seed()
s = ""
for x in range(0,20):
    s = s+str(random.randrange(16)-20) +" "
print(s)