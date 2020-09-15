import math
import time


def is_prime(n):
    for x in range(2, int(math.sqrt(n)) + 1):
        if n % x == 0:
            return False

    return True


def return_prime_factors(a_number):
    factors = [a_number]

    while True:

        if is_prime(factors[0]):
            break

        for i in range(2, int(factors[0])):

            if factors[0] % i == 0:

                factors[0] = factors[0] / i
                factors.append(i)
                break

    return int(max(factors))


start = time.time()
print(return_prime_factors(600851475143))
end = time.time()
print(f"This program takes {end - start} seconds to run.")




