import numpy as np
import pandas as pd
import math

frame_of_1000 = np.genfromtxt('problem8.csv', delimiter=',')
list_of_1000 = []
temp_string = ""
i, product, max_product = 0, 0, 0
list_of_13 = [z for z in range(1, 14)]

# convert numPy array to array of string
frame_of_1000 = list(map(str, frame_of_1000))

# convert numPy array of strings to list of ints
for x in range(0, 20):
    temp_string = frame_of_1000[x]

    for y in range(0, len(temp_string)):

        if '0' <= temp_string[y] <= '9':
            list_of_1000.append(int(temp_string[y]))

while i != 987:

    product = math.prod(list_of_1000[i:i + 14])

    if max_product < product:
        max_product = product
        list_of_13 = list_of_1000[i:i + 14]

    i = i + 1

print(list_of_13)
print(max_product)

