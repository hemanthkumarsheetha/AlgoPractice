#L=[1,-3,2,1,-1]
L=[-2,3,2,4,-1]
print(*L)
import numpy as np
for i in range(len(L)-1,-1,-1):
  k = int(np.floor((i+1)*np.random.rand()))
  L[i],L[k] = L[k],L[i]
print(*L)