import pandas as pd
import numpy as np

num = 0
keep_going = True

while keep_going:
    num += 20
    count = 0

    for x in range(20, 10, -1):

        if num % x == 0:
            count += 2

    if count == 20:
        keep_going = False
        break

print(num)


