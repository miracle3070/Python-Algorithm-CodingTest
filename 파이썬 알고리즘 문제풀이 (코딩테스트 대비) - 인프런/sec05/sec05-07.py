# 풀이시간: 14분
from collections import deque
import sys
#sys.stdin = open("input.txt", "r")


must = list(input())
n = int(input())
curi = [input() for _ in range(n)]

for i in range(n):
    queue = deque(must)
    result = "YES"
    for c in curi[i]:
        if not c in queue:
            continue
        else:
            target = queue.popleft()
            if target != c:
                result = "NO"
                break
    if not queue and result == "YES":
        print(f"#{i+1} YES")
    else:
        print(f"#{i+1} NO")


