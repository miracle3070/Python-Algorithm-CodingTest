# 출제자의 의도대로 다시 풀었음.
import sys
#sys.stdin = open("input.txt", "r")


n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))

result = []
length = n + m
i = 0
k = 0
for _ in range(length):
    if i < len(list1) and k < len(list2):
        if list1[i] < list2[k]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[k])
            k += 1
    elif i < len(list1):
        result.append(list1[i])
        i += 1
    else:
        result.append(list2[k])
        k += 1

for x in result:
    print(x, end=" ")