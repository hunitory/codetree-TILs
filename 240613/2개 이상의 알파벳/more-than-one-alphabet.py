A = input()

def check(A):
    main = A[0]
    for a in A:
        if main != a:
            return "Yes"
    
    return "No"

print(check(A))