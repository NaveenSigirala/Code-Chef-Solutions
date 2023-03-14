for _ in range(int(input())):
    arr=list(map(str,input().split()))
    x,y=map(str,input().split())
    if arr.index(x)>arr.index(y):
        print(y)
    else:
        print(x)
