# -*- coding: utf-8 -*-
from multiply import *
import sys

def test_schoolbook_multiply():
    
    # multiply the corresponding f's and g's
    fs = [[1,2], [8, -3, 0, 5], [0], [1,10,-8]]
    gs = [[1,2], [1], [5,5], [-4,0,3]]
    
    # the true products
    answers = [[1,4,4], [8, -3, 0, 5], [0,0], [-4, -40, 35, 30, -24]] 
    
    for i in xrange(len(fs)):
        assert schoolbook(fs[i], gs[i]) == answers[i]

def test_algorithms(interpolation_method, min_degree=30, max_degree=150):
    for poly_length in xrange(min_degree, max_degree+1):
        for algorithm_list in [[], [2], [3], [4], [5], [6],
                               [7], [8], [9], [10], [2,2],
                               [5,2], [2,2,2], [1]]:
            f = [int(x) for x in np.random.randint(-100, 100,
                                                    size=poly_length)]
            g = [int(x) for x in np.random.randint(-100, 100, 
                                                    size=poly_length)]
            assert schoolbook(f,g) == multiply(f, g, algorithm_list, 
                                               interpolation_method)


def main(argv):
    test_schoolbook_multiply();
    test_algorithms('Natural', max_degree=80)
    test_algorithms('Efficient', max_degree=80)
    test_algorithms('Matrix', max_degree=80)
    print "Done testing."


if __name__ == "__main__":
    main(sys.argv[1:])