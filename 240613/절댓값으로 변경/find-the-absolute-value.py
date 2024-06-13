N = int(input())

arr = list(map(int, input().split()))

def change(arr):
    a = len(arr)
    for i in range(a):
        if arr[i] < 0:
            arr[i] = -(arr[i])
    
    return arr

print(*change(arr))