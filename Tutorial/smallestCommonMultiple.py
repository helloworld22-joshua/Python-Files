import math

a = 355
b = 175

gcd = math.gcd(a, b)
lcm = abs(a * b) // gcd
print(gcd, lcm)

def nextPrime(prime):
    while True:
        prime += 1

        for i in range(2, prime):
            if prime % i == 0:
                break
        else:
            return prime

def primeFactorization(num):
    pri = 2
    exp = [0]

    while num > 1:
        if num % pri == 0:
            num /= pri
            exp[-1] += 1
        else:
            pri = nextPrime(pri)
            exp.append(0)

    return exp

def calculateGcd(a, b):
    a = primeFactorization(a)
    b = primeFactorization(b)

    pri = 2
    gcd = 1

    for i in range(min(len(a), len(b))):
        gcd *= pri ** min(a[i], b[i])

        pri = nextPrime(pri)

    return gcd

def calculateLcm(a, b):
    return a * b // calculateGcd(a, b)

print(calculateGcd(a, b), calculateLcm(a, b))