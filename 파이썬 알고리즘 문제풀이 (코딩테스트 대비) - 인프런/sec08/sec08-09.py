# 실패!
# 20분안에 해결했으나 시간초과 발생 (40점)


import sys
#sys.stdin = open("input.txt", "r")


def DFS(t_weight, t_worth):
    global worth
    if t_weight > limit_weight:
        return
    else:
        if worth < t_worth:
            worth = t_worth
        for i in range(n):
            DFS(t_weight + jewel[i][0], t_worth + jewel[i][1])



worth = 0
jewel = []
n, limit_weight = map(int, input().split())
for _ in range(n):
    a, b = map(int, input().split())
    jewel.append((a, b))

DFS(0, 0)
print(worth)