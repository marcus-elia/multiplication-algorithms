from multiply import *
from get_graph_data import *
import json
import sys, getopt

usage = """
usage: find_ideal_decompositions.py -m <min sb degree> -M <max sb degree> -t <num trials>
                    -f <filename> [-s <start degree>]
                    
Find the best Toom decomposition for every degree until the program is
terminated. THIS PROGRAM WILL NOT STOP ON ITS OWN.
The idea is to use the same text file to store data from multiple runs. This will
only overwrite data if more trials are used now than were used previously.
The text file stores {degree: (ideal decomp, num trials)}
Arguments:
-m        min sb degree: The minimum degree for which it is worth considering
                        algorithms other than schoolbook (like 20 or 25).
-M        max sb degree: The maxmimum degree for which schoolbook is worth
                        considering (like 45 or 50).
-s        start degree: The degree to start searching at. Default is 10.
-f        filename:
-h        print usage string and exit
"""

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
    """
    Parameters
    ----------
    d : int.
    max_factor_size : int
        max n such that Toom-n is implemented.

    Returns
    -------
    List of lists
        Each list is a descending factorization of d.
        Example: when d = 24, n = 10, returns
        [[6,4],[6,2,2],[8,3]]

    """
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
    """
    Parameters
    ----------
    d : int
        degree of polynomials.
    max_factor_size : int
        the max value n for which Toom-n has been implemented
        It is 10 for me.
    min_sb_degree: int
        The minimum degree for which considering something other than 
        schoolbook is worth it.
    max_sb_degree: int
        The maxmimum degree for which considering schoolbook is worth it.

    Returns
    -------
    L : list of lists of ints
        Makes a list of all Toom-Cook decompositions worth considering
        at this value.

    """
    L = []
    splits = get_conceivable_total_splits(d, min_sb_degree, max_sb_degree)
    for split in splits:
        L = L + get_descending_factorizations(split, max_factor_size)
    return L

def determine_best_decomposition(d, max_factor_size,
                                 min_sb_degree, max_sb_degree, num_trials):
    """
    Parameters
    ----------
    d : int
        degree of polynomials.
    max_factor_size : int
        the max value n for which Toom-n has been implemented
        It is 10 for me.
    min_sb_degree: int
        The minimum degree for which considering something other than 
        schoolbook is worth it.
    max_sb_degree: int
        The maxmimum degree for which considering schoolbook is worth it.
    num_trials: int
        How many polynomial multiplications to do for each decomposition.

    Returns
    -------
    List.
        The fastest decomposition for multiplying degree d polynomials
    """
    
    decompositions = get_all_candidate_decompositions(d, max_factor_size,
                                                      min_sb_degree, max_sb_degree)
    if d <= max_sb_degree:
        decompositions.append([])
    
    decompositions = [tuple(algorithm_list) for algorithm_list in decompositions]
    
    print("Finding best decomposition for d = {} from {} candidates.".format(d, len(decompositions)))
        
    # a dictionary mapping each algorithm list to a dictionary mapping each
    # degree to the time sum for it
    algorithm_to_time_sum = {algorithm_list: 0 for algorithm_list in decompositions}
    
    # this is the outer loop so all variables will be affected equally by
    # slow outliers
    progress_time = time.time() # for the progress bar
    for _ in range(num_trials):
        f = [int(x) for x in np.random.randint(0, 2048, d)]
        g = [int(x) for x in np.random.randint(0, 2048, d)]
        for algorithm_list in decompositions:
            start_time = time.process_time()
            multiply(f, g, algorithm_list, "Efficient")
            total_time = time.process_time() - start_time
            algorithm_to_time_sum[algorithm_list] += total_time
                
        # progress bar
        if _ % (num_trials//10) == 0:
            x = _ // (num_trials//10)
            this_time = format_time(time.time()-progress_time)
            print("[" + "-"*x + " "*(10-x) + "]  " + str(this_time))
    print("[----------]  " + str(format_time(time.time()-progress_time)))
                
    # take the average
    algorithm_list_to_time = {algorithm_list :
        algorithm_to_time_sum[algorithm_list] / num_trials for algorithm_list in decompositions}
        
    winner = min(algorithm_list_to_time, key=algorithm_list_to_time.get)
    print("Best decomp is {}".format(winner))
    
    return min(algorithm_list_to_time, key=algorithm_list_to_time.get)


def main(argv):
    max_toom_n = 10
    min_sb_degree = 0
    max_sb_degree = 0
    num_trials = 0
    start_degree = 1
    filename = ""
    
    try:
        opts, args = getopt.getopt(argv,"hm:M:t:s:f:",["help="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h' or opt == "--help":
            print(usage)
            sys.exit()
        elif opt == '-m':
            min_sb_degree = int(arg)
        elif opt == '-M':
            max_sb_degree = int(arg)
        elif opt == '-t':
            num_trials = int(arg)
        elif opt == '-s':
            start_degree = int(arg)
        elif opt == '-f':
            filename = arg
        
    if min_sb_degree <= 0:
        print("Error: minimum schoolbook degree not specified or invalid")
        print(usage)
        sys.exit(1)
    if max_sb_degree <= min_sb_degree:
        print("Error: max schoolbook degree not specified or invalid")
        print(usage)
        sys.exit(1)
    if num_trials <= 0:
        print("Error: num trials not specified or invalid")
        print(usage)
        sys.exit(1)
    if filename == "":
        print("Error: filename not specified")
        print(usage)
        sys.exit(1)
    
    # read in the existing data
    try:
        f = open(filename, 'r')
        existing = f.readline()
        f.close()
    except FileNotFoundError:
        f = open(filename, 'w')
        f.close()
        existing = {}
    if existing:
        previous_results = json.loads(existing)
    else:
        previous_results = {}
    
    d = start_degree
    while True:
        # if we don't need to redo this degree
        if d in previous_results and previous_results[d][1] > num_trials:
            d += 1
            continue
        else:
            # get the best decomp for this degree
            best_decomp = determine_best_decomposition(d, max_toom_n,
                                 min_sb_degree, max_sb_degree, num_trials)
            previous_results[d] = (best_decomp, num_trials)
            
            # overwrite the file
            f = open(filename, 'w')
            f.write(json.dumps(previous_results))
            f.close()
            d += 1

if __name__ == "__main__":
    main(sys.argv[1:])
                  