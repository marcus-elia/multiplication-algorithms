from append_data_to_file import *
import sys, getopt

usage = """
usage: append_data_to_file.py -i <input file> -o <output file> 
Read parameter sets from input file, run algorithm comparisons,
and write the data to output file.
Arguments:
-i        input filename: A string 
-o        output filename: A string
-a        append, but do not overwrite output file
-h        print usage string and exit
"""

def read_commands(filename):
    """
    Parameters
    ----------
    filename : string
        Text file containing one command per line.
        Example line: [100, 200, 500, [[4,3,2], [10]], 0]
        0 = "Natural"
        1 = "Efficient"
        2 = "Matrix"

    Returns
    -------
    List of lists, where each list specifies a parameter set.

    """
    parameter_sets = []
    
    f = open(filename, "r")
    for line in f:
        parameter_sets.append(json.loads(line))
    f.close()
    
    return parameter_sets


def main(argv):
    input_filename = ""
    output_filename = ""
    overwrite = True
    
    try:
        opts, args = getopt.getopt(argv,"hai:o:",["help="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h' or opt == "--help":
            print(usage)
            sys.exit()
        elif opt == '-i':
            input_filename = arg
        elif opt == '-o':
            output_filename = arg
        elif opt == '-a':
            overwrite = False
        else:
            print(usage)
            sys.exit()
    
    code_to_interp = {0:"Natural", 1:"Efficient", 2:"Matrix"}
    
    # overwrite output file
    if overwrite:
        f = open(output_filename, 'w')
        f.close()
            
    parameter_sets = read_commands(input_filename)
    for parameter_set in parameter_sets:
        min_deg = parameter_set[0]
        max_deg = parameter_set[1]
        num_trials = parameter_set[2]
        decomposition_list = parameter_set[3]
        if len(parameter_set) == 5:
            try:
                interpolation = code_to_interp[int(parameter_set[4])]
            except ValueError:
                interpolation = parameter_set[4]
        else:
            interpolation = None
        
        # if an interpolation is specified
        if interpolation:
            print("Running Decomp Comparison on {}-{}, {} trials, {}, {}".format(min_deg, max_deg, num_trials, decomposition_list, interpolation))
            run_and_append_decomposition_data(min_deg, max_deg, num_trials,
                                              decomposition_list, interpolation,
                                              output_filename)
        else:
            print("Running Interp Comparison on {}-{}, {} trials, {}".format(min_deg, max_deg, num_trials, decomposition_list))
            run_and_append_interpolation_data(min_deg, max_deg, num_trials,
                                              decomposition_list,
                                              output_filename)


if __name__ == "__main__":
    main(sys.argv[1:])