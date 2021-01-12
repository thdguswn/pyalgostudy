#문제: n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
#출력: 1부터 n까지 합을 출력한다.
#예제: 3 ->6
n=int(input())
for i in range(0,n):
    n+=i
print(n)




