 #2720 세탁소 동혁
for _ in range(int(input())):
    money = int(input())
    coin = [25.10,5,1]
    
    Q = money // 25
    T = (money%25)//10
    N = (money%25)% 10// 5
    P = (money%25)% 10 % 5 //1

    print(Q,T,N,P)

#2903 중앙이동 알고리즘
n = int(input())
print((2**n+1)**2)


#2292 벌집
n = int(input())

start = 1 #벌집의 갯수, 1부터 시작
cnt = 1

while n > start:
    start += 6 * cnt #벌집이 6의 배수로 증가
    cnt += 1 #반복문을 반복하는 횟수
print(cnt)

#1193
n = int(input())
line = 1

while n > line:
    n -= line
    line += 1

if line % 2 == 0:
    up = n
    down = line - n + 1
else:
    up = line - n + 1
    down = n

print(up,'/',down, sep="")