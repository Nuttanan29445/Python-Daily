inp = input().split()
j1=[]
j2=[]
with open ("Day034.txt", "r") as myfile:
    data = myfile.readlines()
for i in data:
    x = i.split()
    j1.append(x)
for i in range(5):
    if(int(j1[i][0])<=int(inp[0])):
        j1.insert(i,inp)
        break
for i in range(5):
    print(j1[i][0],j1[i][1])

f = open("Day034.txt", "w")
for i in range(5):
    f.write(j1[i][0]+j1[i][1])
    f.write("\n")
f.close()