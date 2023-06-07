import sys

def binary_search(array, target, start, end):
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        end = min - 1
    else:
        start = mid + 1
    return None

N = int(sys.stdin.readline().rstrip())
N_list = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
M_list = list(map(int, sys.stdin.readline().rstrip().split()))

N_list.sort()

for i in M_list:
    result = binary_search(N_list, i, 0, N - 1)
    if result != None
        print("yes", end = ' ')
    else:
        print("no", end = ' ')