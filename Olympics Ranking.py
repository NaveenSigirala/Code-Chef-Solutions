for _ in range(int(input())):
    a1,b1,c1,a2,b2,c2=map(int,input().split())
    if ((a1+b1+c1) > (a2+b2+c2)):
        print("1")
    else:
        print("2")
