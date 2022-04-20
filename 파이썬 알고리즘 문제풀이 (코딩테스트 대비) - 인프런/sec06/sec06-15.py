# 성공!
# 풀이시간: 28분
import sys
#sys.stdin = open("input.txt", "r")


def DFS(start):
    global cnt
    if visited[start]:
        return
    if start == n:
        cnt += 1
        return
    else:
        visited[start] = True
        for x in graph[start]:
            DFS(x)
        visited[start] = False


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

cnt = 0
visited = [False] * (n+1)
visited[0] = True
DFS(1)
print(cnt)