from math_helper import *

def write_to_file(filename, interpolation, max_n):
    write_calling_function(filename, interpolation, max_n)

    for n in range(2, max_n + 1):
        if interpolation == "Efficient":
            write_efficient(filename, n)
        elif interpolation == "Natural":
            write_natural(filename, n)
        # matrix formulas require matrix inversion. done via sage
        #elif interpolation == "Matrix":
        #    write_matrix(filename, n)
        else:
            raise ValueError("invalid interpolation: {}".format(interpolation))
    return

def write_calling_function(filename, interpolation, max_n):
    f = open(filename, "w")
    
    # The header of the function
    f.write("def solve_for_coefficients_{}(n, r):\n".format(interpolation.lower()))
        
    # 2 is a special case
    f.write("\tif n == {}:\n".format(2))
    f.write("\t\treturn {}_interpolate_{}(r)\n".format(interpolation.lower(), 2))
    f.write("\n")
    
    # Call the function for each valid n
    for n in range(3, max_n + 1):
        f.write("\telif n == {}:\n".format(n))
        f.write("\t\treturn {}_interpolate_{}(r)\n".format(interpolation.lower(), n))
        f.write("\n")
    
    # error if n is too big
    f.write("\telse:\n")
    f.write("\t\traise ValueError(\"Toom-{} is not implemented\".format(n))\n")
    f.write("\n")
    
    f.close()
    return

