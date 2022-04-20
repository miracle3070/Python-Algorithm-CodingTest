# 실패...
# 29분 고민했는데 안풀림.

#===========================
# 문제가 안풀렸던 원인: 살리고자 하는 개수가 m인데 나는 삭제해야할 개수가 m으로 착각함.
# 그러나 테스트케이스 2개에서 시간초과 발생

import sys
#sys.stdin = open("input.txt", "r")


# 피자배달거리 계산
def calc_dis(a, b):
    n1 = abs(a[0] - b[0])
    n2 = abs(a[1] - b[1])
    return n1 + n2

def DFS(level, pizza):
    global result
    if level == total_cnt - m:
        distance = 0
        for h in house:
            calc = []
            for p in pizza:
                calc.append(calc_dis(h, p))
            distance += min(calc)
        if distance < result:
            result = distance
    else:
        for i in range(len(pizza)):
            t_pizza = list(pizza)
            t_pizza.pop(i)
            DFS(level+1, t_pizza)




n, m = map(int,input().split())
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

result = int(1e9)

# 집, 피자집 검색
house = []
pizza = []
for y in range(n):
    for x in range(n):
        if board[y][x] == 1:
            house.append((y, x))
        elif board[y][x] == 2:
            pizza.append((y, x))
        else:
            pass
total_cnt = len(pizza)
DFS(0, pizza)
print(result)
