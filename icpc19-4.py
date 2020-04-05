for _ in range(int(input())):
    n,k = map(int,input().split())
    s = input()
    L=[]
    for i in range(k):
        L+=[input()]
    for i in s:
        l=k-1
        for h in range(len(L)):
            if i in L[h]:
                print(h)
                break
