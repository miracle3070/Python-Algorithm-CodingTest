# 풀이시간: 13분

import sys
#sys.stdin = open("input.txt", "r")


n, m = map(int, input().split())
people = list(map(int, input().split()))

people.sort(reverse=True)
cnt = 0

while people:
    cur = people[0]
    for i in range(1, len(people)):
        if cur + people[i] <= m:
            people.pop(i)
            break
    people.pop(0)
    cnt += 1

print(cnt)
