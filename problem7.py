def sieve_of_eratosthenes(num):  # same algorithm but different parameter

    prime_list = [i for i in range(2, num)]

    p = 2

    while p * p < num:

        for x in range(p + 1, len(prime_list)):

            if prime_list[x] % p == 0:
                prime_list[x] = 0

        p += 1

    return list(filter(lambda b: b != 0, prime_list))


index = 10001

list_of_primes = sieve_of_eratosthenes(200000)
print(list_of_primes[index])
