import time


def triangle_number(n):
    triangle_sum = 0
    for i in range(1, n + 1):
        triangle_sum += i
    return triangle_sum


def return_num_divisors(m):
    num_factors = 0
    i = 1

    while i * i <= m:
        if m % i == 0:
            num_factors += 1
        i += 1

    return 2 * num_factors


start = time.time()

curr_index = 1
curr_tri_num = triangle_number(curr_index)
curr_num_factors = return_num_divisors(curr_tri_num)

while curr_num_factors < 500:
    curr_index += 1
    curr_tri_num = triangle_number(curr_index)
    curr_num_factors = return_num_divisors(curr_tri_num)

end = time.time()

print(curr_index, curr_tri_num)
print(f'The program takes {end - start} seconds to run.')
