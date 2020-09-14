def fib_sequence(num):
    list_fib_terms = [1, 2]

    first = 1
    second = 2
    temp = second

    while first + second < num:
        temp = second
        second = first + second
        first = temp

        list_fib_terms.append(second)

    return list_fib_terms


fib_seq_4_mil = fib_sequence(4000000)
fib_seq_4_mil = list(filter(lambda x: x % 2 == 0, fib_seq_4_mil))
print(sum(fib_seq_4_mil))

