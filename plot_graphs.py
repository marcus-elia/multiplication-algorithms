# -*- coding: utf-8 -*-

#from multiply import *
from get_graph_data import *
import matplotlib.pyplot as plt
import time
import json
import sys, getopt

usage = """
usage: plot_graphs.py -m <min degree> -M <max degree> -t <num trials>
                    -a <algorithm list> -i <interpolation method>
                    [-f <filename>]
Either compare multiple decompositions with the same 
        interpolation method, or compare the same decomposition
        with different interpolation methods.
Arguments:
-a        algorithm list: A string containing a list of lists.
                Example: "[[1], [4,2,2], [10,3], [7]]"
-i        interpolation method: "Natural" or "Efficient" or "Matrix"
                If interpolation method is blank and algorithm list has one
                element, then it compares the same decomposition with all
                three interpolation methods
-f        filename (optional): specify the filename to save the image
                If not specified, a file name will be auto-generated
                based on the algorithm list
-h        print usage string and exit
"""


# -----------------------------
# =============================
#
#         Plotting
#
# =============================
# -----------------------------
def plot_compare_decompositions(min_deg, max_deg, num_trials, 
                            algorithms,  interpolation,
                            filename=""):
    
    # Run the trials to get data
    algorithm_list_to_y_values = compare_decompositions(min_deg, max_deg, num_trials, 
                            algorithms,  interpolation)
    
    # now plot
    degrees = range(min_deg, max_deg + 1)
    plt.figure(figsize=(16,8))
    for algorithm_list in algorithm_list_to_y_values:
        plt.plot(degrees, algorithm_list_to_y_values[algorithm_list], 
                 lw=4, label=list_to_string(algorithm_list))

    plt.xlabel("Degree", size=19)
    plt.ylabel("Average CPU Time (seconds)", size=19)
    plt.legend(fontsize=18)
    plt.title("Comparison of Toom-Cook Decompositions", size=20)
    if filename != "":
        plt.savefig(filename, bbox_inches='tight')
    else:
        auto_filename = "decomp_plot"
        for algorithm_list in algorithms:
            auto_filename += "_" + list_to_string(algorithm_list)
        auto_filename += "_m" + str(min_deg) + "_M" + str(max_deg) + "_t" + str(num_trials)
        auto_filename += ".jpg"
        plt.savefig(auto_filename, bbox_inches='tight')
    
    return

def plot_compare_interpolations(min_deg, max_deg, num_trials, 
                            algorithm_list,
                            filename=""):
    
    # Run the trials to get data
    interpolation_to_y_values = compare_interpolations(min_deg, max_deg, num_trials, 
                            algorithm_list)
    
    # now plot
    degrees = range(min_deg, max_deg + 1)
    plt.figure(figsize=(16,8))
    for interpolation in interpolation_to_y_values:
        plt.plot(degrees, interpolation_to_y_values[interpolation], 
                 lw=4, label=interpolation)

    plt.xlabel("Degree", size=19)
    plt.ylabel("Average CPU Time (seconds)", size=19)
    plt.legend(fontsize=18)
    plt.title("Comparison of Interpolation Methods for Toom-" + list_to_string(algorithm_list), size=20)
    if filename != "":
        plt.savefig(filename, bbox_inches='tight')
    else:
        auto_filename = "interp_plot"
        auto_filename += "_" + list_to_string(algorithm_list)
        auto_filename += "_m" + str(min_deg) + "_M" + str(max_deg) + "_t" + str(num_trials)
        auto_filename += ".jpg"
        plt.savefig(auto_filename, bbox_inches='tight')
    
    return


def main(argv):
    min_degree = 0
    max_degree = 0
    num_trials = 0
    algorithm_list = []
    interpolation_method = ""
    input_filename = ""
    
    try:
        opts, args = getopt.getopt(argv,"hm:M:t:a:i:f:",["help="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h' or opt == "--help":
            print(usage)
            sys.exit()
        elif opt == '-m':
            min_degree = int(arg)
        elif opt == '-M':
            max_degree = int(arg)
        elif opt == '-t':
            num_trials = int(arg)
        elif opt == '-a':
            algorithm_list = json.loads(arg)
        elif opt == '-i':
            interpolation_method = arg
        elif opt == '-f':
            input_filename = arg

    if min_degree <= 0:
        print("Error: minimum degree not specified or invalid")
        print(usage)
        sys.exit(1)
    if max_degree <= min_degree:
        print("Error: max degree not specified or invalid")
        print(usage)
        sys.exit(1)
    if num_trials <= 0:
        print("Error: num trials not specified or invalid")
        print(usage)
        sys.exit(1)
    if algorithm_list == []:
        print("Error: algorithm list cannot be empty")
        print(usage)
        sys.exit(1)
    if len(algorithm_list) > 1 and interpolation_method == "":
        print("Error: cannot compare interpolation methods with multiple decompositions")
        print(usage)
        sys.exit(1)
    if interpolation_method != "" and not interpolation_method in ("Natural", "Efficient", "Matrix"):
        print(interpolation_method)
        print("Error: invalid interpolation method")
        print(usage)
        sys.exit(1)
    
    if len(algorithm_list) >= 1 and interpolation_method != "":
        plot_compare_decompositions(min_degree, max_degree, num_trials, 
                            algorithm_list, interpolation_method,
                            filename=input_filename)
    elif len(algorithm_list) == 1 and interpolation_method == "":
        plot_compare_interpolations(min_degree, max_degree, num_trials, 
                               algorithm_list[0],
                               filename=input_filename)
    else:
        print("Error: some invalid combination of algorithm list and interpolation method")
        print(usage)
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])



