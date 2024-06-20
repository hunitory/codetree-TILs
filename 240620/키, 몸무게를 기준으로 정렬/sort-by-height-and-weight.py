class person_info:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())

people = []

for i in range(n):
    name, height, weight = map(str, input().split())
    people.append(person_info(name, int(height), int(weight)))

people.sort(key=lambda x:(x.height, -x.weight))

for person in people:
    print(person.name, person.height, person.weight)