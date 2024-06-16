class bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second
        print(f'code : {code}')
        print(f'color : {color}')
        print(f'second : {second}')
    
code, color, second = input().split()

bomb1 = bomb(code, color, second)