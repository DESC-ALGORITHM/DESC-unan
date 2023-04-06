import sys

# N은 100000개
N = int(sys.stdin.readline())

f_list = []

for _ in range(N):
    f = int(sys.stdin.readline())
    f_list.append(f)

f_list.sort()
result = 0
init_length = len(f_list)

# ! Idea
# 모든 로프를 사용할 때의 최대 하중을 시작으로, 로프 한개씩 줄여가면서 최대 하중을 업데이트 해준다.
while len(f_list) > 0:
    new_f = init_length * min(f_list)

    if new_f >= result:
        result = new_f
    f_list.pop(0)
    init_length -= 1

print(result)