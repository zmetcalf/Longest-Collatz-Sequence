checkNum = 0
longestNum = 0
counter = 1

for x in range(400001, 500000, 2):
    checkNum = x
    while(checkNum > 1):
        #if(checkNum == 427630):
            #counter += 124
            #break;
        if(checkNum % 2 == 0):
            checkNum = (checkNum / 2)
        else:
            checkNum = ((checkNum * 3) + 1)
        counter += 1
    if(counter > longestNum):
        longestNum = x
        print longestNum
    counter = 1
    
print longestNum
