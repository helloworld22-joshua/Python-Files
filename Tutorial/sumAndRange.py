sum = 0                             # Sum is like a for loop with range

for n in range(2, 9 + 1):           # Go to this value       ->  9
    n *= 3                          # What to sum (n)        ->  Σ n * 3  =  6 + 9 + 12 + 15 + 18 + 21 + 24 + 27 = 132
    sum += n                        # Starting at this value -> n=2
    print(n)

print("Sum: ", sum)                 # Go here to compare: https://www.mathsisfun.com/numbers/sigma-calculator.html