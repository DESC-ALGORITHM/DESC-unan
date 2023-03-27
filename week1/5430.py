import sys
from collections import deque

test_num = int(sys.stdin.readline())

for _ in range(test_num):
    funcs = deque(sys.stdin.readline().rstrip())
    arr_size = int(sys.stdin.readline())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    
    if arr_size == 0:
        arr = deque()
    else:
        arr = deque(arr)
    is_error = False
    reversed_count = 0
    for func in funcs:
        if func == "R":
            reversed_count += 1
        elif func =="D":
            if len(arr) == 0:
                is_error = True
                break
            else:
                if reversed_count % 2 == 1:
                    arr.pop()
                else:
                    arr.popleft()                

    if is_error:
        print("error")
    else:
        if reversed_count % 2 == 1:
            arr.reverse()   
        print("[" + ",".join(list(arr)) + "]")