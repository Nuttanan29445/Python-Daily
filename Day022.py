x1 = input()
x2=x1
j = []
for i in range(len(x2)):
    y = int(x2)%10
    j.append(int(y))
    x2 = int(x2)/10
n = (10*j[8])+(9*j[7])+(8*j[6])+(7*j[5])+(6*j[4])+(5*j[3])+(4*j[2])+(3*j[1])+(2*j[0])
for i in range(0,11):
    if((n+i)%11 == 0):
        print(x1+str(i))
        break