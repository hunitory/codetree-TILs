n, m = map(int, input().split())

n_arr = list(map(int, input().split()))

m_arr = [tuple(map(int, input().split())) for _ in range(m)]

for s, e in m_arr:
    print(sum(n_arr[s-1 :e]))