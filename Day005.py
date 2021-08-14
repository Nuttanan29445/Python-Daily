n = input()
k = []
i = 0
chck = False
for x in range(len(n)):
    k.append(n[x])

n2 = k[0]
for x in range(len(k)):
   c = k.count(k[x])
   if(c>1):
       break    


if(c>19):
    print("True")
else:
    print("False")