d = int(input())
m = int(input())
y = int(input())
ans = 0
y-=543
Feb=28
if (y%400)==0:
    Feb=29
if ((y%4)==0) and ((y%100)!=0):
    Feb=29
day = [31,Feb,31,30,31,30,31,31,30,31,30,31]
for i in range(m-1) :
    ans += day[i]
ans += d
print(ans)