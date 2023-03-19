for i in range(int(input())):
    n=int(input())
    l=map(int,input().split())
    l1=[6,13,20,27,7,14,21,28]
    count=8
    for i in l:
        if i not in l1:
            count+=1
        else:
            pass
    print(count)
