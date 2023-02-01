T=int(input())
for tc in range(T):
    (a,b,c)=map(int,input().split(' '))
    mini=min(a,b,c)
    if mini==a:
        print("Draw")
    elif mini==b:
        print("Bob")
    elif mini==c:
        print("Alice")
