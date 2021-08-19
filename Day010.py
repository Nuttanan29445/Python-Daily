j=[]
k=[]
z=[]
n=0
check = True
while(check==True):
    x = int(input())
    j.append(x)
    if(x == -1):
        check = False
    else:
        n = n+1
for i in j:
    c = j.count(i)
    k.append(c)

l = max(k)
for y in j:
    c1 = j.count(y)
    if(c1==l):
        z.append(y)
        break

if(l>n/2):
    z1 = " ".join(str(x) for x in z)
    print(z1)
else:
    print("Not Found")