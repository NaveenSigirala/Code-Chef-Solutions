for _ in range(int(input())):
    x,y=map(int,input().split())
    if 100-100*x/100 == 200-200*y/100:
        print("both")
    elif 100-100*x/100 < 200-200*y/100:
        print("first")
    else:
        print("second")
