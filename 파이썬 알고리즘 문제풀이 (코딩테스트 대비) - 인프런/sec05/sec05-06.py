# 풀이시간: 14분
from collections import deque
import sys
#sys.stdin = open("input.txt", "r")


n, m = map(int, input().split())
p_list = list(map(int, input().split()))

queue = deque(enumerate(p_list))
cnt = 0
while True:
    idx, score = queue.popleft()
    if score < max(queue, key=lambda x:x[1])[1]:
        queue.append((idx, score))
    else:
        cnt += 1
        if idx == m:
            break
print(cnt)