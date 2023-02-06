lead,s1,s2,t=0,0,0,''
for i in range(int(input())):
    S,T=map(int,input().split())
    s1+=S
    s2+=T
    if(s1>s2):
        if(s1-s2)>=lead:
            lead=s1-s2
            t=1
    elif(s2-s1)>=lead:
        lead=s2-s1
        t=2
print(t,lead)
