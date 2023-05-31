import math

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # 두 원의 중심 사이의 거리
    
    if d == 0 and r1 == r2:
        print(-1)
    elif abs(r1 - r2) == d or r1 + r2 == d:
        print(1)
    elif abs(r1 - r2) < d < r1 + r2:
        print(2)
    else:
        print(0)