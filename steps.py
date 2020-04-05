def steps(n):
    if n==0: L=[]
    L=n*[1]
    L1=[L]
    for l in L1:
        for i in range(len(l)-2):
            if i+1<len(l)-1 and i+2 <=len(l)-1:
                L1+=[l[:i]+[l[i]+l[i+1]]+l[i+2:]]
    if n%2==0:
        L1+=[n//2 *[2]]
    print(L1)

steps(5)
