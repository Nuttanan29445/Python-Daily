p1,p2,p3,n1,n2 = input().split()
ans = 0
for i in range(int(n1),int(n2)):
    if(i==int(p1)):
        ans=ans + 10000
    if(i%1000==int(p3)):
        ans=ans+100
    if(i%100==int(p2)):
        ans=ans+25
print(ans)