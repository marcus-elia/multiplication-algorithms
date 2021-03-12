def write_to_file(filename, max_n):
    write_calling_function(filename, max_n)

    for n in range(2, max_n + 1):
        write_matrix(filename, n)
    return

def write_calling_function(filename, max_n):
    f = open(filename, "w")
    
    # The header of the function
    f.write("def solve_for_coefficients_matrix(n, r):\n")
        
    # 2 is a special case
    f.write("\tif n == {}:\n".format(2))
    f.write("\t\treturn matrix_interpolate_{}(r)\n".format(2))
    f.write("\n")
    
    # Call the function for each valid n
    for n in range(3, max_n + 1):
        f.write("\telif n == {}:\n".format(n))
        f.write("\t\treturn matrix_interpolate_{}(r)\n".format(n))
        f.write("\n")
    
    # error if n is too big
    f.write("\telse:\n")
    f.write("\t\traise ValueError(\"Toom-{} is not implemented\".format(n))\n")
    f.write("\n")
    
    f.close()
    return

def write_matrix(filename, n):
    f = open(filename, "a")
    f.write("def matrix_interpolate_{}(r):\n".format(n))
    
    # construct and invert the Toom-n matrix
    M = []
    for b in range(-(n-2), n):
        L = []
        for i in range(0, 2*n-1):
            L.append(b^i)
        M.append(L)
    M.append([0 for _ in range(2*n-2)] + [1])
    M = matrix(M)
    M = M.inverse()
    f.write("\tL = len(r[0])\n\n")
    
    # start with r0
    f.write("\tr0 = r[0]\n")
    
    # iterate through all middle rows
    for b in range(1, 2*n-2):
        if b % 2 == 0:
            denom = factorial(2*n-4)
        else:
            denom = factorial(2*n-3)
        s = "\tr{} = [(".format(b)
        
        # start with the first one
        coef = M[b][0]*denom
        if coef == 1:
            s += "r[{}][i]\n\t".format(-(n-2))
        elif coef == -1:
            s += "-r[{}][i]\n\t".format(-(n-2))
        elif coef != 0:
            s += "{}*r[{}][i]\n\t".format(coef,-(n-2))
        # then do all the middle columns
        for i in range(1,2*n-2):
            index = i - (n-2)
            coef = M[b][i]*denom
            if coef == 1:
                s += "+ r[{}][i]\n\t".format(index)
            elif coef == -1:
                s += "- r[{}][i]\n\t".format(index)
            elif coef > 0:
                s += "+ {}*r[{}][i]\n\t".format(coef,index)
            elif coef < 0:
                s += "- {}*r[{}][i]\n\t".format(-1*coef,index)
        # do the last one (r[infinity])
        coef = M[b][2*n-2]*denom
        if coef == 1:
            s += "+ r[\'{}\'][i]\n\t".format('infinity')
        elif coef == -1:
            s += "- r[\'{}\'][i]\n\t".format('infinity')
        elif coef > 0:
            s += "+ {}*r[\'{}\'][i]\n\t".format(coef,'infinity')
        elif coef < 0:
            s += "- {}*r[\'{}\'][i]\n\t".format(-1*coef,'infinity')
        
        s += ") // {} for i in range(L)]\n\n".format(denom)
        f.write(s)
    
    # end with r_2n-2
    f.write("\tr{} = r[\'infinity\']\n".format(2*n-2))
    
    s = "\treturn (r0"
    for i in range(1, 2*n-1):
        s += ", r{}".format(i)
    s += ")\n\n"
    f.write(s)
    f.close()
    return

if __name__ == "__main__":
    filename = "auto_generated_matrix_formulas.py"
    write_to_file(filename, 15)