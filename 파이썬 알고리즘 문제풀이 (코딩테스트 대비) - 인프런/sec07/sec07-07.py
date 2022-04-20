# 일부 성공 (재귀호출 깊이 제한 때문에 오류)
# 풀이시간: 23분
import sys
#sys.stdin = open("input.txt", "r")
INF = int(1e9)


def BFS(cur):
    global cnt
    if cur == e:
        return
    add = 0
    min_char = INF
    for i in range(3):
        temp = cur + dx[i]
        if 1 <= temp <= 10000:
            t_char = e - (cur + dx[i])
            if abs(t_char) < abs(min_char):
                min_char = t_char
                add = dx[i]
    cnt += 1
    BFS(cur + add)


dx = (1, -1, 5)
cnt = 0
s, e = map(int, input().split())
BFS(s)
print(cnt)