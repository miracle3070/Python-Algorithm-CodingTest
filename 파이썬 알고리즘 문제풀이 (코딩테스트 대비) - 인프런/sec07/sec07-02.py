# 재도전으로 성공
# 풀이시간: 24분
import sys
#sys.stdin = open("input.txt", "r")


def DFS(level, t, p):
    global result
    if level > n:
        return
    if level == n:
        if result < p:
            result = p
    else:
        DFS(level+day[level], t+day[level], p+pay[level])
        DFS(level+1, t, p)


n = int(input()) # 휴가 가기 전 남은 날짜
day = []
pay = []
for _ in range(n):
    a, b = map(int, input().split())
    day.append(a)
    pay.append(b)

result = 0
DFS(0, 0, 0)
print(result)