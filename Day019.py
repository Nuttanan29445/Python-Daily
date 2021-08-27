x = int(input())
j=[]
while(x >= 0.10):
    y = x*0.9
    z = "{:.2f}".format(y)
    j.append(z)
    x = x*0.9
for i in range(0,len(j)):
    print("[#%d]" %(i+1),"High : ",j[i])
print("Hit count: ",i+1)