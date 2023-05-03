import sys

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

def main():
    n = int(sys.stdin.readline())
    cards = list(map(int, sys.stdin.readline().split()))
    cards.sort()

    m = int(sys.stdin.readline())
    targets = list(map(int, sys.stdin.readline().split()))

    for target in targets:
        if binary_search(cards, target, 0, n - 1):
            print(1, end=" ")
        else:
            print(0, end=" ")

if __name__ == "__main__":
    main()