# ===========================================================================
#
#       Code to Generate Python Code for the Efficient Formulas
#
# ===========================================================================
def write_efficient(filename, n):
    # Special cases for 2, 3, 4
    if n == 2:
        f = open(filename, "a")
        f.write("def efficient_interpolate_{}(r):\n".format(2))
        f.write("\tr0 = r[0]\n")
        f.write("\tr2 = r['infinity']\n")
        f.write("\tr1 = [r[1][i] - r0[i] - r2[i] for i in range(len(r0))]\n")
        f.write("\treturn (r0, r1, r2)\n")
        f.write("\n")
        f.close()
    elif n == 3:
        f = open(filename, "a")
        f.write("def efficient_interpolate_{}(r):\n".format(3))
        f.write("\tr0 = r[0]\n")
        f.write("\tr4 = r['infinity']\n")
        f.write("\n")
        f.write("\tL = len(r0)\n")
        f.write("\n")
        f.write("\tr2 = [((r[1][i] + r[-1][i])\n")
        f.write("\t - 2*r0[i]\n")
        f.write("\t - 2*r4[i]\n")
        f.write("\t) // 2 for i in range(len(r0))]\n")
        f.write("\n")
        f.write("\tO1 = [(r[1][i] - r[-1][i])//2 for i in range(L)]\n")
        f.write("\n") 
        f.write("\tr3 = [((r[2][i] - r0[i] - 4*r2[i] - 16*r4[i])//2 - O1[i])//3 for i in range(L)]\n")
        f.write("\tr1 = [O1[i] - r3[i] for i in range(L)]\n")
        f.write("\n")  
        f.write("\treturn (r0, r1, r2, r3, r4)\n")
        f.write("\n")
        f.close()
    elif n == 4:
        f = open(filename, "a")
        f.write("def efficient_interpolate_{}(r):\n".format(4))
        f.write("\tr0 = r[0]\n")
        f.write("\tr6 = r['infinity']\n")
        f.write("\n")
        f.write("\tL = len(r0)\n")
        f.write("\n")
        f.write("\t# the even temp variables\n")
        f.write("\n")
        f.write("\t# start with E1, since it's not in a layer\n")
        f.write("\tE1 = [(r[1][i] + r[-1][i])//2 - r0[i] - r6[i] for i in range(L)]\n")
        f.write("\n")
        f.write("\t# the remaining even variables\n")
        f.write("\tr4 = [(((r[2][i] + r[-2][i])//2 - r0[i] - 64*r6[i])//4 - E1[i])//3 for i in range(L)]\n")
        f.write("\tr2 = [E1[i] - r4[i]  for i in range(L)]\n")
        f.write("\n")
        f.write("\t# the odd temp variables\n")
        f.write("\n")
        f.write("\t# start with O1, since it's not in a layer\n")
        f.write("\tO1 = [(r[1][i] - r[-1][i])//2 for i in range(L)]\n")
        f.write("\n")
        f.write("\t# layer 1\n")
        f.write("\tO2 = [((r[2][i] - r[-2][i])//4 - O1[i])//3 for i in range(L)]\n")
        f.write("\tO3 = [((r[3][i] - r0[i] - 9*r2[i] - 81*r4[i] - 729*r6[i] )//3 - O1[i])//8 for i in range(L)]\n")
        f.write("\n")
        f.write("\t# the remaining odd variables\n")
        f.write("\tr5 = [(O3[i] - O2[i]) // 5 for i in range(L)]\n")
        f.write("\tr3 = [O2[i] - 5*r5[i]  for i in range(L)]\n")
        f.write("\tr1 = [O1[i] - r3[i] - r5[i]  for i in range(L)]\n")
        f.write("\n")
        f.write("\treturn (r0, r1, r2, r3, r4, r5, r6)\n")
        f.write("\n")
        f.close()
    # Can do it in general when n >= 5
    else:
        f = open(filename, "a")
        f.write("def efficient_interpolate_{}(r):\n".format(n)) 
        # the first two are for free
        f.write("\tr0 = r[0]\n")
        f.write("\tr{} = r['infinity']\n\n".format(2*n-2))
    
        # save the length, to save time
        f.write("\tL = len(r0)\n\n")
    
        # the even temp variables
        f.write("\t# the even temp variables\n\n")
    
        # start with E1, since it's not in a layer
        f.write("\t# start with E1, since it's not in a layer\n")
        f.write("\tE1 = [(r[1][i] + r[-1][i])//2 - r0[i] - r{}[i] for i in range(L)]\n\n".format(2*n-2))
    
        # now do layer 1
        f.write("\t# layer 1\n")
        for b in range(2, n-1):
            f.write("\tE{} = [(((r[{}][i] + r[-{}][i])//2 - r0[i] - {}*r{}[i])//{} - E1[i])//{} for i in range(L)]\n".format(b, b, b, exp(b, 2*n-2), 2*n-2, b*b, b*b-1))
    
        # the other even layers
        for layer in range(2, n - 4 + 1):
            f.write("\n\t# layer {}\n".format(layer))
            for b in range(2, n - 1 - layer + 1):
                f.write("\tE{} = [(E{}[i] - E{}[i]) // {} for i in range(L)]\n".format(ind_e(n,layer,b), ind_e(n, layer-1, b+1), ind_e(n, layer-1, b), denominator(layer, b)))
   
        # the remaining even variables
        f.write("\n\t# the remaining even variables\n")
    
        # r_{2n-4} is special
        f.write("\tr{} = [(E{}[i] - E{}[i]) // {} for i in range(L)]\n".format(2*n-4, ind_e(n, n-4, 3), ind_e(n, n-4, 2), denominator(n-3, 2)))
        
        # the others have a pattern
        for i in range(n-3, 1, -1):
            s = "\tr{} = [E{}[i] ".format(2*i, ind_e(n, i-1, 2))
            for j in range(i+1, n-2+1):
                s += "- {}*r{}[i] ".format(t(j, i, 2), 2*j)
            s += " for i in range(L)]\n"
            f.write(s)
        # r2 is also special because of the 1's
        s = "\tr2 = [E1[i] "
        for j in range(2, n-2+1):
            s += "- r{}[i] ".format(2*j)
        s += " for i in range(L)]\n"
        f.write(s)
    
        # the odd temp variables
        f.write("\n\t# the odd temp variables\n\n")
    
        # start with O1, since it's not in a layer
        f.write("\t# start with O1, since it's not in a layer\n")
        f.write("\tO1 = [(r[1][i] - r[-1][i])//2 for i in range(L)]\n\n")
          
        # now do most of layer 1
        f.write("\t# layer 1\n")
        for b in range(2, n-1):
            f.write("\tO{} = [((r[{}][i] - r[-{}][i])//{} - O1[i])//{} for i in range(L)]\n".format(b, b, b, 2*b, b*b-1))
        # and now the last thing in layer 1
        s = "\tO{} = [((r[{}][i] - r0[i] ".format(n-1, n-1)
        for i in range(1, n):
            s += "- {}*r{}[i] ".format(exp(n-1, 2*i), 2*i)
        s += ")//{} - O1[i])//{} for i in range(L)]\n".format(n-1, (n-1)*(n-1) - 1)
        f.write(s)
    
        # the other odd layers
        for layer in range(2, n - 3 + 1):
            f.write("\n\t# layer {}\n".format(layer))
            for b in range(2, n - layer + 1):
                f.write("\tO{} = [(O{}[i] - O{}[i]) // {} for i in range(L)]\n".format(ind_o(n,layer,b), ind_o(n, layer-1, b+1), ind_o(n, layer-1, b), denominator(layer, b)))
            
        # the remaining odd variables
        f.write("\n\t# the remaining odd variables\n")
    
        # r_{2n-3} is special
        f.write("\tr{} = [(O{}[i] - O{}[i]) // {} for i in range(L)]\n".format(2*n-3, ind_o(n, n-3, 3), ind_o(n, n-3, 2), denominator(n-2, 2)))
    
        # the others have a pattern
        for i in range(n-2, 1, -1):
            s = "\tr{} = [O{}[i] ".format(2*i-1, ind_o(n, i-1, 2))
            for j in range(i+1, n-1+1):
                s += "- {}*r{}[i] ".format(t(j, i, 2), 2*j-1)
            s += " for i in range(L)]\n"
            f.write(s)
    
        # r1 is also special because of the 1's
        s = "\tr1 = [O1[i] "
        for j in range(2, n-1+1):
            s += "- r{}[i] ".format(2*j-1)
        s += " for i in range(L)]\n\n"
        f.write(s)
    
        s = "\treturn (r0"
        for i in range(1, 2*n-1):
            s += ", r{}".format(i)
        s += ")\n\n"
        f.write(s)
        f.close()
    
    return

