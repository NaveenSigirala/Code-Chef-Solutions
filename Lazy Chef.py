for i in range(int(input())):
    x=list(map(int,input().split()))
    a=x[0]*x[1]
    b=x[0]+x[2]
    c=min(a,b)
    print(c)
