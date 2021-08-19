n1 = int(input("Enter num1: "))
n2 = int(input("Enter num2: "))
ans = 1
x = max(n1,n2)
for i in range(1,x):
    if(n1 % i == 0 and n2 % i == 0):
        ans = ans*i
        n1 = n1/i
        n2 = n2/i

print("Greatest common divisor:",ans)