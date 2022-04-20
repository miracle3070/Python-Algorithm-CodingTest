# 풀이시간: 14분
import sys
#sys.stdin = open("input.txt", "r")


n = int(input())
people = []
for _ in range(n):
    h, w = map(int, input().split())
    people.append((h, w))

people.sort(reverse=True)
cnt = 1
max_w = people[0][1]

for i in range(1, n):
    if max_w < people[i][1]:
        max_w = people[i][1]
        cnt += 1

print(cnt)