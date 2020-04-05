for _ in range(int(input())):
    n = input()
    L=[]
    for i in range(len(n)):
        L+=[int(n[:i]+n[i+1:])]
    print(min(L))