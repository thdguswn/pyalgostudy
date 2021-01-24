def score(a,b):
   return a/b*100

C=int(input())
            
for i in range(C):
    N=list(map(int,input().split()))
    avg=sum(N[1:])/N[0]
    num=0
    for u in N:
       if u<avg:
          N.remove(u)
    print(N)
