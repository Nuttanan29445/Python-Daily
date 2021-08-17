def is_prime(n):
    if n <= 1:
        return False
    for k in range(2,n):
        if n%k == 0:
            return False
    return True
def next_prime(N):
    i = N+1
    d = False
    while(d==False) :
        d = is_prime(i)
        if d == True :
            return i
        i += 1
num = int(input())
ans = next_prime(num)
print(ans)