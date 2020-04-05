n = int(input())
for i in range(n):
    m = int(input())
    L=list(map(int,input().split()))
    L= sorted(L)
    f=0
    s=0
    L1=[]
    for i in range(len(L)-1,-1,-1):
        if L[i]<2048:
          L1.append(L[i])
        if sum(L1)==2048 or L[i]==2048:
          print("YES")
          f=1
          break
    if f==0:
      print("NO")