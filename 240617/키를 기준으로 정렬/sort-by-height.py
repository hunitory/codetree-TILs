n = int(input())

people = [list(map(str, input().split())) for _ in range(n)]

people.sort(key=lambda x:x[1])

for person in people:
    print(*person)