def fibo(n,s):
    if n in s.keys():
        return s[n]
    s[n]= fibo(n-1,s)+fibo(n-2,s)
    return fibo(n-1,s)+fibo(n-2,s)

n = int(input())
for i in range(n):
    p = int(input())
    L=[]
    for i in range(p):
        L+=[fibo(i,{0:0,1:1})]
    L1=[]
    while(len(L)>1):
        for i in range(len(L)):
           if (i+1)%2==0:
                L1+=[L[i]]
        L=L1
        L1=[]
    print(L[0]%10)