checkNum = 0
longestNum = 0
counter = 1

for x in range(9, 1000000, 2):
    checkNum = x
    while(checkNum > 1):
        if(checkNum % 2 == 0):
            checkNum = (checkNum / 2)
        else:
            checkNum = ((checkNum * 3) + 1)
        counter += 1
    if(counter > longestNum):
        longestNum = x
    counter = 1
    
print longestNum
