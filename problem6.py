
first_100_NN = [x for x in range(1, 101)]
sum_of_squares = sum([x*x for x in first_100_NN])
square_of_sums = sum(first_100_NN)*sum(first_100_NN)
diff = square_of_sums - sum_of_squares
print(diff)
