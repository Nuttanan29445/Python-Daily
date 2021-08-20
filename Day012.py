ans = []
n = int(input())
for i in range(0,n):
    a = int(input())
    ans += [a]
b = input()
b = [int(e) for e in b.split()]
ans += b
x = 0
while x != -1 :
    x = int(input())
    if x != -1 :
        ans += [x]
anss = []
for i in range(len(ans)):
    if i%2 == 0 :
        anss += [ans[i]]
    else :
        anss = [ans[i]] + anss

print(anss)