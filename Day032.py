opr = input("Input Operator:")
st = []
n = int(input("Input num:"))
chck = 1
print("Input String")
for i in range(0,n) :
    st += [input()]
for i in range(len(st)):
    if len(st[i]) != len(st[i-1]) :
        print("Output:")
        print("Invalid size")
        chck = 0
        break
if chck == 0 :
    pass
else :
    lenx = len(st[0])
    leny = len(st)
    if opr == '90' :
        print("Output:")
        for j in range(lenx):
            for i in range(leny-1,-1,-1):
                print(st[i][j],end='')
            print()