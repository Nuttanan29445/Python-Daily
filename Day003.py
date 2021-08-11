check = True
j = []
#input Number
while(check==True):
    x = int(input())
    j.append(x)
    if(x == 0):
        check = False
#Max Min
c = input()
c1 = "max"
c2 = c.lower() == c1.lower()
if(c2==True):
    j.sort(reverse=True)
else:
    j.sort()
#print
for number in j:
    print(number, end = " ")