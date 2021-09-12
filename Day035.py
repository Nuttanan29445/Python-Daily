inp=int(input())
j=[]
for i in range(inp):
    s = input().split()
    j.append(s)
u = set(j[0])
its = set(j[0])
for i in range(len(j)):
    u = u.union(j[i])
    its = its.intersection(j[i])
print(len(u))
print(len(its))
