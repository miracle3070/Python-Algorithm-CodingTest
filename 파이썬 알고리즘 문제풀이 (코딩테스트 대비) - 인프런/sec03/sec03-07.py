# 문제 푸는 20분 제한시간을 초과

import sys
#sys.stdin = open("input.txt", "r")


n = int(input())
table = []
for _ in range(n):
    row = list(map(int, input().split()))
    table.append(row)

mid = n // 2
total = 0

for i in range(mid):
    for k in range(mid-i, mid+i+1):
        total += table[i][k]
        total += table[n-i-1][k]

total += sum(table[mid])

print(total)

