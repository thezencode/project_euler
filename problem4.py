term_1 = range(100, 999)
term_2 = range(100, 999)
max_result = 0
stored_x = 0
stored_y = 0


def is_palindromic_number(number):
    str_num = str(number)
    if str_num[::] == str_num[::-1]:
        return True
    else:
        return False


for x in term_1:

    for y in term_2:

        result = x * y

        if is_palindromic_number(result) and result > max_result:

            max_result = result
            stored_x, stored_y = x, y

print(stored_x, stored_y, max_result)
