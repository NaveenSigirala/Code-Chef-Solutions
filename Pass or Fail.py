T=int(input())
for i in range (T):
    a,b,c=map(int,input().split())
    if (b*3)-((a-b))>=c:
        print("PASS")
    else:
        print("FAIL")
