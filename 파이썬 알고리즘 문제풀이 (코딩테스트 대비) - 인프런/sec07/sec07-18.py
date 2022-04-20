# 실패!

def Dsort(start, end):
    if start <= end:
        mid = (start + end) // 2
        Dsort(start, mid)
        Dsort(mid+1, end)
        temp = [0] * len(arr)
        k = 0
        for i in range(end-start+1):
            if arr[start+i] < arr[mid+i+1]:
                temp[i] = arr[start+i]
            else:
                temp[i] = arr[mid+i+1]
        for i in range(end-start+1):
            arr[start+i] = temp[i]
    else:
        return



arr = [23, 11, 45, 36, 15, 67, 33, 21]
print(arr)
Dsort(0, len(arr)-1)
print(arr)