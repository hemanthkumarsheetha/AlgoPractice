for _ in range(int(input())):
    n,k1 = map(int,input().split())
    L = list(map(int,input().split()))
    L1=[]
    L2=[]
    for i in range(1,len(L)+1):
        for j in range(i,len(L)+1):
          if i!=j and (j,i) not in L and (i,j) not in L:
            L1+=[(i-1,j-1)]
    for i in range(len(L1)):
        k=[L1[i]]
        for j in range(len(L1) ):
            if i!=j:
                k+=[L1[j]]
        L2+=[k]
    L3=[]
    for l1 in L2:
        L4 = [*L]
        #print(L4)
        for l in l1:
            #print(L4,l)
            while min(L4[l[0]],L4[l[1]]) >k1:
                L4[l[0]]-=1
                L4[l[1]]-=1

        L3+=[sum(L4)]
        L4=L
        #print(L4,L)
    print(max(L3))