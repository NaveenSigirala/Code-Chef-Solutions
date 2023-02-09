t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    p=b*c 
    if(a<=p):
        print("NO")
    else:
        print("YES")
