import sys

def solution(A):
  """Your solution goes here."""
  L=[[A[0]]]
  for i in range(1,len(A)):
    f=0
    c=0
    for p in L:
      f=0
      for j in p:
        if j<A[i]:
          f+=1
      if f==len(p):
        c+=1
      else:
        p+=[A[i]]
    if c==len(L):
      L+=[[A[i]]]
  return len(L)

def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  A = [int(x) for x in input[0].split(",")]
  sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
  main()