C=int(input())
            
for i in range(C):
    N=list(map(int,input().split()))
    n=N[0]
    N=N[1:]
    avg=sum(N)/n
    p=[]
    for u in N:
       if u>avg:
          p.append(u)
    a=len(p)/n*100
    print("{:.3f}%".format(a))
