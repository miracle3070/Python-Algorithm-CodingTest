# 소요시간: 16분 49초
import sys

#sys.stdin = open("input.txt", "r")

l = list(range(1, 20+1))
for _ in range(10):
    a, b = map(int, input().split())
    tmp = l[a-1:b]
    tmp.reverse()
    l[a-1:b] = tmp

for x in l:
    print(x, end=" ")

