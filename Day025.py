def isSquare(*num):
    j=[]
    for i in num:
        if( i/i**0.5 == i**0.5 ):
            j.append(i)
    j.sort()
    return j
print(isSquare(81,4,1))