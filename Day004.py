dg = ['0','1','2','3','4','5','6','7','8','9']
chck = [1]*10
s = input()
for i in range(len(s)) :
    for j in range(0,10) :
        if s[i] == dg[j] :
            chck[j] = 0
#print(chck)
if 1 not in chck :
    print("None")
else :
    for k in range(0,10):
        if(chck[k]==0):
            dg[k] = 0
    for k in range(0,10):
        if(dg[k] != 0):
            print(dg[k], end = " ")