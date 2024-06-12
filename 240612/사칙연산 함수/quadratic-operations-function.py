a, o, c = map(str, input().split())

if o == '/':
    print(int(int(a) / int(c)))
elif o == '+':
    print(f'{int(a)} + {int(c)} = {int(a) + int(c)}')
elif o == '-':
    print(int(a) - int(c))
elif o == '*':
    print(f'{int(a)} * {int(c)} = {int(a) * int(c)}')