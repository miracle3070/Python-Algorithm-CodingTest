import sys
#sys.stdin = open("input.txt", "r")

n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))

result = list1 + list2
result.sort()

for x in result:
    print(x, end=" ")
