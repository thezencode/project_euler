import math
import time

start = time.time()
num = 24
largestFact = 0
factors = [0, 0]
isPrime = True
i = 2

while i * i < num:
    if num % i == 0:
        factors[0] = i
        factors[1] = num / i

        for k in range(0, 2):
            isPrime = True
            j = 2

            while j*j < factors[k]:
                if factors[k] % j == 0:
                    isPrime = False
                    break

                j += 1

            if isPrime and factors[k] > largestFact:
                largestFact = factors[k]

    i += 1

end = time.time()

print(f'{largestFact} is the largest prime factor of {num}.')
print(f'The program takes {(end - start)*1000} milliseconds to run.')

