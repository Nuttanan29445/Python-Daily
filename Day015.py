def Answer(a):
    if(a>2):
        return Answer(a-1)+Answer(a-2)
    elif (a==2):
        return 2
    elif (a==1):
        return 1

x = int(input("Enter a number of stair step :"))
ans = Answer(x)
print("When rabbit moves 1 or 2 steps in each jump all possible jumping methods = ",ans)