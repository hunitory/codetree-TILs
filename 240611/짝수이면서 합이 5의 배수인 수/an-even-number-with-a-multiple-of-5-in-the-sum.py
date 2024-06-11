n = input()

if int(n) % 2 == 0 and (int(n[1]) + int(n[0])) % 5 == 0:
    print('Yes')
else:
    print("No")