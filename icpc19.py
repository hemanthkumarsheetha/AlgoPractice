def returnpalindrome(s,t):
    if s==t:
        print(len(s))
    elif len(s)==1 and len(t)==1 and s!=t:
        print(len(s+t+s))
    else:
        if len(s)>len(t):
            if s[-1]==t[0]:
                w =s[:-1]+t

                if w!=w[::-1]:
                    w+=s[0]
                print(len(w))
            else:
                rev_s = s[::-1]
                if t in rev_s:
                    ind = rev_s.index(t)
                    while(s+rev_s[ind-1] == (s+rev_s[ind-1])[::-1]):
                        ind-=1
                        if ind<1:break
                    print(len(s+rev_s[ind-1:]))
                else:
                    if
        else:
            s,t = t,s
            if s[-1] == t[0]:
                w = s[:-1] + t

                if w != w[::-1]:
                    w += s[0]
                print(len(w))
            else:
                rev_s = s[::-1]
                if t in rev_s:
                    ind = rev_s.index(t)
                while (s + rev_s[ind - 1] == (s + rev_s[ind - 1])[::-1]):
                    ind -= 1
                    if ind < 1: break
                print(len(s + rev_s[ind - 1:]))

for _ in range(int(input())):
    s,t = input().split()
    returnpalindrome(s,t)
