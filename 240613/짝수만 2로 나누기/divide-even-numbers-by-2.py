N = int(input())

arr = list(map(int, input().split()))

def f(arr):
    a = len(arr)
    for i in range(a):
        if arr[i] % 2 == 0:
            arr[i] = arr[i] // 2

    return arr


arr = f(arr)

print(*arr)