# 풀이시간: 15분
import sys
#sys.stdin = open("input.txt", "r")


n = int(input())
array = list(map(int, input().split()))

start = 0
end = len(array) - 1
cnt = 0
result = ""
prev = -1

while start <= end:
    if prev < min(array[start], array[end]):
        if array[start] < array[end]:
            prev = array[start]
            start += 1
            result += "L"
            cnt += 1
        else:
            prev = array[end]
            end -= 1
            result += "R"
            cnt += 1
    elif prev < max(array[start], array[end]):
        if array[start] < array[end]:
            prev = array[end]
            end -= 1
            result += "R"
            cnt += 1
        else:
            prev = array[start]
            start += 1
            result += "L"
            cnt += 1
    else:
        break

print(cnt)
print(result)