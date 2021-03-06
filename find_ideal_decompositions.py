from multiply import *

def get_factors(a):
    """
    Parameters
    ----------
    a : int
        A positive integer.

    Returns
    -------
    The distinct factors of a in decreasing order.

    """
    factors = [a]
    i = a//2 + 1
    while i > 1:
        if a % i == 0:
            factors.append(i)
        i -= 1
    return factors

def get_conceivable_total_splits(degree, min_sb_degree, max_sb_degree):
    """
    Parameters
    ----------
    degree : int
        A positive integer representing the degree of
        polynomials to be multiplied.
    min_sb_degree: int
        The minimum degree for which considering something other than 
        schoolbook is worth it.
    max_sb_degree: int
        The maxmimum degree for which considering schoolbook is worth it.

    Returns
    -------
    List of ints representing possible total Toom split amounts to try.
    For example, if degree = 200, min_sb_degree = 20, max_sb_degree = 50,
    then this should return [6, 7, 8, 9, 10]

    """
    smallest = degree // max_sb_degree
    largest = degree // min_sb_degree
    return range(smallest, largest + 1)

def get_descending_factorizations(d, max_factor_size):
    if d < 2:
        return []
    elif d == 2:
        return [[2]];
    elif d == 3:
        return [[3]];
    else:
        L = []
        factors = get_factors(d)
        for factor in factors:
            if factor > max_factor_size:
                continue
            else:
                factorizations = get_descending_factorizations(d//factor, max_factor_size)
                for factorization in factorizations:
                    if not factorization:
                        L.append([factor])
                    elif factorization[0] <= factor:
                        L.append([factor] + factorization)
    if d <= max_factor_size:
        L = [[d]] + L
    return L

def get_all_candidate_decompositions(d, max_factor_size, min_sb_degree, max_sb_degree):
    L = []
    splits = get_conceivable_total_splits(d, min_sb_degree, max_sb_degree)
    for split in splits:
        L = L + get_descending_factorizations(split, max_factor_size)
    return L

if __name__ == "__main__":
    print(get_all_candidate_decompositions(120, 10, 20, 50))
                  