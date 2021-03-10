import json
import sys, getopt
import matplotlib.pyplot as plt
from get_graph_data import list_to_string

usage = """
usage: make_graphs_from_file.py -i <input file> [-d <decompositions] -p
Arguments:
-i        input filename: A string 
                          Should be a text file produced by
                          run_trials_to_file.py.
                          Lines alternate between metadata and data
-d        decompositions: A list of lists of ints
                          [optional]
                          Specify which decompositions to show in the graph
-p        whether to include loss of precision in the labels or not.
                          If -p is not an argument, this defaults to false
"""


# wrapper function to call whichever plot is correct
def make_plot(metadata, data, decompositions=None):
    if len(metadata) == 4:
        make_interp_plot_from_data(metadata, data, decompositions)
    else:
        make_decomp_plot_from_data(metadata, data, decompositions)

def make_decomp_plot_from_data(metadata, data, selected_decompositions):
    min_deg = metadata[0]
    max_deg = metadata[1]
    num_trials = metadata[2]
    interpolation = metadata[4]
    
    if selected_decompositions != None:
        decompositions = [dcmp for dcmp in metadata[3] if dcmp in selected_decompositions]
    else:
        decompositions = metadata[3]
    
    if len(decompositions) == 0:
        print("No valid decompositions selected. Not making a plot.")
        return
        
    
    algorithm_list_to_y_values = data
    
    # now plot
    degrees = range(min_deg, max_deg + 1)
    plt.figure(figsize=(16,8))
    for algorithm_list in [list_to_string(d) for d in decompositions]:
        plt.plot(degrees, algorithm_list_to_y_values[algorithm_list], 
                 lw=4, label=algorithm_list)

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
    print("Saving plot to " + auto_filename)
    
    return

def make_interp_plot_from_data(metadata, data, selected_decompositions):
    min_deg = metadata[0]
    max_deg = metadata[1]
    num_trials = metadata[2]
    decomposition = metadata[3]
    
    if selected_decompositions != None:
        decompositions = [dcmp for dcmp in metadata[3] if dcmp in selected_decompositions]
    else:
        decompositions = metadata[3]
        
    if len(decompositions) == 0:
        print("No valid decompositions selected. Not making a plot.")
        return
    
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
    print("Saving plot to " + auto_filename)
    
    return

def main(argv):
    input_filename = ""
    show_loss_of_precision = False
    decompositions = None
    
    try:
        opts, args = getopt.getopt(argv,"hpi:d:",["help="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h' or opt == "--help":
            print(usage)
            sys.exit()
        elif opt == '-i':
            input_filename = arg
        elif opt == '-d':
            decompositions = json.loads(arg)
        elif opt == '-p':
            show_loss_of_precision = True
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
            make_plot(metadata, data, decompositions)
    


if __name__ == "__main__":
    main(sys.argv[1:])