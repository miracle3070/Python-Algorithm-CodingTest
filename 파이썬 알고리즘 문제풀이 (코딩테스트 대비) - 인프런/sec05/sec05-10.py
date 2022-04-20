# 풀이시간: 15분
import sys, heapq
#sys.stdin = open("input.txt", "r")


heap = []
while True:
    num = int(input())
    if num == -1:
        break
    elif num == 0:
        if heap:
            output = heapq.heappop(heap)
            print(output)
        else:
            print(-1)
    else:
        heapq.heappush(heap, num)