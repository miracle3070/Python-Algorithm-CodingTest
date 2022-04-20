# 풀이시간: 27분 (시간초과로 60점)
# 파스칼 성질을 이용하지 않아서 시간초과 걸림.. (강의 참고)
import sys
#sys.stdin = open("input.txt", "r")


def DFS(level):
    if level == n:
        DFS2(0, nums)
    else:
        for i in range(1, n+1):
            if check[i] == 0:
                check[i] = 1
                nums[level] = i
                DFS(level+1)
                check[i] = 0


def DFS2(level, n_list):
    global result
    if level == (n-1):
        if n_list[0] == f:
            result.append(list(nums))
    else:
        tmp = []
        for i in range(len(n_list)-1):
            tmp.append(n_list[i] + n_list[i+1])
        DFS2(level+1, tmp)


n, f = map(int, input().split())
nums = [0] * n
check = [0] * (n+1)
result = []
DFS(0)

result.sort()
for x in result[0]:
    print(x, end=" ")
