search = input()
target = input()

def find_target_index(search, target):
    search_len = len(search)
    target_len = len(target)

    for i in range(search_len):
        if search[i] == target[0]:
            cnt = 0
            for j in range(target_len):
                if search[i + j] == target[j]:
                    cnt += 1
            
            if cnt == target_len:
                return i
    
    return -1

print(find_target_index(search, target))