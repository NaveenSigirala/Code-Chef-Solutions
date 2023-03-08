for _ in range(int(input())):
    a,b,c,d,e=map(int,input().split())
    x=a//c 
    y=b//d 
    z=min(x,y)
    if z>=e:
        print("yes")
    else:
        print("no")
    
