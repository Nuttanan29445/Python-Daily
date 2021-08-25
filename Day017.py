x=  input("Enter Your List : ").split()
l=[]
ans = []
temp = []
realAns = []
chck = False
for a in range(0,len(x)):
    z1=int(x[a])
    for b in range(a+1,len(x)):
        z2=int(x[b])
        for c in range(b+1,len(x)):
            z3 = int(x[c])
            for d in range(c+1,len(x)):
                z4 = int(x[d])
                for e in range(d+1,len(x)):
                    z5 = int(x[e])
                    for f in range(e+1,len(x)):
                        z6 = int(x[f])
                        for g in range(f+1,len(x)):
                            z7 = int(x[g])
                            for h in range(g+1,len(x)):
                                z8 = int(x[h])
                                if(z1+z2+z3+z4+z5+z6+z7+z8 == 100):
                                    l.append(z1)
                                    l.append(z2)
                                    l.append(z3)
                                    l.append(z4)
                                    l.append(z5)
                                    l.append(z6)
                                    l.append(z7)
                                    l.append(z8)
                                    chck = True


if(chck == True):               
    for i in range(len(l)):
        temp.append(l[i])  
        if((i+1)%8==0):
            ans.append(temp) 
            temp = []            
    for i in ans:
         if(i not in realAns):
             realAns.append(i)
    
    print(realAns)
else:
     print("None")