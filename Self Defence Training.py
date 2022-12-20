T=int(input())
for i in range(T):
    count=0
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(len(a)):
        if a[i] in range(10,61):
            count=count+1
        else:
            count=count+0
    print(count)