# ===========================================================================
#
#       Code to Generate Python Code for the Natural Formulas
#
# ===========================================================================
def write_natural(filename, n):
    # Special case for n = 2
    if n == 2:
        f = open(filename, "a")
        f.write("def natural_interpolate_{}(r):\n".format(2))
        f.write("\tr0 = r[0]\n")
        f.write("\tr2 = r['infinity']\n")
        f.write("\tr1 = [r[1][i] - r0[i] - r2[i] for i in range(len(r0))]\n")
        f.write("\treturn (r0, r1, r2)\n")
        f.write("\n")
        f.close()
    else:
        f = open(filename, "a")
        f.write("def natural_interpolate_{}(r):\n".format(n))
        # the first two are for free
        f.write("\tr0 = r[0]\n")
        f.write("\tr{} = r['infinity']\n".format(2*n-2))

        # now do the other even coefficients
        current_coef = 2*n - 2
        while current_coef > 2:
            current_coef -= 2
            s = "\tr{} = [(".format(current_coef)
            m = current_coef // 2

            # do the first r(a) + r(-a)
            j = 1
            e = exp(-1, m+j) * binomial(2*m, m-j)
            if e == 1:
                coef_string = ""
            else:
                coef_string = "{}*".format(e)
            s += coef_string + "(r[{}][i] + r[-{}][i])\n\t".format(j,j)

            # add in the other (r(a) + r(-a)) things
            for j in range(2, m + 1):
                e = exp(-1, m+j) * binomial(2*m, m-j)
                if e > 1:
                    coef_string = " + {}*".format(e)
                elif e < 0:
                    coef_string = " - {}*".format(abs(e))
                else:
                    coef_string = " + "
                s += coef_string + "(r[{}][i] + r[-{}][i])\n\t".format(j,j)

            # do r0
            i = 0
            this_coef = 2*sum([exp(-1, m+j) * binomial(2*m, m-j)*exp(j, i) for j in range(1, m + 1)])
            if this_coef < 0:
                coef_string = " + {}*".format(abs(this_coef))
            elif this_coef > 1:
                coef_string = " - {}*".format(this_coef)
            else:
                coef_string = " + "
            s += coef_string + "r{}[i]\n\t".format(i)

            # do the remaining even r's
            for i in range(current_coef + 2, 2*n, 2):
                this_coef = 2*sum([exp(-1, m+j) * binomial(2*m, m-j)*exp(j, i) for j in range(1, m + 1)])
                if this_coef < 0:
                    coef_string = " + {}*".format(abs(this_coef))
                elif this_coef > 1:
                    coef_string = " - {}*".format(this_coef)
                else:
                    coef_string = " + "
                s += coef_string + "r{}[i]\n\t".format(i)

            s += ") // {}".format(factorial(current_coef))
            f.write(s + " for i in range(len(r0))]\n\n")


        # the odd coefficients
        current_coef = 2*n - 1
        while current_coef > 3:
            current_coef -= 2
            s = "\tr{} = [(".format(current_coef)
            m = (current_coef + 1) // 2

            # do the first r(a)
            j = 1
            o = exp(-1, m+j) * binomial(2*m - 1, m-j)*2*j // (m+j)
            if o == 1:
                coef_string = ""
            else:
                coef_string = "{}*".format(o)
            s += coef_string + "r[{}][i] \n\t".format(j)

            # add in the other r(a) things
            for j in range(2, m + 1):
                o = exp(-1, m+j) * binomial(2*m - 1, m-j)*2*j // (m+j)
                if o > 1:
                    coef_string = " + {}*".format(o)
                elif o < 0:
                    coef_string = " - {}*".format(abs(o))
                else:
                    coef_string = " + "
                s += coef_string + "r[{}][i]\n\t".format(j)

            # do r0
            i = 0
            this_coef = sum([exp(-1, m+j) * binomial(2*m - 1, m-j)*2*j*exp(j, i) // (m+j) for j in range(1, m + 1)])
            if this_coef < 0:
                coef_string = " + {}*".format(abs(this_coef))
            elif this_coef > 1:
                coef_string = " - {}*".format(this_coef)
            else:
                coef_string = " + "
            s += coef_string + "r{}[i]\n\t".format(i)

            # do the remaining r's
            for i in [x for x in range(2, 2*n-2 + 1) if (x % 2) == 0 or x > current_coef]:
                this_coef = sum([exp(-1, m+j) * binomial(2*m - 1, m-j)*2*j*exp(j, i) // (m+j) for j in range(1, m + 1)])
                if this_coef < 0:
                    coef_string = " + {}*".format(abs(this_coef))
                elif this_coef > 1:
                    coef_string = " - {}*".format(this_coef)
                else:
                    coef_string = " + "
                s += coef_string + "r{}[i]\n\t".format(i)

            s += ") // {}".format(factorial(current_coef))
            f.write(s + " for i in range(len(r0))]\n\n")

        # do r1 separately
        s = "\tr1 = [r[1][i]\n\t - r0[i]\n\t"
        for i in range(2, 2*n-2 + 1):
            s += "- r{}[i]\n\t".format(i)
        f.write(s + " for i in range(len(r0))]\n\n")
        s = "\n\treturn (r0"
        for i in range(1, 2*n-1):
            s += ", r{}".format(i)
        s += ")\n"
        f.write(s + "\n")
    return
        
if __name__ == "__main__":
   write_to_file("auto_generated_efficient_formulas.py", "Efficient", 15)
    
    