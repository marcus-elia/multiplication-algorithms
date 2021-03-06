import json
import sys, getopt
import matplotlib.pyplot as plt
from get_graph_data import list_to_string

usage = """
usage: make_graphs_from_file.py -i <input file>
Arguments:
-i        input filename: A string 
                          Should be a text file produced by
                          run_trials_to_file.py.
                          Lines alternate between metadata and data
"""


# wrapper function to call whichever plot is correct
def make_plot(metadata, data):
    if len(metadata) == 4:
        make_interp_plot_from_data(metadata, data)
    else:
        make_decomp_plot_from_data(metadata, data)

def make_decomp_plot_from_data(metadata, data):
    min_deg = metadata[0]
    max_deg = metadata[1]
    num_trials = metadata[2]
    decompositions = metadata[3]
    interpolation = metadata[4]
    
    algorithm_list_to_y_values = data
    
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
   
    auto_filename = "decomp_plot"
    for algorithm_list in decompositions:
        auto_filename += "_" + list_to_string(algorithm_list)
    auto_filename += "_m" + str(min_deg) + "_M" + str(max_deg) + "_t" + str(num_trials)
    auto_filename += ".jpg"
    plt.savefig(auto_filename, bbox_inches='tight')
    
    return

def make_interp_plot_from_data(metadata, data):
    min_deg = metadata[0]
    max_deg = metadata[1]
    num_trials = metadata[2]
    decomposition = metadata[3]
    
    interpolation_to_y_values = data
    
    # now plot
    degrees = range(min_deg, max_deg + 1)
    plt.figure(figsize=(16,8))
    for interpolation in interpolation_to_y_values:
        plt.plot(degrees, interpolation_to_y_values[interpolation], 
                 lw=4, label=interpolation)

    plt.xlabel("Degree", size=19)
    plt.ylabel("Average CPU Time (seconds)", size=19)
    plt.legend(fontsize=18)
    plt.title("Comparison of Interpolation Methods for Toom-" + list_to_string(decomposition), size=20)
   
    auto_filename = "interp_plot"
    auto_filename += "_" + list_to_string(decomposition)
    auto_filename += "_m" + str(min_deg) + "_M" + str(max_deg) + "_t" + str(num_trials)
    auto_filename += ".jpg"
    plt.savefig(auto_filename, bbox_inches='tight')
    
    return

def main(argv):
    input_filename = ""
    try:
        opts, args = getopt.getopt(argv,"hi:",["help="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h' or opt == "--help":
            print(usage)
            sys.exit()
        elif opt == '-i':
            input_filename = arg
        else:
            print(usage)
            sys.exit()
    
    f = open(input_filename, 'r')
    is_data_line = False # lines alternate between metadata and data
    for line in f:
        if not is_data_line:
            metadata = json.loads(line)
            is_data_line = True
        else:
            data = json.loads(line)
            is_data_line = False
            make_plot(metadata, data)
    


if __name__ == "__main__":
    main(sys.argv[1:])