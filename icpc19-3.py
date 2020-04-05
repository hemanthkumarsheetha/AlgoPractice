for _ in range(int(input())):
    L1=[]
    L2=[]
    for e in range(int(input())):
        f1,f2 = input().split()
        if f1 not in L1:
            L1+=[f1]
            L2+=[[f2]]
        else:
            p = L1.index(f1)
            L2[p]+=[f2]
    #print(L1,L2)
    s=0
    for i in L2:
        zeros = i.count('1')
        ones = i.count('0')
        if zeros>ones:
            s+=zeros
        elif ones>zeros:
            s+=ones
        else:
            s+=zeros
    print(s)