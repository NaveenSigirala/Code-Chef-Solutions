for _ in range(int(input())):
    z,y,a,b,c=map(int,input().split())
    if (z-y) >= (a+b+c):
        print("yes")
    else:
        print("No")
