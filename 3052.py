mylist=[]
for i in range(10):
    i=int(input())
    i=i%42
    mylist.append(i)
myset=set(mylist)
#중복된 숫자를 제거해주는 과정
mylist=list(myset)
#다시 리스트로 변환해주는 과정
print(len(mylist))
#리스트에 숫자가 몇개있는지-> count랑 다름 (이부분 헷갈


 
