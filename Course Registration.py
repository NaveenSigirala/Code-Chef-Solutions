T=int(input())
for i in range(T):
    X,Y,Z=map(int,input().split())
    if Y>=X+Z:
        print("Yes")
    else:
        print("No")
