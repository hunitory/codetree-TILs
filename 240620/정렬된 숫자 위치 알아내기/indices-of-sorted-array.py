# 클래스 선언
class Number:
    def __init__(self, number, index):
        self.number, self.index = number, index


# 변수 선언 및 입력
n = int(input())
numbers = []
arr = list(map(int, input().split()))
numbers = [
    Number(num, i)
    for i, num in enumerate(arr)
]
answer = [
    0 for _ in range(n)
]

# Custom Comparator를 활용한 정렬
numbers.sort(key=lambda x: (x.number, x.index))

# 정렬된 숫자들의 원래 인덱스를 활용한 정답 배열 저장
for i, number in enumerate(numbers):
    answer[number.index] = i + 1 # 인덱스 보정

# 출력
for i in range(n):
    print(answer[i], end = ' ')