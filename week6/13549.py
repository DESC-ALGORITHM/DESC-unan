from collections import deque

MAX = 100001
n, k = map(int, input().split())
array = [0] * MAX

def bfs():
    q = deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos == k:
            return array[now_pos]
        for next_pos in (now_pos - 1, now_pos + 1, 2 * now_pos):
            if 0 <= next_pos < MAX and not array[next_pos]:
                if next_pos == 2 * now_pos and now_pos != 0:
                    array[next_pos] = array[now_pos]
                    q.appendleft(next_pos)
                else:
                    array[next_pos] = array[now_pos] + 1
                    q.append(next_pos)
print(bfs())