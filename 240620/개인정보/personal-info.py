class person_info:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


people = []
for i in range(5):
    name, height, weight = map(str, input().split())
    people.append(person_info(name, int(height), float(weight)))


print("name")
people.sort(key=lambda x:(x.name))

for person in people:
    print(person.name, person.height, person.weight)

print()

print("height")
people.sort(key=lambda x: (-x.height))

for person in people:
    print(person.name, person.height, person.weight)