# 풀이시간: 8분
import sys
#sys.stdin = open("input.txt.", "r")


l = int(input())
boxes = list(map(int, input().split()))
cnt = int(input())

for _ in range(cnt):
    max_idx = boxes.index(max(boxes))
    min_idx = boxes.index(min(boxes))
    boxes[max_idx] -= 1
    boxes[min_idx] += 1

result = max(boxes) - min(boxes)
print(result)