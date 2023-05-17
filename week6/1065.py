N = int(input())

target_list = []

def check(num):
    digit = len(str(num))
    
    diff_list = []
    for i in range(digit-1):
        diff = int(str(num)[i+1]) - int(str(num)[i])
        diff_list.append(diff)
    if all(x == diff_list[0] for x in diff_list):
        return True
    else:
        return False
    
for num in range(0, N):    
    if len(str(num)) == 1:
        if num != 0:
            target_list.append(True)
    # 두 자리 수 이상
    else:
        if check(num):
            target_list.append(True)
    
print(len(target_list))