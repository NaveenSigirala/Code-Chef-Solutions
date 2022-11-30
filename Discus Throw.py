T=int(input())
for i in range(T):
    x,y,z=map(int,input().split())
    print(max(x,max(y,z)))
