from itertools import product

n, k = map(int, input().split())
arr = list(map(str, input().split()))
length = len(str(n))

# product : 중복순열
while True:
    temp = list(product(arr, repeat=length))  # repeat을 통해 몇개를 뽑을지 설정한다.
    print(temp)
    ex = []
    for i in temp:
        now=int(''.join(i))
        if now <= n:
            ex.append(now)
    if len(ex) >= 1:
        print(max(ex))
        break
    else:
        length -= 1 # 숫자 단위가 바뀌는 구간
