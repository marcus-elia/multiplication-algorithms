def solve_for_coefficients_natural(n, r):
    if n == 2:
        r0 = r[0]
        r2 = r['infinity']
        r1 = [r[1][i] - r0[i] - r2[i] for i in range(len(r0))]
        return (r0, r1, r2)
    
    if n == 3:
        r0 = r[0]

        r4 = r['infinity']

        r2 = [((r[1][i] + r[-1][i])
         - 2*r0[i]
         - 2*r4[i]
        ) // 2 for i in range(len(r0))]

        r3 = [(-2*r[1][i] 
         + r[2][i]
         + 1*r0[i]
         - 2*r2[i]
         - 14*r4[i]
        ) // 6 for i in range(len(r0))]

        r1 = [r[1][i]
         - r0[i]
        - r2[i]
        - r3[i]
        - r4[i]
         for i in range(len(r0))]

        return (r0, r1, r2, r3, r4)
    
    if n == 4:
        r0 = r[0]

        r6 = r['infinity']

        r4 = [(-4*(r[1][i] + r[-1][i])
         + (r[2][i] + r[-2][i])
         + 6*r0[i]
         - 120*r6[i]
        ) // 24 for i in range(len(r0))]

        r2 = [((r[1][i] + r[-1][i])
         - 2*r0[i]
         - 2*r4[i]
         - 2*r6[i]
        ) // 2 for i in range(len(r0))]

        r5 = [(5*r[1][i] 
         - 4*r[2][i]
         + r[3][i]
         - 2*r0[i]
         + 2*r2[i]
         - 22*r4[i]
         - 478*r6[i]
        ) // 120 for i in range(len(r0))]

        r3 = [(-2*r[1][i] 
         + r[2][i]
         + 1*r0[i]
         - 2*r2[i]
         - 14*r4[i]
         - 30*r5[i]
         - 62*r6[i]
        ) // 6 for i in range(len(r0))]

        r1 = [r[1][i]
         - r0[i]
        - r2[i]
        - r3[i]
        - r4[i]
        - r5[i]
        - r6[i]
         for i in range(len(r0))]

        return (r0, r1, r2, r3, r4, r5, r6)

    if n == 5:
        r0 = r[0]

        r8 = r['infinity']
        
        r6 = [(15*(r[1][i] + r[-1][i])
         - 6*(r[2][i] + r[-2][i])
         + (r[3][i] + r[-3][i])
         - 20*r0[i]
         - 10080*r8[i]
        ) // 720 for i in range(len(r0))]
        
        r4 = [(-4*(r[1][i] + r[-1][i])
         + (r[2][i] + r[-2][i])
         + 6*r0[i]
         - 120*r6[i]
         - 504*r8[i]
        ) // 24 for i in range(len(r0))]
        
        r2 = [((r[1][i] + r[-1][i])
         - 2*r0[i]
         - 2*r4[i]
         - 2*r6[i]
         - 2*r8[i]
        ) // 2 for i in range(len(r0))]
        
        r7 = [(-14*r[1][i] 
         + 14*r[2][i]
         - 6*r[3][i]
         + r[4][i]
         + 5*r0[i]
         - 4*r2[i]
         + 20*r4[i]
         - 604*r6[i]
         - 29740*r8[i]
        ) // 5040 for i in range(len(r0))]
        
        r5 = [(5*r[1][i] 
         - 4*r[2][i]
         + r[3][i]
         - 2*r0[i]
         + 2*r2[i]
         - 22*r4[i]
         - 478*r6[i]
         - 1680*r7[i]
         - 5542*r8[i]
        ) // 120 for i in range(len(r0))]
        
        r3 = [(-2*r[1][i] 
         + r[2][i]
         + 1*r0[i]
         - 2*r2[i]
         - 14*r4[i]
         - 30*r5[i]
         - 62*r6[i]
         - 126*r7[i]
         - 254*r8[i]
        ) // 6 for i in range(len(r0))]
        
        r1 = [r[1][i]
         - r0[i]
        - r2[i]
        - r3[i]
        - r4[i]
        - r5[i]
        - r6[i]
        - r7[i]
        - r8[i]
         for i in range(len(r0))]
        
        return (r0, r1, r2, r3, r4, r5, r6, r7, r8)
    
    if n == 6:
        r0 = r[0]

        r10 = r['infinity']
        
        r8 = [(-56*(r[1][i] + r[-1][i])
         + 28*(r[2][i] + r[-2][i])
         - 8*(r[3][i] + r[-3][i])
         + (r[4][i] + r[-4][i])
         + 70*r0[i]
         - 1209600*r10[i]
        ) // 40320 for i in range(len(r0))]
        
        r6 = [(15*(r[1][i] + r[-1][i])
         - 6*(r[2][i] + r[-2][i])
         + (r[3][i] + r[-3][i])
         - 20*r0[i]
         - 10080*r8[i]
         - 105840*r10[i]
        ) // 720 for i in range(len(r0))]
        
        r4 = [(-4*(r[1][i] + r[-1][i])
         + (r[2][i] + r[-2][i])
         + 6*r0[i]
         - 120*r6[i]
         - 504*r8[i]
         - 2040*r10[i]
        ) // 24 for i in range(len(r0))]
        
        r2 = [((r[1][i] + r[-1][i])
         - 2*r0[i]
         - 2*r4[i]
         - 2*r6[i]
         - 2*r8[i]
         - 2*r10[i]
        ) // 2 for i in range(len(r0))]
        
        r9 = [(42*r[1][i] 
         - 48*r[2][i]
         + 27*r[3][i]
         - 8*r[4][i]
         + r[5][i]
         - 14*r0[i]
         + 10*r2[i]
         - 38*r4[i]
         + 490*r6[i]
         - 31238*r8[i]
         - 2922230*r10[i]
        ) // 362880 for i in range(len(r0))]
        
        r7 = [(-14*r[1][i] 
         + 14*r[2][i]
         - 6*r[3][i]
         + r[4][i]
         + 5*r0[i]
         - 4*r2[i]
         + 20*r4[i]
         - 604*r6[i]
         - 29740*r8[i]
         - 151200*r9[i]
         - 708604*r10[i]
        ) // 5040 for i in range(len(r0))]
        
        r5 = [(5*r[1][i] 
         - 4*r[2][i]
         + r[3][i]
         - 2*r0[i]
         + 2*r2[i]
         - 22*r4[i]
         - 478*r6[i]
         - 1680*r7[i]
         - 5542*r8[i]
         - 17640*r9[i]
         - 54958*r10[i]
        ) // 120 for i in range(len(r0))]
        
        r3 = [(-2*r[1][i] 
         + r[2][i]
         + 1*r0[i]
         - 2*r2[i]
         - 14*r4[i]
         - 30*r5[i]
         - 62*r6[i]
         - 126*r7[i]
         - 254*r8[i]
         - 510*r9[i]
         - 1022*r10[i]
        ) // 6 for i in range(len(r0))]
        
        r1 = [r[1][i]
         - r0[i]
        - r2[i]
        - r3[i]
        - r4[i]
        - r5[i]
        - r6[i]
        - r7[i]
        - r8[i]
        - r9[i]
        - r10[i]
         for i in range(len(r0))]
        
        return (r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10)
    
    if n == 7:
        r0 = r[0]

        r12 = r['infinity']
        
        r10 = [(210*(r[1][i] + r[-1][i])
         - 120*(r[2][i] + r[-2][i])
         + 45*(r[3][i] + r[-3][i])
         - 10*(r[4][i] + r[-4][i])
         + (r[5][i] + r[-5][i])
         - 252*r0[i]
         - 199584000*r12[i]
        ) // 3628800 for i in range(len(r0))]
        
        r8 = [(-56*(r[1][i] + r[-1][i])
         + 28*(r[2][i] + r[-2][i])
         - 8*(r[3][i] + r[-3][i])
         + (r[4][i] + r[-4][i])
         + 70*r0[i]
         - 1209600*r10[i]
         - 25280640*r12[i]
        ) // 40320 for i in range(len(r0))]
        
        r6 = [(15*(r[1][i] + r[-1][i])
         - 6*(r[2][i] + r[-2][i])
         + (r[3][i] + r[-3][i])
         - 20*r0[i]
         - 10080*r8[i]
         - 105840*r10[i]
         - 1013760*r12[i]
        ) // 720 for i in range(len(r0))]
        
        r4 = [(-4*(r[1][i] + r[-1][i])
         + (r[2][i] + r[-2][i])
         + 6*r0[i]
         - 120*r6[i]
         - 504*r8[i]
         - 2040*r10[i]
         - 8184*r12[i]
        ) // 24 for i in range(len(r0))]
        
        r2 = [((r[1][i] + r[-1][i])
         - 2*r0[i]
         - 2*r4[i]
         - 2*r6[i]
         - 2*r8[i]
         - 2*r10[i]
         - 2*r12[i]
        ) // 2 for i in range(len(r0))]
        
        r11 = [(-132*r[1][i] 
         + 165*r[2][i]
         - 110*r[3][i]
         + 44*r[4][i]
         - 10*r[5][i]
         + r[6][i]
         + 42*r0[i]
         - 28*r2[i]
         + 92*r4[i]
         - 868*r6[i]
         + 22652*r8[i]
         - 2620708*r10[i]
         - 415790788*r12[i]
        ) // 39916800 for i in range(len(r0))]
        
        r9 = [(42*r[1][i] 
         - 48*r[2][i]
         + 27*r[3][i]
         - 8*r[4][i]
         + r[5][i]
         - 14*r0[i]
         + 10*r2[i]
         - 38*r4[i]
         + 490*r6[i]
         - 31238*r8[i]
         - 2922230*r10[i]
         - 19958400*r11[i]
         - 124075238*r12[i]
        ) // 362880 for i in range(len(r0))]
        
        r7 = [(-14*r[1][i] 
         + 14*r[2][i]
         - 6*r[3][i]
         + r[4][i]
         + 5*r0[i]
         - 4*r2[i]
         + 20*r4[i]
         - 604*r6[i]
         - 29740*r8[i]
         - 151200*r9[i]
         - 708604*r10[i]
         - 3160080*r11[i]
         - 13645900*r12[i]
        ) // 5040 for i in range(len(r0))]
        
        r5 = [(5*r[1][i] 
         - 4*r[2][i]
         + r[3][i]
         - 2*r0[i]
         + 2*r2[i]
         - 22*r4[i]
         - 478*r6[i]
         - 1680*r7[i]
         - 5542*r8[i]
         - 17640*r9[i]
         - 54958*r10[i]
         - 168960*r11[i]
         - 515062*r12[i]
        ) // 120 for i in range(len(r0))]
        
        r3 = [(-2*r[1][i] 
         + r[2][i]
         + 1*r0[i]
         - 2*r2[i]
         - 14*r4[i]
         - 30*r5[i]
         - 62*r6[i]
         - 126*r7[i]
         - 254*r8[i]
         - 510*r9[i]
         - 1022*r10[i]
         - 2046*r11[i]
         - 4094*r12[i]
        ) // 6 for i in range(len(r0))]
        
        r1 = [r[1][i]
         - r0[i]
        - r2[i]
        - r3[i]
        - r4[i]
        - r5[i]
        - r6[i]
        - r7[i]
        - r8[i]
        - r9[i]
        - r10[i]
        - r11[i]
        - r12[i]
         for i in range(len(r0))]
        
        return (r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12)
    
    if n == 8:
        r0 = r[0]

        r14 = r['infinity']
        
        r12 = [(-792*(r[1][i] + r[-1][i])
         + 495*(r[2][i] + r[-2][i])
         - 220*(r[3][i] + r[-3][i])
         + 66*(r[4][i] + r[-4][i])
         - 12*(r[5][i] + r[-5][i])
         + (r[6][i] + r[-6][i])
         + 924*r0[i]
         - 43589145600*r14[i]
        ) // 479001600 for i in range(len(r0))]
        
        r10 = [(210*(r[1][i] + r[-1][i])
         - 120*(r[2][i] + r[-2][i])
         + 45*(r[3][i] + r[-3][i])
         - 10*(r[4][i] + r[-4][i])
         + (r[5][i] + r[-5][i])
         - 252*r0[i]
         - 199584000*r12[i]
         - 7264857600*r14[i]
        ) // 3628800 for i in range(len(r0))]
        
        r8 = [(-56*(r[1][i] + r[-1][i])
         + 28*(r[2][i] + r[-2][i])
         - 8*(r[3][i] + r[-3][i])
         + (r[4][i] + r[-4][i])
         + 70*r0[i]
         - 1209600*r10[i]
         - 25280640*r12[i]
         - 461260800*r14[i]
        ) // 40320 for i in range(len(r0))]
        
        r6 = [(15*(r[1][i] + r[-1][i])
         - 6*(r[2][i] + r[-2][i])
         + (r[3][i] + r[-3][i])
         - 20*r0[i]
         - 10080*r8[i]
         - 105840*r10[i]
         - 1013760*r12[i]
         - 9369360*r14[i]
        ) // 720 for i in range(len(r0))]
        
        r4 = [(-4*(r[1][i] + r[-1][i])
         + (r[2][i] + r[-2][i])
         + 6*r0[i]
         - 120*r6[i]
         - 504*r8[i]
         - 2040*r10[i]
         - 8184*r12[i]
         - 32760*r14[i]
        ) // 24 for i in range(len(r0))]
        
        r2 = [((r[1][i] + r[-1][i])
         - 2*r0[i]
         - 2*r4[i]
         - 2*r6[i]
         - 2*r8[i]
         - 2*r10[i]
         - 2*r12[i]
         - 2*r14[i]
        ) // 2 for i in range(len(r0))]
        
        r13 = [(429*r[1][i] 
         - 572*r[2][i]
         + 429*r[3][i]
         - 208*r[4][i]
         + 65*r[5][i]
         - 12*r[6][i]
         + r[7][i]
         - 132*r0[i]
         + 84*r2[i]
         - 252*r4[i]
         + 2004*r6[i]
         - 37212*r8[i]
         + 1710324*r10[i]
         - 325024572*r12[i]
         - 80789566956*r14[i]
        ) // 6227020800 for i in range(len(r0))]
        
        r11 = [(-132*r[1][i] 
         + 165*r[2][i]
         - 110*r[3][i]
         + 44*r[4][i]
         - 10*r[5][i]
         + r[6][i]
         + 42*r0[i]
         - 28*r2[i]
         + 92*r4[i]
         - 868*r6[i]
         + 22652*r8[i]
         - 2620708*r10[i]
         - 415790788*r12[i]
         - 3632428800*r13[i]
         - 28616744548*r14[i]
        ) // 39916800 for i in range(len(r0))]
        
        r9 = [(42*r[1][i] 
         - 48*r[2][i]
         + 27*r[3][i]
         - 8*r[4][i]
         + r[5][i]
         - 14*r0[i]
         + 10*r2[i]
         - 38*r4[i]
         + 490*r6[i]
         - 31238*r8[i]
         - 2922230*r10[i]
         - 19958400*r11[i]
         - 124075238*r12[i]
         - 726485760*r13[i]
         - 4084385750*r14[i]
        ) // 362880 for i in range(len(r0))]
        
        r7 = [(-14*r[1][i] 
         + 14*r[2][i]
         - 6*r[3][i]
         + r[4][i]
         + 5*r0[i]
         - 4*r2[i]
         + 20*r4[i]
         - 604*r6[i]
         - 29740*r8[i]
         - 151200*r9[i]
         - 708604*r10[i]
         - 3160080*r11[i]
         - 13645900*r12[i]
         - 57657600*r13[i]
         - 239967004*r14[i]
        ) // 5040 for i in range(len(r0))]
        
        r5 = [(5*r[1][i] 
         - 4*r[2][i]
         + r[3][i]
         - 2*r0[i]
         + 2*r2[i]
         - 22*r4[i]
         - 478*r6[i]
         - 1680*r7[i]
         - 5542*r8[i]
         - 17640*r9[i]
         - 54958*r10[i]
         - 168960*r11[i]
         - 515062*r12[i]
         - 1561560*r13[i]
         - 4717438*r14[i]
        ) // 120 for i in range(len(r0))]
        
        r3 = [(-2*r[1][i] 
         + r[2][i]
         + 1*r0[i]
         - 2*r2[i]
         - 14*r4[i]
         - 30*r5[i]
         - 62*r6[i]
         - 126*r7[i]
         - 254*r8[i]
         - 510*r9[i]
         - 1022*r10[i]
         - 2046*r11[i]
         - 4094*r12[i]
         - 8190*r13[i]
         - 16382*r14[i]
        ) // 6 for i in range(len(r0))]
        
        r1 = [r[1][i]
         - r0[i]
        - r2[i]
        - r3[i]
        - r4[i]
        - r5[i]
        - r6[i]
        - r7[i]
        - r8[i]
        - r9[i]
        - r10[i]
        - r11[i]
        - r12[i]
        - r13[i]
        - r14[i]
         for i in range(len(r0))]
        
        return (r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14)
    
    if n == 9:
        r0 = r[0]

        r16 = r['infinity']
        
        r14 = [(3003*(r[1][i] + r[-1][i])
         - 2002*(r[2][i] + r[-2][i])
         + 1001*(r[3][i] + r[-3][i])
         - 364*(r[4][i] + r[-4][i])
         + 91*(r[5][i] + r[-5][i])
         - 14*(r[6][i] + r[-6][i])
         + (r[7][i] + r[-7][i])
         - 3432*r0[i]
         - 12204960768000*r16[i]
        ) // 87178291200 for i in range(len(r0))]
        
        r12 = [(-792*(r[1][i] + r[-1][i])
         + 495*(r[2][i] + r[-2][i])
         - 220*(r[3][i] + r[-3][i])
         + 66*(r[4][i] + r[-4][i])
         - 12*(r[5][i] + r[-5][i])
         + (r[6][i] + r[-6][i])
         + 924*r0[i]
         - 43589145600*r14[i]
         - 2528170444800*r16[i]
        ) // 479001600 for i in range(len(r0))]
        
        r10 = [(210*(r[1][i] + r[-1][i])
         - 120*(r[2][i] + r[-2][i])
         + 45*(r[3][i] + r[-3][i])
         - 10*(r[4][i] + r[-4][i])
         + (r[5][i] + r[-5][i])
         - 252*r0[i]
         - 199584000*r12[i]
         - 7264857600*r14[i]
         - 223134912000*r16[i]
        ) // 3628800 for i in range(len(r0))]
        
        r8 = [(-56*(r[1][i] + r[-1][i])
         + 28*(r[2][i] + r[-2][i])
         - 8*(r[3][i] + r[-3][i])
         + (r[4][i] + r[-4][i])
         + 70*r0[i]
         - 1209600*r10[i]
         - 25280640*r12[i]
         - 461260800*r14[i]
         - 7904856960*r16[i]
        ) // 40320 for i in range(len(r0))]
        
        r6 = [(15*(r[1][i] + r[-1][i])
         - 6*(r[2][i] + r[-2][i])
         + (r[3][i] + r[-3][i])
         - 20*r0[i]
         - 10080*r8[i]
         - 105840*r10[i]
         - 1013760*r12[i]
         - 9369360*r14[i]
         - 85307040*r16[i]
        ) // 720 for i in range(len(r0))]
        
        r4 = [(-4*(r[1][i] + r[-1][i])
         + (r[2][i] + r[-2][i])
         + 6*r0[i]
         - 120*r6[i]
         - 504*r8[i]
         - 2040*r10[i]
         - 8184*r12[i]
         - 32760*r14[i]
         - 131064*r16[i]
        ) // 24 for i in range(len(r0))]
        
        r2 = [((r[1][i] + r[-1][i])
         - 2*r0[i]
         - 2*r4[i]
         - 2*r6[i]
         - 2*r8[i]
         - 2*r10[i]
         - 2*r12[i]
         - 2*r14[i]
         - 2*r16[i]
        ) // 2 for i in range(len(r0))]
        
        r15 = [(-1430*r[1][i] 
         + 2002*r[2][i]
         - 1638*r[3][i]
         + 910*r[4][i]
         - 350*r[5][i]
         + 90*r[6][i]
         - 14*r[7][i]
         + r[8][i]
         + 429*r0[i]
         - 264*r2[i]
         + 744*r4[i]
         - 5304*r6[i]
         + 81384*r8[i]
         - 2605944*r10[i]
         + 192387624*r12[i]
         - 55942352184*r14[i]
         - 20546119600536*r16[i]
        ) // 1307674368000 for i in range(len(r0))]
        
        r13 = [(429*r[1][i] 
         - 572*r[2][i]
         + 429*r[3][i]
         - 208*r[4][i]
         + 65*r[5][i]
         - 12*r[6][i]
         + r[7][i]
         - 132*r0[i]
         + 84*r2[i]
         - 252*r4[i]
         + 2004*r6[i]
         - 37212*r8[i]
         + 1710324*r10[i]
         - 325024572*r12[i]
         - 80789566956*r14[i]
         - 871782912000*r15[i]
         - 8422900930332*r16[i]
        ) // 6227020800 for i in range(len(r0))]
        
        r11 = [(-132*r[1][i] 
         + 165*r[2][i]
         - 110*r[3][i]
         + 44*r[4][i]
         - 10*r[5][i]
         + r[6][i]
         + 42*r0[i]
         - 28*r2[i]
         + 92*r4[i]
         - 868*r6[i]
         + 22652*r8[i]
         - 2620708*r10[i]
         - 415790788*r12[i]
         - 3632428800*r13[i]
         - 28616744548*r14[i]
         - 210680870400*r15[i]
         - 1479485236228*r16[i]
        ) // 39916800 for i in range(len(r0))]
        
        r9 = [(42*r[1][i] 
         - 48*r[2][i]
         + 27*r[3][i]
         - 8*r[4][i]
         + r[5][i]
         - 14*r0[i]
         + 10*r2[i]
         - 38*r4[i]
         + 490*r6[i]
         - 31238*r8[i]
         - 2922230*r10[i]
         - 19958400*r11[i]
         - 124075238*r12[i]
         - 726485760*r13[i]
         - 4084385750*r14[i]
         - 22313491200*r15[i]
         - 119387268038*r16[i]
        ) // 362880 for i in range(len(r0))]
        
        r7 = [(-14*r[1][i] 
         + 14*r[2][i]
         - 6*r[3][i]
         + r[4][i]
         + 5*r0[i]
         - 4*r2[i]
         + 20*r4[i]
         - 604*r6[i]
         - 29740*r8[i]
         - 151200*r9[i]
         - 708604*r10[i]
         - 3160080*r11[i]
         - 13645900*r12[i]
         - 57657600*r13[i]
         - 239967004*r14[i]
         - 988107120*r15[i]
         - 4037604460*r16[i]
        ) // 5040 for i in range(len(r0))]
        
        r5 = [(5*r[1][i] 
         - 4*r[2][i]
         + r[3][i]
         - 2*r0[i]
         + 2*r2[i]
         - 22*r4[i]
         - 478*r6[i]
         - 1680*r7[i]
         - 5542*r8[i]
         - 17640*r9[i]
         - 54958*r10[i]
         - 168960*r11[i]
         - 515062*r12[i]
         - 1561560*r13[i]
         - 4717438*r14[i]
         - 14217840*r15[i]
         - 42784582*r16[i]
        ) // 120 for i in range(len(r0))]
        
        r3 = [(-2*r[1][i] 
         + r[2][i]
         + 1*r0[i]
         - 2*r2[i]
         - 14*r4[i]
         - 30*r5[i]
         - 62*r6[i]
         - 126*r7[i]
         - 254*r8[i]
         - 510*r9[i]
         - 1022*r10[i]
         - 2046*r11[i]
         - 4094*r12[i]
         - 8190*r13[i]
         - 16382*r14[i]
         - 32766*r15[i]
         - 65534*r16[i]
        ) // 6 for i in range(len(r0))]
        
        r1 = [r[1][i]
         - r0[i]
        - r2[i]
        - r3[i]
        - r4[i]
        - r5[i]
        - r6[i]
        - r7[i]
        - r8[i]
        - r9[i]
        - r10[i]
        - r11[i]
        - r12[i]
        - r13[i]
        - r14[i]
        - r15[i]
        - r16[i]
         for i in range(len(r0))]
        
        return (r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16)

    if n == 10:
        r0 = r[0]

        r18 = r['infinity']
        
        r16 = [(-11440*(r[1][i] + r[-1][i])
         + 8008*(r[2][i] + r[-2][i])
         - 4368*(r[3][i] + r[-3][i])
         + 1820*(r[4][i] + r[-4][i])
         - 560*(r[5][i] + r[-5][i])
         + 120*(r[6][i] + r[-6][i])
         - 16*(r[7][i] + r[-7][i])
         + (r[8][i] + r[-8][i])
         + 12870*r0[i]
         - 4268249137152000*r18[i]
        ) // 20922789888000 for i in range(len(r0))]
        
        r14 = [(3003*(r[1][i] + r[-1][i])
         - 2002*(r[2][i] + r[-2][i])
         + 1001*(r[3][i] + r[-3][i])
         - 364*(r[4][i] + r[-4][i])
         + 91*(r[5][i] + r[-5][i])
         - 14*(r[6][i] + r[-6][i])
         + (r[7][i] + r[-7][i])
         - 3432*r0[i]
         - 12204960768000*r16[i]
         - 1058170098585600*r18[i]
        ) // 87178291200 for i in range(len(r0))]
        
        r12 = [(-792*(r[1][i] + r[-1][i])
         + 495*(r[2][i] + r[-2][i])
         - 220*(r[3][i] + r[-3][i])
         + 66*(r[4][i] + r[-4][i])
         - 12*(r[5][i] + r[-5][i])
         + (r[6][i] + r[-6][i])
         + 924*r0[i]
         - 43589145600*r14[i]
         - 2528170444800*r16[i]
         - 120467944396800*r18[i]
        ) // 479001600 for i in range(len(r0))]
        
        r10 = [(210*(r[1][i] + r[-1][i])
         - 120*(r[2][i] + r[-2][i])
         + 45*(r[3][i] + r[-3][i])
         - 10*(r[4][i] + r[-4][i])
         + (r[5][i] + r[-5][i])
         - 252*r0[i]
         - 199584000*r12[i]
         - 7264857600*r14[i]
         - 223134912000*r16[i]
         - 6289809926400*r18[i]
        ) // 3628800 for i in range(len(r0))]
        
        r8 = [(-56*(r[1][i] + r[-1][i])
         + 28*(r[2][i] + r[-2][i])
         - 8*(r[3][i] + r[-3][i])
         + (r[4][i] + r[-4][i])
         + 70*r0[i]
         - 1209600*r10[i]
         - 25280640*r12[i]
         - 461260800*r14[i]
         - 7904856960*r16[i]
         - 131254905600*r18[i]
        ) // 40320 for i in range(len(r0))]
        
        r6 = [(15*(r[1][i] + r[-1][i])
         - 6*(r[2][i] + r[-2][i])
         + (r[3][i] + r[-3][i])
         - 20*r0[i]
         - 10080*r8[i]
         - 105840*r10[i]
         - 1013760*r12[i]
         - 9369360*r14[i]
         - 85307040*r16[i]
         - 771695280*r18[i]
        ) // 720 for i in range(len(r0))]
        
        r4 = [(-4*(r[1][i] + r[-1][i])
         + (r[2][i] + r[-2][i])
         + 6*r0[i]
         - 120*r6[i]
         - 504*r8[i]
         - 2040*r10[i]
         - 8184*r12[i]
         - 32760*r14[i]
         - 131064*r16[i]
         - 524280*r18[i]
        ) // 24 for i in range(len(r0))]
        
        r2 = [((r[1][i] + r[-1][i])
         - 2*r0[i]
         - 2*r4[i]
         - 2*r6[i]
         - 2*r8[i]
         - 2*r10[i]
         - 2*r12[i]
         - 2*r14[i]
         - 2*r16[i]
         - 2*r18[i]
        ) // 2 for i in range(len(r0))]
        
        r17 = [(4862*r[1][i] 
         - 7072*r[2][i]
         + 6188*r[3][i]
         - 3808*r[4][i]
         + 1700*r[5][i]
         - 544*r[6][i]
         + 119*r[7][i]
         - 16*r[8][i]
         + r[9][i]
         - 1430*r0[i]
         + 858*r2[i]
         - 2310*r4[i]
         + 15258*r6[i]
         - 206790*r8[i]
         + 5386458*r10[i]
         - 272513670*r12[i]
         + 30255826458*r14[i]
         - 12765597850950*r16[i]
         - 6622557957272742*r18[i]
        ) // 355687428096000 for i in range(len(r0))]
        
        r15 = [(-1430*r[1][i] 
         + 2002*r[2][i]
         - 1638*r[3][i]
         + 910*r[4][i]
         - 350*r[5][i]
         + 90*r[6][i]
         - 14*r[7][i]
         + r[8][i]
         + 429*r0[i]
         - 264*r2[i]
         + 744*r4[i]
         - 5304*r6[i]
         + 81384*r8[i]
         - 2605944*r10[i]
         + 192387624*r12[i]
         - 55942352184*r14[i]
         - 20546119600536*r16[i]
         - 266765571072000*r17[i]
         - 3083760849804024*r18[i]
        ) // 1307674368000 for i in range(len(r0))]
        
        r13 = [(429*r[1][i] 
         - 572*r[2][i]
         + 429*r[3][i]
         - 208*r[4][i]
         + 65*r[5][i]
         - 12*r[6][i]
         + r[7][i]
         - 132*r0[i]
         + 84*r2[i]
         - 252*r4[i]
         + 2004*r6[i]
         - 37212*r8[i]
         + 1710324*r10[i]
         - 325024572*r12[i]
         - 80789566956*r14[i]
         - 871782912000*r15[i]
         - 8422900930332*r16[i]
         - 75583578470400*r17[i]
         - 643521842437836*r18[i]
        ) // 6227020800 for i in range(len(r0))]
        
        r11 = [(-132*r[1][i] 
         + 165*r[2][i]
         - 110*r[3][i]
         + 44*r[4][i]
         - 10*r[5][i]
         + r[6][i]
         + 42*r0[i]
         - 28*r2[i]
         + 92*r4[i]
         - 868*r6[i]
         + 22652*r8[i]
         - 2620708*r10[i]
         - 415790788*r12[i]
         - 3632428800*r13[i]
         - 28616744548*r14[i]
         - 210680870400*r15[i]
         - 1479485236228*r16[i]
         - 10038995366400*r17[i]
         - 66394067988388*r18[i]
        ) // 39916800 for i in range(len(r0))]
        
        r9 = [(42*r[1][i] 
         - 48*r[2][i]
         + 27*r[3][i]
         - 8*r[4][i]
         + r[5][i]
         - 14*r0[i]
         + 10*r2[i]
         - 38*r4[i]
         + 490*r6[i]
         - 31238*r8[i]
         - 2922230*r10[i]
         - 19958400*r11[i]
         - 124075238*r12[i]
         - 726485760*r13[i]
         - 4084385750*r14[i]
         - 22313491200*r15[i]
         - 119387268038*r16[i]
         - 628980992640*r17[i]
         - 3275389222070*r18[i]
        ) // 362880 for i in range(len(r0))]
        
        r7 = [(-14*r[1][i] 
         + 14*r[2][i]
         - 6*r[3][i]
         + r[4][i]
         + 5*r0[i]
         - 4*r2[i]
         + 20*r4[i]
         - 604*r6[i]
         - 29740*r8[i]
         - 151200*r9[i]
         - 708604*r10[i]
         - 3160080*r11[i]
         - 13645900*r12[i]
         - 57657600*r13[i]
         - 239967004*r14[i]
         - 988107120*r15[i]
         - 4037604460*r16[i]
         - 16406863200*r17[i]
         - 66398623804*r18[i]
        ) // 5040 for i in range(len(r0))]
        
        r5 = [(5*r[1][i] 
         - 4*r[2][i]
         + r[3][i]
         - 2*r0[i]
         + 2*r2[i]
         - 22*r4[i]
         - 478*r6[i]
         - 1680*r7[i]
         - 5542*r8[i]
         - 17640*r9[i]
         - 54958*r10[i]
         - 168960*r11[i]
         - 515062*r12[i]
         - 1561560*r13[i]
         - 4717438*r14[i]
         - 14217840*r15[i]
         - 42784582*r16[i]
         - 128615880*r17[i]
         - 386371918*r18[i]
        ) // 120 for i in range(len(r0))]
        
        r3 = [(-2*r[1][i] 
         + r[2][i]
         + 1*r0[i]
         - 2*r2[i]
         - 14*r4[i]
         - 30*r5[i]
         - 62*r6[i]
         - 126*r7[i]
         - 254*r8[i]
         - 510*r9[i]
         - 1022*r10[i]
         - 2046*r11[i]
         - 4094*r12[i]
         - 8190*r13[i]
         - 16382*r14[i]
         - 32766*r15[i]
         - 65534*r16[i]
         - 131070*r17[i]
         - 262142*r18[i]
        ) // 6 for i in range(len(r0))]
        
        r1 = [r[1][i]
         - r0[i]
        - r2[i]
        - r3[i]
        - r4[i]
        - r5[i]
        - r6[i]
        - r7[i]
        - r8[i]
        - r9[i]
        - r10[i]
        - r11[i]
        - r12[i]
        - r13[i]
        - r14[i]
        - r15[i]
        - r16[i]
        - r17[i]
        - r18[i]
         for i in range(len(r0))]
        
        return (r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18)
    
    raise ValueError("We have not implement natural Toom-{}".format(n))