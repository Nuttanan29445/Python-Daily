print("Input:")
n = int(input())
wina = 0
winb = 0
ans = 'Tie'
for i in range(0,3*n) :
    a,b = input().split()
    if a=='R' :
        if b == 'P' :
            winb +=1
        elif b == 'S' :
            wina += 1
    elif a=='P' :
        if b == 'R' :
            wina +=1
        elif b == 'S' :
            winb +=1
    elif a=='S' :
        if b == 'R' :
            winb +=1
        elif b == 'P' :
            wina +=1
    if wina==n or winb==n :
        if wina > winb :
            ans = 'Player 1 wins'
        elif wina < winb :
            ans = 'Player 2 wins'
        break
print("Output:")
print(wina,winb)
print(ans)