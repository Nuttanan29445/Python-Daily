n = int(input())
j=[]
k=[]
for i in range(n) :
    if i%2 == 0:
        a,b=[int(e) for e in input().split()]
    else :
        b,a=[int(e) for e in input().split()]
    j.append(a)
    k.append(b)
minx = min(j)
maxx = max(j)
miny = min(k)
maxy = max(k)
zz = input()
if zz == 'Zig-Zag' :
    print("Output:",minx,maxy)
else :
    print("Output:",miny,maxx)