x = [float(x) for x in input("Enter matrix1: ").split()]
y = [float(y) for y in input("Enter matrix2: ").split()]
sum = 0
if( len(y) != len(x) ):
    print("error")
else:
    for i in range(len(x)):
        sum = sum + (x[i] * y[i])
    print(sum)