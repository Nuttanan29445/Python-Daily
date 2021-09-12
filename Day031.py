x = int(input("Enter num 1 or 2 or 3: "))

if(x==1):
    f = open("textdaily.txt", "r")
    print(f.read())
if(x==2):
    inp = input("Write to text:").split()
    f = open("textdaily.txt", "w")
    for i in range(len(inp)):
        f.write(inp[i])
    f.close()
if(x==3):
    inp1 = input("Update to text:").split()
    f = open("textdaily.txt", "a")
    for i in range(len(inp1)):
        f.write(inp1[i])
    f.close()