for i in range(int(input())):
    x,y,a,b=map(int,input().split())
    if x!=a and x!=b and y!=a and y!=b:
        print("2")
    elif (x==a or x==b) and (y==a or y==b):
        print("0")
    else:
        print("1")
