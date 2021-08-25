def is_prime(n):
    if n <= 1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k == 0:
            return False
    return True
def next_prime(N):
    i = N+1
    while True :
        d = is_prime(i)
        if d == True :
            return i
        i += 1
def next_twin_prime(N):
    i = N
    while True :
        k = next_prime(i)
        q = next_prime(k)
        if q-k == 2 :
            c = str(k)+','+str(q)
            return c
        else :
            i = k

x = int(input("Input number:"))
ans = next_twin_prime(x)
print("Next twin prime:",ans)