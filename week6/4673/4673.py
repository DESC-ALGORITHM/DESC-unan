num_set = set(i for i in range(1,10001))
d_set = set()
result = 0

for i in range(1, 10000):
    length = len(str(i))
    num = str(i)

    for idx in range(length):
        result += int(num[idx])
    result += int(num)

    d_set.add(result)
    result = 0

result_set = num_set - d_set
result_list = sorted(list(result_set))
for x in result_list:
    print(x)


    