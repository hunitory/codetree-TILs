a, o, c = map(str, input().split())

if o == '/':
    print(f'{int(a)} / {int(c)} = int(int(a) / int(c))')
elif o == '+':
    print(f'{int(a)} + {int(c)} = {int(a) + int(c)}')
elif o == '-':
    print(f'{int(a)} - {int(c)} = {int(a) - int(c)}')
elif o == '*':
    print(f'{int(a)} * {int(c)} = {int(a) * int(c)}')
else:
    print('False')