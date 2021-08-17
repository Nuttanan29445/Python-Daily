a = int(input("Input A:"))
n = 0
m = 0
while(n==0):
    b = int(input("Input B:"))
    if(a==b):
        print("You Win")
        n = 1
    elif(b>a):
        print("Higher")
    elif(b<a):
        print("Lower")
    
    if(m == 4):
        print("You Lose")
        n=1

    m = m+1