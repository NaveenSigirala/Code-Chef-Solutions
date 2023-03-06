for t in range(int(input())):
    x, y, p, q = map(int, input().split())
    if(y + (q * 10) < x + (p * 10)):
        print("Chefina")
    elif(x + (p * 10) < y + (q * 10)):
        print("Chef")
    else:
        print("Draw")
