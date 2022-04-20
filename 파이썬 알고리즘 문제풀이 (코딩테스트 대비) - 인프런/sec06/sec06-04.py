# 실패
import sys
#sys.stdin = open("input.txt", "r")


array = []
def recursive(slist, i):
    if len(slist) <= i:
        return
    check[slist[i]] = 1
    recursive(slist, i+1)
    tmp = tuple([x for x in range(len(check)) if check[x] == 1])
    array.append(tmp)

    check[slist[i]] = 0
    recursive(slist, i+1)
    tmp = tuple([x for x in range(len(check)) if check[x] == 1])
    array.append(tmp)





n = int(input())
set_list = list(map(int, input().split()))
set_list.sort()
check = [0] * (set_list[-1]+1)
recursive(set_list, 0)
array = list(set(array))
array.remove(())
origin = tuple(set_list)

flag = False
for i in range(len(array)):
    for j in range(len(array)):
        target = array[i] + array[j]
        if target == origin and sum(target) == sum(origin):
            flag = True
            break
    if flag:
        break

if flag:
    print("YES")
else:
    print("NO")

