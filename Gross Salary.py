for i in range(int(input())):
    salary=int(input())
    if(salary<1500):
        print(salary+0.1*salary+0.9*salary)
    else:
        print(salary+500+0.98*salary)
