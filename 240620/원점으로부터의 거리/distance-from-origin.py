class dot:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y

n = int(input())

dots = []

for i in range(1, n + 1):
    x, y = map(int, input().split())
    dots.append(dot(i, x, y))

dots.sort(key=lambda x:(abs(0 - x.x) + abs(0 - x.y)))

for do in dots:
    print(do.number)