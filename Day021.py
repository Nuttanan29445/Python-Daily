import math
j=[]
x = input().split()
for i in range(len(x)):
    y = math.factorial(int(x[i]))
    j.append(y)
for i in range(len(j)):
    print(j)