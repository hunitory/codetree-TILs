N = int(input())

def print_world(cnt):
    if cnt == 0 :
        return
    
    print('HelloWorld')
    print_world(cnt - 1)

print_world(N)