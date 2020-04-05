#L=[1,-3,2,1,-1]
L=[-2,3,2,4,-1]
L1=[]
for i in range(len(L)):
  if i!=0:
    #print(L1[i-1],L[i])
    print(L1)
    if (sum(L1[i-1])+ L[i]) > L[i]:
        L1+=[L1[i-1]+[L[i]]]
    else:
      L1+=[[L[i]]]
  else:
    L1+=[[L[i]]]
print(L1)
maxi = [sum(i) for i in L1]
print(maxi.index(max(maxi)))
print(L1[maxi.index(max(maxi))])