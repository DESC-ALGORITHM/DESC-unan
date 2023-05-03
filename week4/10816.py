import sys
from collections import Counter

N = int(sys.stdin.readline())
my_cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
find_cards = list(map(int, sys.stdin.readline().split()))

my_cards_counter = Counter(my_cards)


answer = []

for num in find_cards:
    if my_cards_counter[num]:
        answer.append(my_cards_counter[num])

    else:
        answer.append(0)

print(" ".join(str(n) for n in answer))
