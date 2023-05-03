import sys

def binary_search(trees, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = sum([tree - mid if tree > mid else 0 for tree in trees])

        if total >= target:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

def main():
    N, M = map(int, sys.stdin.readline().split())
    trees = list(map(int, sys.stdin.readline().split()))

    start = 0
    end = max(trees)

    print(binary_search(trees, M, start, end))

if __name__ == "__main__":
    main()
