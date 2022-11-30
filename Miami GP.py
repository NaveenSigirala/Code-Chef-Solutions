T=int(input())
for i in range(T):
    x, y=map(int,input().split())
    if (1.07*x) >= y:
        print("YES")
    else:
        print("NO")
