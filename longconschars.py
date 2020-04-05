s = "AABCDDBBBEA"
#s = "AABCDDBBBEEEEEFFFFFFFA"
a = {}
for i in range(len(s)-1):
  if s[i] in a.keys() and s[i+1] in a.keys():
    if s[i]==s[i+1]:
        a[s[i]]+=1
  else:
    if s[i] not in a.keys():
        a[s[i]]=1
        if s[i]==s[i+1]:
            a[s[i]]+=1
    else:
        if s[i]==s[i+1]:
            a[s[i]]+=1
maxi = max(a.values())
for i in a.keys():
    if a[i]==maxi:
        print(i,maxi)
        break