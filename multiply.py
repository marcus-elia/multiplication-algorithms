# -*- coding: utf-8 -*-
import numpy as np
#from natural_interpolation import solve_for_coefficients_natural
#from efficient_interpolation import solve_for_coefficients_efficient
#from matrix_interpolation import solve_for_coefficients_matrix
from auto_generated_efficient_formulas import *
from auto_generated_natural_formulas import *
from auto_generated_matrix_formulas import *


def multiply(f, g, algorithm, interpolation):
    """ This multiplies f and g. algorithm_list specifies how.
        If algorithm_list is a list of valid ints, then we recursively 
        multiply until the end of the list, at which point we use 
        schoolbook.  Also, 1 means schoolbook.
        interpolation is in ("Matrix", "Natural", "Efficient")"""
       
    if len(f) != len(g):
        raise ValueError("Can only multiply polys of the same length")
        
    # do schoolbook multiplication if the list is empty
    if len(algorithm) == 0 or algorithm[0] == 1:
        return schoolbook(f, g)
     
    n = algorithm[0]
    next_alg = algorithm[1:]
            
    fblocks = split(f, n)
    gblocks = split(g, n)
    
    # the list of evaluating numbers
    eval_list =  make_eval_list(n)
    
    # plug the numbers in
    f_eval = evaluate_blocks_list(fblocks, eval_list)
    g_eval = evaluate_blocks_list(gblocks, eval_list)
    
    # perform the recursive multiplication
    r = {eval_list[i]:multiply(f_eval[i], g_eval[i], next_alg, interpolation)
            for i in range(len(f_eval))}
    
    # Solve for the coefficients
    if interpolation == "Natural":
        r_coefs = solve_for_coefficients_natural(n, r)
    elif interpolation == "Efficient":    
        r_coefs = solve_for_coefficients_efficient(n, r)
    elif interpolation == "Matrix":
        r_coefs = solve_for_coefficients_matrix(n, r)
    else:
        raise ValueError("Invalid interpolation method: " + str(interpolation)) 
    
    # recombination
    k = int(np.ceil(len(f) / n))
    prod = r_coefs[0][:k]
    for j in range(1, 2*n-2):
        prod = prod + [r_coefs[j-1][k+i] + r_coefs[j][i] for i in range(k-1)]
        prod = prod + [r_coefs[j][k-1]]

    prod = prod + [r_coefs[2*n-3][k+i] + r_coefs[2*n-2][i] for i in range(k-1)]

    prod = prod + r_coefs[2*n-2][k-1:]

    return prod[:2*len(f)-1]


def schoolbook(f, g):
    """ Uses schoolbook multiplication to multiply f and g. Returns the
        product as a list"""
    d = len(f) + len(g) - 1
    
    # initialize a list of zeros
    product = [0]*d
    
    # distribute through all possible combinations of coefficients
    for i in range(len(f)):
        for j in range(len(g)):
            product[i + j] += f[i]*g[j]
    return product

def split(f, num_blocks):
    """ Splits the list f into num_blocks different blocks of equal size
        If it doesn't divide evenly, we put zeros on the end of the last
        block."""
    blocks = []
    copy_f = list(f)  # copy f so we don't ruin it!!!!!!!!
    while len(copy_f) % num_blocks != 0:
        copy_f.append(0)
    block_length = len(copy_f) // num_blocks
    index = 0
    while index + block_length < len(copy_f):
        blocks.append(copy_f[index:index+block_length])
        index += block_length
    blocks.append(copy_f[index:])
    return blocks    

def make_eval_list(n):
    """ In Toom-n, this makes the list of number to plug in
        (0, 1, -1, 2, -2, ..., n-2, -(n-2), n-1, 'infinity')"""
    eval_points = [0]
    for i in range(1, n - 1):
        eval_points.append(i)
        eval_points.append(-i)
    eval_points.append(n-1)
    eval_points.append('infinity')
    return eval_points
  

def evaluate_blocks(blocks, value):
    """ blocks is a list of lists, each list is the coefficients of a
        polynomial. But each list a coefficient. For example, if blocks is
        [[1,2],[3,4],[5,6]] and value is -2, we return
        [1,2] + [-6,-8] + [20,24] = [15, 18].  If the value is infinity,
        we return the leading coefficient."""
        
    if value == 'infinity':
        return blocks[-1]
    
    # initialize an empty list of the right length
    answer = [0]*len(blocks[0])
    
    coefficient = 1
    for i in range(len(blocks)):
        for j in range(len(blocks[0])):
            answer[j] += coefficient*blocks[i][j]
        coefficient *= value    # multiply to make powers of value
    return answer

def evaluate_blocks_list(blocks, values):
    """ Evaluates the blocks on a list of values, and returns a list"""
    answer = []
    for value in values:
        answer.append(evaluate_blocks(blocks, value))
    return answer