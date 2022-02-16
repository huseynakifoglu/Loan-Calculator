# the following line reads the list from the input, do not modify it, please
old_list = [int(num) for num in input().split()]

binary_list = []
for dig in old_list:
    if dig > 0:
        binary_list.append(int("1"))
    elif dig <= 0:
        binary_list.append(int("0"))
print(binary_list)
