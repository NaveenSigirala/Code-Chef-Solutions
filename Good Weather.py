for _ in range(int(input())):
    A1,A2,A3,A4,A5,A6,A7 = map(int,input().split())
    if (A1 + A2 + A3 + A4 + A5 + A6 + A7) > 3:
        print("YES")
    else:
        print("NO")
