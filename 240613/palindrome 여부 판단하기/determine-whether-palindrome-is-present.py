st = input()

def check_palindrome(s):
    if s == s[::-1]:
        return "Yes"
    return "No"

print(check_palindrome(st))