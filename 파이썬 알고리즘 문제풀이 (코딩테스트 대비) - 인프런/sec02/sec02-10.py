n = int(input())
result = list(map(int, input().split()))
prev = 0
score = 0

for i in range(n):
    cur = result[i]
    if cur == 1:
        score += (prev + 1)
        prev += 1
    else:
        prev = 0

print(score)