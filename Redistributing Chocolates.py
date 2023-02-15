for _ in range(int(input())):
    a,b,c=list(map(int,input().split()))
    if a+b+c>=6:
        print("yes")
    else:
        print("no")
