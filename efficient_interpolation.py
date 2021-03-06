def solve_for_coefficients_efficient(n, r):
    if n == 2:
        r0 = r[0]
        r2 = r['infinity']
        r1 = [r[1][i] - r0[i] - r2[i] for i in xrange(len(r0))]
        return (r0, r1, r2)
    
    if n == 3:
         r0 = r[0]
         r4 = r['infinity']
         
         L = len(r0)

         r2 = [((r[1][i] + r[-1][i])
         - 2*r0[i]
         - 2*r4[i]
         ) / 2 for i in xrange(len(r0))]
         
         O1 = [(r[1][i] - r[-1][i])/2 for i in xrange(L)]
         
         r3 = [((r[2][i] - r0[i] - 4*r2[i] - 16*r4[i])/2 - O1[i])/3 for i in xrange(L)]
         r1 = [O1[i] - r3[i] for i in xrange(L)]
         
         return (r0, r1, r2, r3, r4)
         
    if n == 4:
        r0 = r[0]
        r6 = r['infinity']

        L = len(r0)

        # the even temp variables

        # start with E1, since it's not in a layer
        E1 = [(r[1][i] + r[-1][i])/2 - r0[i] - r6[i] for i in xrange(L)]

        # the remaining even variables
        r4 = [(((r[2][i] + r[-2][i])/2 - r0[i] - 64*r6[i])/4 - E1[i])/3 for i in xrange(L)]
        r2 = [E1[i] - r4[i]  for i in xrange(L)]

        # the odd temp variables

        # start with O1, since it's not in a layer
        O1 = [(r[1][i] - r[-1][i])/2 for i in xrange(L)]

        # layer 1
        O2 = [((r[2][i] - r[-2][i])/4 - O1[i])/3 for i in xrange(L)]
        O3 = [((r[3][i] - r0[i] - 9*r2[i] - 81*r4[i] - 729*r6[i] )/3 - O1[i])/8 for i in xrange(L)]

        # the remaining odd variables
        r5 = [(O3[i] - O2[i]) / 5 for i in xrange(L)]
        r3 = [O2[i] - 5*r5[i]  for i in xrange(L)]
        r1 = [O1[i] - r3[i] - r5[i]  for i in xrange(L)]

        return (r0, r1, r2, r3, r4, r5, r6)
    
    if n == 5:
        r0 = r[0]
        r8 = r['infinity']
        
        L = len(r0)
        
        # the even temp variables
        
        # start with E1, since it's not in a layer
        E1 = [(r[1][i] + r[-1][i])/2 - r0[i] - r8[i] for i in xrange(L)]
        
        # layer 1
        E2 = [(((r[2][i] + r[-2][i])/2 - r0[i] - 256*r8[i])/4 - E1[i])/3 for i in xrange(L)]
        E3 = [(((r[3][i] + r[-3][i])/2 - r0[i] - 6561*r8[i])/9 - E1[i])/8 for i in xrange(L)]
        
        # the remaining even variables
        r6 = [(E3[i] - E2[i]) / 5 for i in xrange(L)]
        r4 = [E2[i] - 5*r6[i]  for i in xrange(L)]
        r2 = [E1[i] - r4[i] - r6[i]  for i in xrange(L)]
        
        # the odd temp variables
        
        # start with O1, since it's not in a layer
        O1 = [(r[1][i] - r[-1][i])/2 for i in xrange(L)]
        
        # layer 1
        O2 = [((r[2][i] - r[-2][i])/4 - O1[i])/3 for i in xrange(L)]
        O3 = [((r[3][i] - r[-3][i])/6 - O1[i])/8 for i in xrange(L)]
        O4 = [((r[4][i] - r0[i] - 16*r2[i] - 256*r4[i] - 4096*r6[i] - 65536*r8[i] )/4 - O1[i])/15 for i in xrange(L)]
        
        # layer 2
        O5 = [(O3[i] - O2[i]) / 5 for i in xrange(L)]
        O6 = [(O4[i] - O3[i]) / 7 for i in xrange(L)]
        
        # the remaining odd variables
        r7 = [(O6[i] - O5[i]) / 12 for i in xrange(L)]
        r5 = [O5[i] - 14*r7[i]  for i in xrange(L)]
        r3 = [O2[i] - 5*r5[i] - 21*r7[i]  for i in xrange(L)]
        r1 = [O1[i] - r3[i] - r5[i] - r7[i]  for i in xrange(L)]
        
        return (r0, r1, r2, r3, r4, r5, r6, r7, r8)
    
    if n == 6:
        r0 = r[0]
        r10 = r['infinity']
        
        L = len(r0)
        
        # the even temp variables
        
        # start with E1, since it's not in a layer
        E1 = [(r[1][i] + r[-1][i])/2 - r0[i] - r10[i] for i in xrange(L)]
        
        # layer 1
        E2 = [(((r[2][i] + r[-2][i])/2 - r0[i] - 1024*r10[i])/4 - E1[i])/3 for i in xrange(L)]
        E3 = [(((r[3][i] + r[-3][i])/2 - r0[i] - 59049*r10[i])/9 - E1[i])/8 for i in xrange(L)]
        E4 = [(((r[4][i] + r[-4][i])/2 - r0[i] - 1048576*r10[i])/16 - E1[i])/15 for i in xrange(L)]
        
        # layer 2
        E5 = [(E3[i] - E2[i]) / 5 for i in xrange(L)]
        E6 = [(E4[i] - E3[i]) / 7 for i in xrange(L)]
        
        # the remaining even variables
        r8 = [(E6[i] - E5[i]) / 12 for i in xrange(L)]
        r6 = [E5[i] - 14*r8[i]  for i in xrange(L)]
        r4 = [E2[i] - 5*r6[i] - 21*r8[i]  for i in xrange(L)]
        r2 = [E1[i] - r4[i] - r6[i] - r8[i]  for i in xrange(L)]
        
        # the odd temp variables
        
        # start with O1, since it's not in a layer
        O1 = [(r[1][i] - r[-1][i])/2 for i in xrange(L)]
        
        # layer 1
        O2 = [((r[2][i] - r[-2][i])/4 - O1[i])/3 for i in xrange(L)]
        O3 = [((r[3][i] - r[-3][i])/6 - O1[i])/8 for i in xrange(L)]
        O4 = [((r[4][i] - r[-4][i])/8 - O1[i])/15 for i in xrange(L)]
        O5 = [((r[5][i] - r0[i] - 25*r2[i] - 625*r4[i] - 15625*r6[i] - 390625*r8[i] - 9765625*r10[i] )/5 - O1[i])/24 for i in xrange(L)]
        
        # layer 2
        O6 = [(O3[i] - O2[i]) / 5 for i in xrange(L)]
        O7 = [(O4[i] - O3[i]) / 7 for i in xrange(L)]
        O8 = [(O5[i] - O4[i]) / 9 for i in xrange(L)]
        
        # layer 3
        O9 = [(O7[i] - O6[i]) / 12 for i in xrange(L)]
        O10 = [(O8[i] - O7[i]) / 16 for i in xrange(L)]
        
        # the remaining odd variables
        r9 = [(O10[i] - O9[i]) / 21 for i in xrange(L)]
        r7 = [O9[i] - 30*r9[i]  for i in xrange(L)]
        r5 = [O6[i] - 14*r7[i] - 147*r9[i]  for i in xrange(L)]
        r3 = [O2[i] - 5*r5[i] - 21*r7[i] - 85*r9[i]  for i in xrange(L)]
        r1 = [O1[i] - r3[i] - r5[i] - r7[i] - r9[i]  for i in xrange(L)]
        
        return (r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10)
    
    if n == 7:
        r0 = r[0]
        r12 = r['infinity']
        
        L = len(r0)
        
        # the even temp variables
        
        # start with E1, since it's not in a layer
        E1 = [(r[1][i] + r[-1][i])/2 - r0[i] - r12[i] for i in xrange(L)]
        
        # layer 1
        E2 = [(((r[2][i] + r[-2][i])/2 - r0[i] - 4096*r12[i])/4 - E1[i])/3 for i in xrange(L)]
        E3 = [(((r[3][i] + r[-3][i])/2 - r0[i] - 531441*r12[i])/9 - E1[i])/8 for i in xrange(L)]
        E4 = [(((r[4][i] + r[-4][i])/2 - r0[i] - 16777216*r12[i])/16 - E1[i])/15 for i in xrange(L)]
        E5 = [(((r[5][i] + r[-5][i])/2 - r0[i] - 244140625*r12[i])/25 - E1[i])/24 for i in xrange(L)]
        
        # layer 2
        E6 = [(E3[i] - E2[i]) / 5 for i in xrange(L)]
        E7 = [(E4[i] - E3[i]) / 7 for i in xrange(L)]
        E8 = [(E5[i] - E4[i]) / 9 for i in xrange(L)]
        
        # layer 3
        E9 = [(E7[i] - E6[i]) / 12 for i in xrange(L)]
        E10 = [(E8[i] - E7[i]) / 16 for i in xrange(L)]
        
        # the remaining even variables
        r10 = [(E10[i] - E9[i]) / 21 for i in xrange(L)]
        r8 = [E9[i] - 30*r10[i]  for i in xrange(L)]
        r6 = [E6[i] - 14*r8[i] - 147*r10[i]  for i in xrange(L)]
        r4 = [E2[i] - 5*r6[i] - 21*r8[i] - 85*r10[i]  for i in xrange(L)]
        r2 = [E1[i] - r4[i] - r6[i] - r8[i] - r10[i]  for i in xrange(L)]
        
        # the odd temp variables
        
        # start with O1, since it's not in a layer
        O1 = [(r[1][i] - r[-1][i])/2 for i in xrange(L)]
        
        # layer 1
        O2 = [((r[2][i] - r[-2][i])/4 - O1[i])/3 for i in xrange(L)]
        O3 = [((r[3][i] - r[-3][i])/6 - O1[i])/8 for i in xrange(L)]
        O4 = [((r[4][i] - r[-4][i])/8 - O1[i])/15 for i in xrange(L)]
        O5 = [((r[5][i] - r[-5][i])/10 - O1[i])/24 for i in xrange(L)]
        O6 = [((r[6][i] - r0[i] - 36*r2[i] - 1296*r4[i] - 46656*r6[i] - 1679616*r8[i] - 60466176*r10[i] - 2176782336*r12[i] )/6 - O1[i])/35 for i in xrange(L)]
        
        # layer 2
        O7 = [(O3[i] - O2[i]) / 5 for i in xrange(L)]
        O8 = [(O4[i] - O3[i]) / 7 for i in xrange(L)]
        O9 = [(O5[i] - O4[i]) / 9 for i in xrange(L)]
        O10 = [(O6[i] - O5[i]) / 11 for i in xrange(L)]
        
        # layer 3
        O11 = [(O8[i] - O7[i]) / 12 for i in xrange(L)]
        O12 = [(O9[i] - O8[i]) / 16 for i in xrange(L)]
        O13 = [(O10[i] - O9[i]) / 20 for i in xrange(L)]
        
        # layer 4
        O14 = [(O12[i] - O11[i]) / 21 for i in xrange(L)]
        O15 = [(O13[i] - O12[i]) / 27 for i in xrange(L)]
        
        # the remaining odd variables
        r11 = [(O15[i] - O14[i]) / 32 for i in xrange(L)]
        r9 = [O14[i] - 55*r11[i]  for i in xrange(L)]
        r7 = [O11[i] - 30*r9[i] - 627*r11[i]  for i in xrange(L)]
        r5 = [O7[i] - 14*r7[i] - 147*r9[i] - 1408*r11[i]  for i in xrange(L)]
        r3 = [O2[i] - 5*r5[i] - 21*r7[i] - 85*r9[i] - 341*r11[i]  for i in xrange(L)]
        r1 = [O1[i] - r3[i] - r5[i] - r7[i] - r9[i] - r11[i]  for i in xrange(L)]
        
        return (r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12)
    
    if n == 8:
        r0 = r[0]
        r14 = r['infinity']
        
        L = len(r0)
        
        # the even temp variables
        
        # start with E1, since it's not in a layer
        E1 = [(r[1][i] + r[-1][i])/2 - r0[i] - r14[i] for i in xrange(L)]
        
        # layer 1
        E2 = [(((r[2][i] + r[-2][i])/2 - r0[i] - 16384*r14[i])/4 - E1[i])/3 for i in xrange(L)]
        E3 = [(((r[3][i] + r[-3][i])/2 - r0[i] - 4782969*r14[i])/9 - E1[i])/8 for i in xrange(L)]
        E4 = [(((r[4][i] + r[-4][i])/2 - r0[i] - 268435456*r14[i])/16 - E1[i])/15 for i in xrange(L)]
        E5 = [(((r[5][i] + r[-5][i])/2 - r0[i] - 6103515625*r14[i])/25 - E1[i])/24 for i in xrange(L)]
        E6 = [(((r[6][i] + r[-6][i])/2 - r0[i] - 78364164096*r14[i])/36 - E1[i])/35 for i in xrange(L)]
        
        # layer 2
        E7 = [(E3[i] - E2[i]) / 5 for i in xrange(L)]
        E8 = [(E4[i] - E3[i]) / 7 for i in xrange(L)]
        E9 = [(E5[i] - E4[i]) / 9 for i in xrange(L)]
        E10 = [(E6[i] - E5[i]) / 11 for i in xrange(L)]
        
        # layer 3
        E11 = [(E8[i] - E7[i]) / 12 for i in xrange(L)]
        E12 = [(E9[i] - E8[i]) / 16 for i in xrange(L)]
        E13 = [(E10[i] - E9[i]) / 20 for i in xrange(L)]
        
        # layer 4
        E14 = [(E12[i] - E11[i]) / 21 for i in xrange(L)]
        E15 = [(E13[i] - E12[i]) / 27 for i in xrange(L)]
        
        # the remaining even variables
        r12 = [(E15[i] - E14[i]) / 32 for i in xrange(L)]
        r10 = [E14[i] - 55*r12[i]  for i in xrange(L)]
        r8 = [E11[i] - 30*r10[i] - 627*r12[i]  for i in xrange(L)]
        r6 = [E7[i] - 14*r8[i] - 147*r10[i] - 1408*r12[i]  for i in xrange(L)]
        r4 = [E2[i] - 5*r6[i] - 21*r8[i] - 85*r10[i] - 341*r12[i]  for i in xrange(L)]
        r2 = [E1[i] - r4[i] - r6[i] - r8[i] - r10[i] - r12[i]  for i in xrange(L)]
        
        # the odd temp variables
        
        # start with O1, since it's not in a layer
        O1 = [(r[1][i] - r[-1][i])/2 for i in xrange(L)]
        
        # layer 1
        O2 = [((r[2][i] - r[-2][i])/4 - O1[i])/3 for i in xrange(L)]
        O3 = [((r[3][i] - r[-3][i])/6 - O1[i])/8 for i in xrange(L)]
        O4 = [((r[4][i] - r[-4][i])/8 - O1[i])/15 for i in xrange(L)]
        O5 = [((r[5][i] - r[-5][i])/10 - O1[i])/24 for i in xrange(L)]
        O6 = [((r[6][i] - r[-6][i])/12 - O1[i])/35 for i in xrange(L)]
        O7 = [((r[7][i] - r0[i] - 49*r2[i] - 2401*r4[i] - 117649*r6[i] - 5764801*r8[i] - 282475249*r10[i] - 13841287201*r12[i] - 678223072849*r14[i] )/7 - O1[i])/48 for i in xrange(L)]
        
        # layer 2
        O8 = [(O3[i] - O2[i]) / 5 for i in xrange(L)]
        O9 = [(O4[i] - O3[i]) / 7 for i in xrange(L)]
        O10 = [(O5[i] - O4[i]) / 9 for i in xrange(L)]
        O11 = [(O6[i] - O5[i]) / 11 for i in xrange(L)]
        O12 = [(O7[i] - O6[i]) / 13 for i in xrange(L)]
        
        # layer 3
        O13 = [(O9[i] - O8[i]) / 12 for i in xrange(L)]
        O14 = [(O10[i] - O9[i]) / 16 for i in xrange(L)]
        O15 = [(O11[i] - O10[i]) / 20 for i in xrange(L)]
        O16 = [(O12[i] - O11[i]) / 24 for i in xrange(L)]
        
        # layer 4
        O17 = [(O14[i] - O13[i]) / 21 for i in xrange(L)]
        O18 = [(O15[i] - O14[i]) / 27 for i in xrange(L)]
        O19 = [(O16[i] - O15[i]) / 33 for i in xrange(L)]
        
        # layer 5
        O20 = [(O18[i] - O17[i]) / 32 for i in xrange(L)]
        O21 = [(O19[i] - O18[i]) / 40 for i in xrange(L)]
        
        # the remaining odd variables
        r13 = [(O21[i] - O20[i]) / 45 for i in xrange(L)]
        r11 = [O20[i] - 91*r13[i]  for i in xrange(L)]
        r9 = [O17[i] - 55*r11[i] - 2002*r13[i]  for i in xrange(L)]
        r7 = [O13[i] - 30*r9[i] - 627*r11[i] - 11440*r13[i]  for i in xrange(L)]
        r5 = [O8[i] - 14*r7[i] - 147*r9[i] - 1408*r11[i] - 13013*r13[i]  for i in xrange(L)]
        r3 = [O2[i] - 5*r5[i] - 21*r7[i] - 85*r9[i] - 341*r11[i] - 1365*r13[i]  for i in xrange(L)]
        r1 = [O1[i] - r3[i] - r5[i] - r7[i] - r9[i] - r11[i] - r13[i]  for i in xrange(L)]
        
        return (r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14)
    
    if n == 9:
        r0 = r[0]
        r16 = r['infinity']
        
        L = len(r0)
        
        # the even temp variables
        
        # start with E1, since it's not in a layer
        E1 = [(r[1][i] + r[-1][i])/2 - r0[i] - r16[i] for i in xrange(L)]
        
        # layer 1
        E2 = [(((r[2][i] + r[-2][i])/2 - r0[i] - 65536*r16[i])/4 - E1[i])/3 for i in xrange(L)]
        E3 = [(((r[3][i] + r[-3][i])/2 - r0[i] - 43046721*r16[i])/9 - E1[i])/8 for i in xrange(L)]
        E4 = [(((r[4][i] + r[-4][i])/2 - r0[i] - 4294967296*r16[i])/16 - E1[i])/15 for i in xrange(L)]
        E5 = [(((r[5][i] + r[-5][i])/2 - r0[i] - 152587890625*r16[i])/25 - E1[i])/24 for i in xrange(L)]
        E6 = [(((r[6][i] + r[-6][i])/2 - r0[i] - 2821109907456*r16[i])/36 - E1[i])/35 for i in xrange(L)]
        E7 = [(((r[7][i] + r[-7][i])/2 - r0[i] - 33232930569601*r16[i])/49 - E1[i])/48 for i in xrange(L)]
        
        # layer 2
        E8 = [(E3[i] - E2[i]) / 5 for i in xrange(L)]
        E9 = [(E4[i] - E3[i]) / 7 for i in xrange(L)]
        E10 = [(E5[i] - E4[i]) / 9 for i in xrange(L)]
        E11 = [(E6[i] - E5[i]) / 11 for i in xrange(L)]
        E12 = [(E7[i] - E6[i]) / 13 for i in xrange(L)]
        
        # layer 3
        E13 = [(E9[i] - E8[i]) / 12 for i in xrange(L)]
        E14 = [(E10[i] - E9[i]) / 16 for i in xrange(L)]
        E15 = [(E11[i] - E10[i]) / 20 for i in xrange(L)]
        E16 = [(E12[i] - E11[i]) / 24 for i in xrange(L)]
        
        # layer 4
        E17 = [(E14[i] - E13[i]) / 21 for i in xrange(L)]
        E18 = [(E15[i] - E14[i]) / 27 for i in xrange(L)]
        E19 = [(E16[i] - E15[i]) / 33 for i in xrange(L)]
        
        # layer 5
        E20 = [(E18[i] - E17[i]) / 32 for i in xrange(L)]
        E21 = [(E19[i] - E18[i]) / 40 for i in xrange(L)]
        
        # the remaining even variables
        r14 = [(E21[i] - E20[i]) / 45 for i in xrange(L)]
        r12 = [E20[i] - 91*r14[i]  for i in xrange(L)]
        r10 = [E17[i] - 55*r12[i] - 2002*r14[i]  for i in xrange(L)]
        r8 = [E13[i] - 30*r10[i] - 627*r12[i] - 11440*r14[i]  for i in xrange(L)]
        r6 = [E8[i] - 14*r8[i] - 147*r10[i] - 1408*r12[i] - 13013*r14[i]  for i in xrange(L)]
        r4 = [E2[i] - 5*r6[i] - 21*r8[i] - 85*r10[i] - 341*r12[i] - 1365*r14[i]  for i in xrange(L)]
        r2 = [E1[i] - r4[i] - r6[i] - r8[i] - r10[i] - r12[i] - r14[i]  for i in xrange(L)]
        
        # the odd temp variables
        
        # start with O1, since it's not in a layer
        O1 = [(r[1][i] - r[-1][i])/2 for i in xrange(L)]
        
        # layer 1
        O2 = [((r[2][i] - r[-2][i])/4 - O1[i])/3 for i in xrange(L)]
        O3 = [((r[3][i] - r[-3][i])/6 - O1[i])/8 for i in xrange(L)]
        O4 = [((r[4][i] - r[-4][i])/8 - O1[i])/15 for i in xrange(L)]
        O5 = [((r[5][i] - r[-5][i])/10 - O1[i])/24 for i in xrange(L)]
        O6 = [((r[6][i] - r[-6][i])/12 - O1[i])/35 for i in xrange(L)]
        O7 = [((r[7][i] - r[-7][i])/14 - O1[i])/48 for i in xrange(L)]
        O8 = [((r[8][i] - r0[i] - 64*r2[i] - 4096*r4[i] - 262144*r6[i] - 16777216*r8[i] - 1073741824*r10[i] - 68719476736*r12[i] - 4398046511104*r14[i] - 281474976710656*r16[i] )/8 - O1[i])/63 for i in xrange(L)]
        
        # layer 2
        O9 = [(O3[i] - O2[i]) / 5 for i in xrange(L)]
        O10 = [(O4[i] - O3[i]) / 7 for i in xrange(L)]
        O11 = [(O5[i] - O4[i]) / 9 for i in xrange(L)]
        O12 = [(O6[i] - O5[i]) / 11 for i in xrange(L)]
        O13 = [(O7[i] - O6[i]) / 13 for i in xrange(L)]
        O14 = [(O8[i] - O7[i]) / 15 for i in xrange(L)]
        
        # layer 3
        O15 = [(O10[i] - O9[i]) / 12 for i in xrange(L)]
        O16 = [(O11[i] - O10[i]) / 16 for i in xrange(L)]
        O17 = [(O12[i] - O11[i]) / 20 for i in xrange(L)]
        O18 = [(O13[i] - O12[i]) / 24 for i in xrange(L)]
        O19 = [(O14[i] - O13[i]) / 28 for i in xrange(L)]
        
        # layer 4
        O20 = [(O16[i] - O15[i]) / 21 for i in xrange(L)]
        O21 = [(O17[i] - O16[i]) / 27 for i in xrange(L)]
        O22 = [(O18[i] - O17[i]) / 33 for i in xrange(L)]
        O23 = [(O19[i] - O18[i]) / 39 for i in xrange(L)]
        
        # layer 5
        O24 = [(O21[i] - O20[i]) / 32 for i in xrange(L)]
        O25 = [(O22[i] - O21[i]) / 40 for i in xrange(L)]
        O26 = [(O23[i] - O22[i]) / 48 for i in xrange(L)]
        
        # layer 6
        O27 = [(O25[i] - O24[i]) / 45 for i in xrange(L)]
        O28 = [(O26[i] - O25[i]) / 55 for i in xrange(L)]
        
        # the remaining odd variables
        r15 = [(O28[i] - O27[i]) / 60 for i in xrange(L)]
        r13 = [O27[i] - 140*r15[i]  for i in xrange(L)]
        r11 = [O24[i] - 91*r13[i] - 5278*r15[i]  for i in xrange(L)]
        r9 = [O20[i] - 55*r11[i] - 2002*r13[i] - 61490*r15[i]  for i in xrange(L)]
        r7 = [O15[i] - 30*r9[i] - 627*r11[i] - 11440*r13[i] - 196053*r15[i]  for i in xrange(L)]
        r5 = [O9[i] - 14*r7[i] - 147*r9[i] - 1408*r11[i] - 13013*r13[i] - 118482*r15[i]  for i in xrange(L)]
        r3 = [O2[i] - 5*r5[i] - 21*r7[i] - 85*r9[i] - 341*r11[i] - 1365*r13[i] - 5461*r15[i]  for i in xrange(L)]
        r1 = [O1[i] - r3[i] - r5[i] - r7[i] - r9[i] - r11[i] - r13[i] - r15[i]  for i in xrange(L)]
        
        return (r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16)
    
    if n == 10:
        r0 = r[0]
        r18 = r['infinity']
        
        L = len(r0)
        
        # the even temp variables
        
        # start with E1, since it's not in a layer
        E1 = [(r[1][i] + r[-1][i])/2 - r0[i] - r18[i] for i in xrange(L)]
        
        # layer 1
        E2 = [(((r[2][i] + r[-2][i])/2 - r0[i] - 262144*r18[i])/4 - E1[i])/3 for i in xrange(L)]
        E3 = [(((r[3][i] + r[-3][i])/2 - r0[i] - 387420489*r18[i])/9 - E1[i])/8 for i in xrange(L)]
        E4 = [(((r[4][i] + r[-4][i])/2 - r0[i] - 68719476736*r18[i])/16 - E1[i])/15 for i in xrange(L)]
        E5 = [(((r[5][i] + r[-5][i])/2 - r0[i] - 3814697265625*r18[i])/25 - E1[i])/24 for i in xrange(L)]
        E6 = [(((r[6][i] + r[-6][i])/2 - r0[i] - 101559956668416*r18[i])/36 - E1[i])/35 for i in xrange(L)]
        E7 = [(((r[7][i] + r[-7][i])/2 - r0[i] - 1628413597910449*r18[i])/49 - E1[i])/48 for i in xrange(L)]
        E8 = [(((r[8][i] + r[-8][i])/2 - r0[i] - 18014398509481984*r18[i])/64 - E1[i])/63 for i in xrange(L)]
        
        # layer 2
        E9 = [(E3[i] - E2[i]) / 5 for i in xrange(L)]
        E10 = [(E4[i] - E3[i]) / 7 for i in xrange(L)]
        E11 = [(E5[i] - E4[i]) / 9 for i in xrange(L)]
        E12 = [(E6[i] - E5[i]) / 11 for i in xrange(L)]
        E13 = [(E7[i] - E6[i]) / 13 for i in xrange(L)]
        E14 = [(E8[i] - E7[i]) / 15 for i in xrange(L)]
        
        # layer 3
        E15 = [(E10[i] - E9[i]) / 12 for i in xrange(L)]
        E16 = [(E11[i] - E10[i]) / 16 for i in xrange(L)]
        E17 = [(E12[i] - E11[i]) / 20 for i in xrange(L)]
        E18 = [(E13[i] - E12[i]) / 24 for i in xrange(L)]
        E19 = [(E14[i] - E13[i]) / 28 for i in xrange(L)]
        
        # layer 4
        E20 = [(E16[i] - E15[i]) / 21 for i in xrange(L)]
        E21 = [(E17[i] - E16[i]) / 27 for i in xrange(L)]
        E22 = [(E18[i] - E17[i]) / 33 for i in xrange(L)]
        E23 = [(E19[i] - E18[i]) / 39 for i in xrange(L)]
        
        # layer 5
        E24 = [(E21[i] - E20[i]) / 32 for i in xrange(L)]
        E25 = [(E22[i] - E21[i]) / 40 for i in xrange(L)]
        E26 = [(E23[i] - E22[i]) / 48 for i in xrange(L)]
        
        # layer 6
        E27 = [(E25[i] - E24[i]) / 45 for i in xrange(L)]
        E28 = [(E26[i] - E25[i]) / 55 for i in xrange(L)]
        
        # the remaining even variables
        r16 = [(E28[i] - E27[i]) / 60 for i in xrange(L)]
        r14 = [E27[i] - 140*r16[i]  for i in xrange(L)]
        r12 = [E24[i] - 91*r14[i] - 5278*r16[i]  for i in xrange(L)]
        r10 = [E20[i] - 55*r12[i] - 2002*r14[i] - 61490*r16[i]  for i in xrange(L)]
        r8 = [E15[i] - 30*r10[i] - 627*r12[i] - 11440*r14[i] - 196053*r16[i]  for i in xrange(L)]
        r6 = [E9[i] - 14*r8[i] - 147*r10[i] - 1408*r12[i] - 13013*r14[i] - 118482*r16[i]  for i in xrange(L)]
        r4 = [E2[i] - 5*r6[i] - 21*r8[i] - 85*r10[i] - 341*r12[i] - 1365*r14[i] - 5461*r16[i]  for i in xrange(L)]
        r2 = [E1[i] - r4[i] - r6[i] - r8[i] - r10[i] - r12[i] - r14[i] - r16[i]  for i in xrange(L)]
        
        # the odd temp variables
        
        # start with O1, since it's not in a layer
        O1 = [(r[1][i] - r[-1][i])/2 for i in xrange(L)]
        
        # layer 1
        O2 = [((r[2][i] - r[-2][i])/4 - O1[i])/3 for i in xrange(L)]
        O3 = [((r[3][i] - r[-3][i])/6 - O1[i])/8 for i in xrange(L)]
        O4 = [((r[4][i] - r[-4][i])/8 - O1[i])/15 for i in xrange(L)]
        O5 = [((r[5][i] - r[-5][i])/10 - O1[i])/24 for i in xrange(L)]
        O6 = [((r[6][i] - r[-6][i])/12 - O1[i])/35 for i in xrange(L)]
        O7 = [((r[7][i] - r[-7][i])/14 - O1[i])/48 for i in xrange(L)]
        O8 = [((r[8][i] - r[-8][i])/16 - O1[i])/63 for i in xrange(L)]
        O9 = [((r[9][i] - r0[i] - 81*r2[i] - 6561*r4[i] - 531441*r6[i] - 43046721*r8[i] - 3486784401*r10[i] - 282429536481*r12[i] - 22876792454961*r14[i] - 1853020188851841*r16[i] - 150094635296999121*r18[i] )/9 - O1[i])/80 for i in xrange(L)]
        
        # layer 2
        O10 = [(O3[i] - O2[i]) / 5 for i in xrange(L)]
        O11 = [(O4[i] - O3[i]) / 7 for i in xrange(L)]
        O12 = [(O5[i] - O4[i]) / 9 for i in xrange(L)]
        O13 = [(O6[i] - O5[i]) / 11 for i in xrange(L)]
        O14 = [(O7[i] - O6[i]) / 13 for i in xrange(L)]
        O15 = [(O8[i] - O7[i]) / 15 for i in xrange(L)]
        O16 = [(O9[i] - O8[i]) / 17 for i in xrange(L)]
        
        # layer 3
        O17 = [(O11[i] - O10[i]) / 12 for i in xrange(L)]
        O18 = [(O12[i] - O11[i]) / 16 for i in xrange(L)]
        O19 = [(O13[i] - O12[i]) / 20 for i in xrange(L)]
        O20 = [(O14[i] - O13[i]) / 24 for i in xrange(L)]
        O21 = [(O15[i] - O14[i]) / 28 for i in xrange(L)]
        O22 = [(O16[i] - O15[i]) / 32 for i in xrange(L)]
        
        # layer 4
        O23 = [(O18[i] - O17[i]) / 21 for i in xrange(L)]
        O24 = [(O19[i] - O18[i]) / 27 for i in xrange(L)]
        O25 = [(O20[i] - O19[i]) / 33 for i in xrange(L)]
        O26 = [(O21[i] - O20[i]) / 39 for i in xrange(L)]
        O27 = [(O22[i] - O21[i]) / 45 for i in xrange(L)]
        
        # layer 5
        O28 = [(O24[i] - O23[i]) / 32 for i in xrange(L)]
        O29 = [(O25[i] - O24[i]) / 40 for i in xrange(L)]
        O30 = [(O26[i] - O25[i]) / 48 for i in xrange(L)]
        O31 = [(O27[i] - O26[i]) / 56 for i in xrange(L)]
        
        # layer 6
        O32 = [(O29[i] - O28[i]) / 45 for i in xrange(L)]
        O33 = [(O30[i] - O29[i]) / 55 for i in xrange(L)]
        O34 = [(O31[i] - O30[i]) / 65 for i in xrange(L)]
        
        # layer 7
        O35 = [(O33[i] - O32[i]) / 60 for i in xrange(L)]
        O36 = [(O34[i] - O33[i]) / 72 for i in xrange(L)]
        
        # the remaining odd variables
        r17 = [(O36[i] - O35[i]) / 77 for i in xrange(L)]
        r15 = [O35[i] - 204*r17[i]  for i in xrange(L)]
        r13 = [O32[i] - 140*r15[i] - 12138*r17[i]  for i in xrange(L)]
        r11 = [O28[i] - 91*r13[i] - 5278*r15[i] - 251498*r17[i]  for i in xrange(L)]
        r9 = [O23[i] - 55*r11[i] - 2002*r13[i] - 61490*r15[i] - 1733303*r17[i]  for i in xrange(L)]
        r7 = [O17[i] - 30*r9[i] - 627*r11[i] - 11440*r13[i] - 196053*r15[i] - 3255330*r17[i]  for i in xrange(L)]
        r5 = [O10[i] - 14*r7[i] - 147*r9[i] - 1408*r11[i] - 13013*r13[i] - 118482*r15[i] - 1071799*r17[i]  for i in xrange(L)]
        r3 = [O2[i] - 5*r5[i] - 21*r7[i] - 85*r9[i] - 341*r11[i] - 1365*r13[i] - 5461*r15[i] - 21845*r17[i]  for i in xrange(L)]
        r1 = [O1[i] - r3[i] - r5[i] - r7[i] - r9[i] - r11[i] - r13[i] - r15[i] - r17[i]  for i in xrange(L)]
        
        return (r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18)

    raise ValueError("We have not implement efficient Toom-{}".format(n))