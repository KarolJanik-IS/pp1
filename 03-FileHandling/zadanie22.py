#22
with open("students.txt","r") as file:
    for line in file:
        
        s = line.split(",")
        
        if len(s)>2:
            if s[2] != "age":
                if int(s[2])<30 :
                    #print(f'{s[0]} {s[1]}{s[2]}')
                    s[4] = s[4].rstrip('\n')
#                     test = s[0]
#                     test += "\t\t"
#                     test += s[1]
#                     print(test)
                    print(s[0],s[1],s[4], sep = '\t\t')
                    #print(f'{s[0]}\t{s[1]}\t{s[4]}')
                    #print(f'{s[0]}\t{s[1]}')
                    #print("a\tb")
                    #print(s[0], s[1])
                #for x in s:
                 #   table.append(int(x))
