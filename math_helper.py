def factorial(n):
    if n < 2:
        return 1
    return n*factorial(n-1)

def binomial(n, k):
    rval = 1
    for i in range(k + 1, n + 1):
        rval *= i
    return rval // factorial(n - k)

def exp(a, b):
    prod = 1
    for _ in range(b):
        prod *= a
    return prod

def ind_e(n, L, b):
    return (L-1)*n - (L+1)*(L+2)//2 + 3 + b
def ind_o(n, L, b):
    return (L-1)*(n+1) - (L+1)*(L+2)//2 + 3 + b
def denominator(L, b):
    return 2*(L-1)*b + exp((L-1), 2)

# A shortcut for t_2 since it has an explicit closed form on OEIS
def t_2(n, k):
    return 2 * sum([exp((-1), (j+k+1)) * binomial(2*k, j+k+1) * exp(j+1, 2*n) for j in range(k)]) // factorial(2*k)

# Compute the n,k entry of the t_b triangle
def t(n, k, b):
    if n == 1 or n == k or k == 1:
        return 1
    if k < 1 or k > n:
        return 0
    return t(n-1, k-1, b) + exp((k + b - 2), 2) * t(n-1, k, b)