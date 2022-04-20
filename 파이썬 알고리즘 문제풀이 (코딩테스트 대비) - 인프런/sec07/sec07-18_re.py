# 성공! (병합정렬 구현)
# 풀이시간: 10분


def Dsort(start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    Dsort(start, mid)
    Dsort(mid+1, end)
    temp = [0] * (end - start + 1)
    left = start
    right = mid+1
    i = 0
    while left <= mid and right <= end:
        if arr[left] < arr[right]:
            temp[i] = arr[left]
            left += 1
        else:
            temp[i] = arr[right]
            right += 1
        i += 1

    if left <= mid:
        while left <= mid:
            temp[i] = arr[left]
            left += 1
            i += 1
    elif right <= end:
        while right <= end:
            temp[i] = arr[right]
            right += 1
            i += 1
    for i in range(len(temp)):
        arr[start+i] = temp[i]


arr = [23, 11, 45, 36, 15, 67, 33, 21]
print(arr)
Dsort(0, len(arr)-1)
print(arr)