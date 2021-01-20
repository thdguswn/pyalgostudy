list=[]
for i in range(9):
    i=int(input())
    list.append(i)
print(max(list))
print(list.index(max(list))+1)

#append 사용해서 list에 하나씩 추가하는방식


저렇게 풀어도 되고 아니면 이렇게 숏코딩 방식으로 풀어도 된다
inp = [int(input()) for _ in range(9)]
M = max(inp)
print(M)
print(inp.index(M) + 1)
