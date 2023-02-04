t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if y<=(x+z*2) or y<=(x+z):
        print("YES")
    else:
        print("NO")
