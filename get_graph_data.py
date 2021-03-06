from multiply import *
import time

# -----------------------------
# =============================
#
#      Helper Functions
#
# =============================
# -----------------------------

def format_time(x):
    if x < 60:
        return str(int(x)) + " seconds"
    elif x < 3600:
        return str(int(x//60)) + "." + str(int((x-60*(x//60))/60*10)) + " minutes"
    else:
        return str(int(x//3600)) + "." + str(int((x-3600*(x//3600))/3600*10)) + " hours"
    
def list_to_string(algorithm_list):
    """ Converts a list of ints into a string with a dash between
        each character"""
    if not algorithm_list:
        return "SB"
    if len(algorithm_list) == 1:
        return str(algorithm_list[0])
    s = str(algorithm_list[0])
    for n in algorithm_list[1:-1]:
        s += '-'
        s += str(n)
    return s + '-' + str(algorithm_list[-1])

# -----------------------------
# =============================
#
#      Generating Data
#
# =============================
# -----------------------------
def compare_decompositions(min_deg, max_deg, num_trials, 
                            algorithms,  interpolation):
    """
    Parameters
    ----------
    min_deg : int
        > 0.
    max_deg : int
        > min_deg.
    num_trials : int
        > 0.
    algorithms : List of lists of ints
        Example: [[4,3,2], [], [10]].
    interpolation : String
        "Natural", "Efficient", "Matrix".

    Returns
    -------
    Dictionary mapping each decomposition to a list of average
    CPU times (entry 0 corresponds to min_deg, last entry
    corresponds to max_deg)

    """
    algorithms = [tuple(algorithm_list) for algorithm_list in algorithms]
    
    # the degrees (x-values)
    degrees = range(min_deg, max_deg+1)
    
    # a dictionary mapping each algorithm list to a dictionary mapping each
    # degree to the time sum for it
    algorithm_to_time_sum = {algorithm_list: {degree:0 for degree in degrees} 
                             for algorithm_list in algorithms}
    
    # this is the outer loop so all variables will be affected equally by
    # slow outliers
    progress_time = time.time() # for the progress bar
    for _ in range(num_trials):
        for degree in degrees:
            f = [int(x) for x in np.random.randint(0, 2048, degree)]
            g = [int(x) for x in np.random.randint(0, 2048, degree)]
            for algorithm_list in algorithms:
                start_time = time.process_time()
                multiply(f, g, algorithm_list, interpolation)
                total_time = time.process_time() - start_time
                algorithm_to_time_sum[algorithm_list][degree] += total_time
                
        # progress bar
        if _ % (num_trials//10) == 0:
            x = _ // (num_trials//10)
            this_time = format_time(time.time()-progress_time)
            print("[" + "-"*x + " "*(10-x) + "]  " + str(this_time))
    print("[----------]  " + str(format_time(time.time()-progress_time)))
                
    # take the average
    algorithm_list_to_y_values = {algorithm_list :
        [algorithm_to_time_sum[algorithm_list][degree]/num_trials for 
         degree in degrees] for algorithm_list in algorithms}
    
    return algorithm_list_to_y_values

def compare_interpolations(min_deg, max_deg, num_trials, 
                            algorithm_list,
                            filename=""):
    """
    Parameters
    ----------
    min_deg : int
        > 0.
    max_deg : int
        > min_deg.
    num_trials : int
        > 0.
    algorithm_list : a single list of ints
        Example: [4,3,2].

    Returns
    -------
    Dictionary mapping each interpolation to a list of average
    CPU times (entry 0 corresponds to min_deg, last entry
    corresponds to max_deg)

    """
    interpolations = ("Natural", "Efficient", "Matrix")
    
    # the degrees (x-values)
    degrees = range(min_deg, max_deg+1)
    
    # a dictionary mapping each algorithm list to a dictionary mapping each
    # degree to the time sum for it
    interpolation_to_time_sum = {interpolation: {degree:0 for degree in degrees} 
                             for interpolation in interpolations}
    
    # this is the outer loop so all variables will be affected equally by
    # slow outliers
    progress_time = time.time() # for the progress bar
    for _ in range(num_trials):
        for degree in degrees:
            f = [int(x) for x in np.random.randint(0, 2048, degree)]
            g = [int(x) for x in np.random.randint(0, 2048, degree)]
            for interpolation in interpolations:
                start_time = time.process_time()
                multiply(f, g, [algorithm_list], interpolation)
                total_time = time.process_time() - start_time
                interpolation_to_time_sum[interpolation][degree] += total_time
                
        # progress bar
        if _ % (num_trials//10) == 0:
            x = _ // (num_trials//10)
            this_time = format_time(time.time()-progress_time)
            print("[" + "-"*x + " "*(10-x) + "]  " + str(this_time))
    print("[----------]  " + str(format_time(time.time()-progress_time)))
                
    # take the average
    interpolation_to_y_values = {interpolation :
        [interpolation_to_time_sum[interpolation][degree]/num_trials for 
         degree in degrees] for interpolation in interpolations}
    
    return interpolation_to_y_values