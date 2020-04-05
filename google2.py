import sys

def solution(A):
  """Your solution goes here."""
  A = sorted(A)
  s1=0
  s2=0
  if len(A)%2==0:
    j=len(A)-1
    c=0
    for i in range(len(A)):
      if i!=j:
        if c%2==0:
          s1+= A[i]+A[j]
        else:
          s2+= A[i]+A[j]
        j-=1
      else:
        break
    return abs(s1-s2)
  else:
    j=len(A)-1
    c=0
    L=[]
    for i in range(len(A)):
      if i!=j:
        if i not in L and j not in L:
          s1+=A[i]
          s2+=A[j]
          L+=[i,j]
          if abs(s1-s2) in A:
            p = abs(s1-s2)
            if s1<s2:
              s1+=p
            else:
              s2+=p
            ind = A.index(p)
            j=ind
            L+=[ind]
          else:
            j-=1
        elif i not in L and j in L:
          j-=1
          s1+=A[i]
          s2+=A[j]
      else:
        break
    #print(s1,s2)
    #print(L)
    return abs(s1-s2)

def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  A = [int(x) for x in input[0].split(",")]
  sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
  main()
