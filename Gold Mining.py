for t in range(int(input())):
    n, x, y = map(int, input().split())
    print("Yes" if (n + 1) * y >= x else "No")
