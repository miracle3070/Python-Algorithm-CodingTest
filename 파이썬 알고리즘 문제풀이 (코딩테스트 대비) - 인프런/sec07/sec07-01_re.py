# 성공!
# 풀이시간: 7분
import sys
#sys.stdin = open("input.txt", "r")


def DFS(level, total, spend):
    global result
    if spend > m:
        return
    if level == n:
        if total > result:
            result = total
    else:
        DFS(level+1, total+score[level], spend+time[level])
        DFS(level+1, total, spend)


n, m = map(int, input().split()) # 문제 수, 제한 시간
score = []
time = []

for _ in range(n):
    a, b = map(int, input().split())
    score.append(a)
    time.append(b)

result = 0
DFS(0, 0, 0)
print(result)