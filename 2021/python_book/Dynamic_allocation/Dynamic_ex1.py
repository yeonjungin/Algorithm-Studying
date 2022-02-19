'''
한 번 계산한 문제는 다시 계산하지 않도록 해주는 알고리즘이다.
다이나믹 프로그래밍 = 동적 계획법
동적 할당 : 프로그램 실행 중 실행에 필요한 메모리를 할당하는 기법이다.

다이나믹 프로그래밍으로 피보나치 수열을 해결할 수 있다. (대표적인 예시)
[피보나치 수열]
1번째 피보나치 수 = 1, 2번째 피보나치 수 = 1
n번째 피보나치 수 = (n-1)번쨰 피보나치 수 + (n-2)번째 피보나치 수

다이나믹 프로그래밍을 사용하기 위해선 다음과 같은 조건을 만족해야 한다.
1. 큰 문제를 작은 문제로 나눌 수 있다.
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

메모이제이션 기법 : 한 번 구한 결과를 메모리 공간에 메모해두고, 같은 식을 다시 호출하면
메모한 결과를 그대로 가져오는 기법이다.

메모이제이션 기법은 다이나믹 프로그래밍을 구현하는 방법 중 하나이다.

다이나믹 프로그래밍의 시간 복잡도는 O(N)
'''

# 피보나치 수열
def fibo(x):
    if x==1 or x==2:
        return 1
    return fibo(x-1)+fibo(x-2)
print(fibo(4))

# >> 이 방식은 x값이 커질수록 수행시간이 급격하게 늘어나는 문제가 발생한다.
# >> 그래서 다이나믹 프로그래밍을 사용하는 것!


# 메모이제이션 기법으로 피보나치 수열 구현 (재귀적)
d=[0]*100

def fibo2(x):
    if x==1 or x==2:
        return 1
    if d[x]!=0: # 이미 계산한 적 있는 문제라면 그대로 반환하기
        return d[x]
    d[x]=fibo(x-1)+fibo(x-2)
    return d[x]
print(fibo(99))

# 재귀함수를 이용하여 다이나믹 프로그래밍 소스코드를 작성하는 방법을, 큰 문제를 해결하기 위해 작은 문제를 호출한다고 하여 탑다운 방식이라고 함
# 재귀함수 대신 반복문을 사용하면 오버헤드를 줄일 수 있다!
# 반복문을 이용한 다이나믹 프로그래밍이 성능이 더 좋다.
# 재귀함수 깊이 오류 해결방법 : setrecursionlimit()함수 사용
'''
6
5 4
    4 3
        3 2     
            2 1
6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 2 -> 3 -> 4             
'''

# 반복문을 이용하면 작은 문제부터 차근차근 답을 도출한다고 하여 보텀업 방식이라고 한다.
d=[0]*100

d[1]=1
d[2]=1
n=99

for i in range(3,n+1):
    d[i]=d[i-1]+d[i-2]
print(d[n])