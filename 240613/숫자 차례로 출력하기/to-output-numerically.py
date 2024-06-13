N = int(input())

def st(n):
    if n == 0:
        print()
        return

    print(N- n + 1,end=" ")
    st(n - 1)

def st2(n):
    if n == 0:
        return

    print(n, end=" ")
    st2(n - 1)


st(N)
st2(N)