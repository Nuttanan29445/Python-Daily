def isSubset(a,b):
    if(all(x in a for x in b)):
        return True
    else:
        return False
      
x = input()
j=[]
k=[]
n=0
for i in range(len(x)):
    if(n==0):
        if(x[i]=="["):
            j.append(int(x[i+1]))
        if(x[i]=="," and x[i+1]!="[" and x[i+1]!=" "):
            j.append(int(x[i+1]))
        if(x[i]=="]"):
            n=n+1
    else:
        if(x[i]=="["):
            k.append(int(x[i+1]))
        if(x[i]=="," and x[i+1]!="[" and x[i+1]!=" "):
            k.append(int(x[i+1]))

chck1=isSubset(j,k)
chck2=isSubset(k,j)
if(chck1==True or chck2==True):
    print("True")
else:
    print("False")