#! /usr/bin/env python3
## Need operator for reduce functions
import operator as op
import functools
# Establish probability
def ncr(n, r):

    # Min = return smaller of the two arguments
    r = min(r, n-r)
    if r == 0: return 1
    # Reduce = do function (arg 1) across all of arg 2 cumulatively

    numer = functools.reduce(op.mul, range(n, n-r, -1))
    denom = functools.reduce(op.mul, range(1, r+1))
    return numer // denom

# Pow = Exponential function
N = pow(2, int(input("Enter k:\n")))
K = int(input("Enter N:\n"))

acc = 0

for i in range(K, N + 1):
    combinations = ncr(N,i)
    success = pow(0.25, i)
    failure = pow(0.75, N - i)
    acc += (combinations * success * failure)


# round(x, y) = round x to the floating point decimal y places in
print(round(acc, 3))
