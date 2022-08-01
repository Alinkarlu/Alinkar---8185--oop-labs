MAX_NUM = 3
product = 1
for i in range(1,MAX_NUM+1):
    product *= i
print(f"product of [1, {MAX_NUM}] is {product}")

sum_squares = 0
for i in range(1,MAX_NUM+1):
    i_sq = i ** 2
    sum_squares += i_sq
print(f"sum_squares of [1, {MAX_NUM}] is {sum_squares}")

nums = 0
for num in range(1,MAX_NUM+1):
    nums += num
print(f"sum of [1, {MAX_NUM}] is {nums}")