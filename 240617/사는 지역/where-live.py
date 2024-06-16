class person_info:
    def __init__(self, name, address, location):
        self.name = name
        self.address = address
        self.location = location


n = int(input())

perple = []
for i in range(n):
    name, address, location = input().split()
    perple.append(person_info(name, address, location))

perple.sort(key=lambda x: x.name, reverse=True)

print(f'name {perple[0].name}')
print(f'address {perple[0].address}')
print(f'location {perple[0].location}')