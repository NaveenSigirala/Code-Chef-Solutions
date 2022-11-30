for i in range(int(input())):
    n,x,k=map(int,input().split())
    if (k//x)<n:
        print(k//x)
    elif (k//x)>n:
        print(n)
    else:
        print("0")
