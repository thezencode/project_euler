max_int = 0

for a in range(999, 100, -1):

    for b in range(999, 100, -1):

        x = a * b

        if x > max_int:

            s = str(a * b)

            if s == s[::-1]:

                max_int = a * b
print(max_int)


