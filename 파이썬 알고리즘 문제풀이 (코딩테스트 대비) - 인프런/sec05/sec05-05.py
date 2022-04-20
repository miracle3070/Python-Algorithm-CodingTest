# 풀이시간: 8분
from collections import deque
import sys
#sys.stdin = open("input.txt", "r")


n, k = map(int, input().split())
queue = deque(range(1, n+1))

while len(queue) != 1:
    for i in range(k):
        target = queue.popleft()
        queue.append(target)
    queue.pop()

print(queue[0])