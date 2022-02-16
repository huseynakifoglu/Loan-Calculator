num = [x for x in input()]
result = []
my_sum = 0
for i in range(len(num)):
    my_sum += int(num[i])
    result.append(my_sum)
result_int = [int(i) for i in result]
print(result_int)
