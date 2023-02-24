for _ in range(int(input())):
    a,b=map(int,input().split())
    if a>1000:
        print((a*b)-((a*b)/100)*10)
    else:
        print(a*b)
