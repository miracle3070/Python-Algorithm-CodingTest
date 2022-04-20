# 성공!
# 풀이시간: 28분
# 지연 이유: 코딩실수. (memory 내용과 비교해야되는데 rocks 내용과 비교함.)
import sys
#sys.stdin = open("input.txt", "r")


n = int(input())
rocks = []
for _ in range(n):
    a, b, c = map(int, input().split())
    rocks.append((a, c, b)) # 밑 넓이, 무게, 높이

rocks.sort(reverse=True)
result = 0
memory = [0] * n
for i in range(n):
    target = 0
    for k in range(i-1, -1, -1):
        if rocks[i][0] < rocks[k][0] and rocks[i][1] < rocks[k][1] and target < memory[k]:
            target = memory[k]
    memory[i] = target + rocks[i][2]
    if result < memory[i]:
        result = memory[i]

print(result)