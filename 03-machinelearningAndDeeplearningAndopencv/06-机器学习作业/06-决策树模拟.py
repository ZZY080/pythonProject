isRed=True
isCold=True
isCheap=True
ishasSeed=True

if isRed:
    if isCold:
       if ishasSeed:
           print("buy")
       else:
           print("don't buy")
    else:
        if isCheap:
            print("buy")
        else:
            print("don't buy")


else:
    print("don't buy")