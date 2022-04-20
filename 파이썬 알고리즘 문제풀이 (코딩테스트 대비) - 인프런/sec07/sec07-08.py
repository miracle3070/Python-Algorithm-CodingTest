# 성공! (BFS로 해결안함...)
# 풀이시간: 24분
import sys
#sys.stdin = open("input.txt", "r")


n = int(input())
table = []
for _ in range(n):
    a = list(map(int, input().split()))
    table.append(a)

mid = n // 2
result = sum(table[mid])
start = 1
end = n - 2
upRow = mid-1
downRow = mid+1
for _ in range(mid):
    if start <= end:
        result += sum(table[upRow][start:end+1])
        result += sum(table[downRow][start:end+1])
        start += 1
        end -= 1
        upRow -= 1
        downRow += 1
    else:
        break

print(result)