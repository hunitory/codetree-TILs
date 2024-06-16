class person_info:
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city


n = int(input())

perple = []
for i in range(n):
    name, addr, city = input().split()
    perple.append(person_info(name, addr, city))

perple.sort(key=lambda x: x.name, reverse=True)

print(f'name {perple[0].name}')
print(f'addr {perple[0].addr}')
print(f'city {perple[0].city}')