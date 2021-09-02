x = int(input("Enter num: "))
j = []
for i in range(0,x):
    if(i%2==0):
        j.append(i)
ans = ", ".join([str(n) for n in j])
print("("+ans+")")