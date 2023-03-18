for i in range(int(input())):
    x=int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ans = 0
    for i in range(x):
        if a[i]<=2*b[i] and b[i]<=2*a[i]:
            ans += 1 
    print(ans)
