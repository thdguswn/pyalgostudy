sample=[]
for i in range(3):
    i=int(input())
    sample.append(i)
b=sample[0]*sample[1]*sample[2]
b=str(b)
for u in range(0,10):
    print(b.count(str(u)))
    
    
#b.count(str(u))에서 struggle 함
    그냥 u는 숫자열이고 문자열로 바꿔야한
