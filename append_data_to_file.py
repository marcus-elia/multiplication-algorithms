from get_graph_data import *
import json

def run_and_append_decomposition_data(min_deg, max_deg, num_trials, 
                            algorithms,  interpolation,
                            filename):
    data = compare_decompositions(min_deg, max_deg, num_trials, 
                            algorithms,  interpolation)
    metadata = [min_deg, max_deg, num_trials, algorithms, interpolation]
    
    f = open(filename, "a")
    f.write(json.dumps(metadata) + "\n")
    f.write(json.dumps(data) + "\n")
    f.close()
    return

def run_and_append_interpolation_data(min_deg, max_deg, num_trials, 
                            algorithm,
                            filename):
    data = compare_interpolations(min_deg, max_deg, num_trials, 
                            algorithm)
    metadata = [min_deg, max_deg, num_trials, algorithm]
    
    f = open(filename, "a")
    f.write(json.dumps(metadata) + "\n")
    f.write(json.dumps(data) + "\n")
    f.close()
    return