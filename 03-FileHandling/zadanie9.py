with open('NoEducation.txt','r') as file:
    number = 0
    print("", end =f'{number}. ')
    for line in file:
        number +=1
        print(line, end=f'{number}. ')
        