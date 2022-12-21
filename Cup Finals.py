T=int(input())
for i in range(T):
    a,b,c=map(int,input().split())
    if (abs(a-b))<=c:
        print("YES")
    else:
        print("NO")
