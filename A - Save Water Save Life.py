for _ in range(int(input())):
    a1,a2,a3,a4=map(int,input().split())
    b=a2+int(a3/2)
    c=b*a1
    if c <= a4:
        print("yes")
    else:
        print("no")
