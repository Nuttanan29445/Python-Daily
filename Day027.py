def Palind(list):
    return list == list[::-1]
l = input("Input String:")
ans = Palind(l)
print(ans)