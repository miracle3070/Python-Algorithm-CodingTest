import sys
#sys.stdin = open("input.txt", "r")


n, target = map(int, input().split())
list_a = list(map(int, input().split()))
list_a.sort()

start = 0
end = len(list_a) - 1
result = -1
while start <= end:
    mid = (start + end) // 2
    if list_a[mid] == target:
        result = mid
        break
    elif list_a[mid] < target:
        start = mid + 1
    else:
        end = mid - 1

print(result+1)