# 풀이시간: 28분
import sys
#sys.stdin = open("input.txt", "r")


n = int(input())
array = list(map(int, input().split()))
result = []

table = list(enumerate(array, start=1))
table.reverse()
for num, idx in table:
    result.insert(idx, num)

for num in result:
    print(num, end=" ")