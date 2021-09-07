x = int(input("Input:"))
l = []
a = 0
b = 0
c = 0
for i in range (0,x):
    a = i
    for j in range (0,x):
        b = j
        for k in range (0,x):
            c = k
            if(a+b+c==30):
                if((a**2)+(b**2)-(c**2)==0):
                    l.append(c)
print(max(j))