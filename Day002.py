num = int(input())
y = []
for z in range(num):
    x = input()
    y.append(x)
else:
    j = sorted(y)
    for z in range(num):
        print(j[z])