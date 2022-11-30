n=int(input())
a=0
u=0
x=list(map(int,input().split()))
for i in range(len(x)):
    if x[i]%2==0:
        a+=1
    else:
        u+=1
if a>u:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
