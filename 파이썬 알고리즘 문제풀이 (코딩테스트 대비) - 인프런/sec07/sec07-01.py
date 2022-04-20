# 시간초과! (40점 나옴)
# 풀이시간: 30분
# 강의보니까 내 풀이 방식이 틀렸음.

import sys
sys.stdin = open("input.txt", "r")


def DFS(level, total, time):
    global result
    # cut edge 방법을 모르겠음... (강의보니까 이 부분 필요없음.)
    # if t_score - total < result - total:
    #     return
    if time > m:
        return
    if level == n:
        if result < total:
            result = total
            return

    if result < total:
        result = total

    else:
        for i in range(n):
            if check[i] == 0:
                check[i] = 1
                DFS(level+1, total+quiz[i][0], time+quiz[i][1])
                check[i] = 0


n, m = map(int, input().split())
quiz = []
check = [0] * n
result = 0
for _ in range(n):
    a, b = map(int, input().split())
    quiz.append((a, b))

t_score = [a for a, b in quiz]
t_score = sum(t_score)

DFS(0, 0, 0)
print(result)