def score(num,M):
    return num/M*100
#똑같이 반복된 행동은 define으로 처리한다

n=int(input())
arr=list(map(int,input().split()))
M=max(arr)

for i in range(n):
    arr[i]=score(arr[i],M)
print(sum(arr)/n)

