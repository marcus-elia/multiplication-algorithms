def solve_for_coefficients_efficient(n, r):
	if n == 2:
		return efficient_interpolate_2(r)

	elif n == 3:
		return efficient_interpolate_3(r)

	elif n == 4:
		return efficient_interpolate_4(r)

	elif n == 5:
		return efficient_interpolate_5(r)

	elif n == 6:
		return efficient_interpolate_6(r)

	elif n == 7:
		return efficient_interpolate_7(r)

	elif n == 8:
		return efficient_interpolate_8(r)

	elif n == 9:
		return efficient_interpolate_9(r)

	elif n == 10:
		return efficient_interpolate_10(r)

	elif n == 11:
		return efficient_interpolate_11(r)

	elif n == 12:
		return efficient_interpolate_12(r)

	elif n == 13:
		return efficient_interpolate_13(r)

	elif n == 14:
		return efficient_interpolate_14(r)

	elif n == 15:
		return efficient_interpolate_15(r)

	else:
		raise ValueError("Toom-{} is not implemented".format(n))

def efficient_interpolate_2(r):
	r0 = r[0]
	r2 = r['infinity']
	r1 = [r[1][i] - r0[i] - r2[i] for i in range(len(r0))]
	return (r0, r1, r2)

def efficient_interpolate_3(r):
	r0 = r[0]
	r4 = r['infinity']

	L = len(r0)

	r2 = [((r[1][i] + r[-1][i])
	 - 2*r0[i]
	 - 2*r4[i]
	) // 2 for i in range(len(r0))]

	O1 = [(r[1][i] - r[-1][i])//2 for i in range(L)]

	r3 = [((r[2][i] - r0[i] - 4*r2[i] - 16*r4[i])//2 - O1[i])//3 for i in range(L)]
	r1 = [O1[i] - r3[i] for i in range(L)]

	return (r0, r1, r2, r3, r4)

def efficient_interpolate_4(r):
	r0 = r[0]
	r6 = r['infinity']

	L = len(r0)

	# the even temp variables

	# start with E1, since it's not in a layer
	E1 = [(r[1][i] + r[-1][i])//2 - r0[i] - r6[i] for i in range(L)]

	# the remaining even variables
	r4 = [(((r[2][i] + r[-2][i])//2 - r0[i] - 64*r6[i])//4 - E1[i])//3 for i in range(L)]
	r2 = [E1[i] - r4[i]  for i in range(L)]

	# the odd temp variables

	# start with O1, since it's not in a layer
	O1 = [(r[1][i] - r[-1][i])//2 for i in range(L)]

	# layer 1
	O2 = [((r[2][i] - r[-2][i])//4 - O1[i])//3 for i in range(L)]
	O3 = [((r[3][i] - r0[i] - 9*r2[i] - 81*r4[i] - 729*r6[i] )//3 - O1[i])//8 for i in range(L)]

	# the remaining odd variables
	r5 = [(O3[i] - O2[i]) // 5 for i in range(L)]
	r3 = [O2[i] - 5*r5[i]  for i in range(L)]
	r1 = [O1[i] - r3[i] - r5[i]  for i in range(L)]

	return (r0, r1, r2, r3, r4, r5, r6)

def efficient_interpolate_5(r):
	r0 = r[0]
	r8 = r['infinity']

	L = len(r0)

	# the even temp variables

	# start with E1, since it's not in a layer
	E1 = [(r[1][i] + r[-1][i])//2 - r0[i] - r8[i] for i in range(L)]

	# layer 1
	E2 = [(((r[2][i] + r[-2][i])//2 - r0[i] - 256*r8[i])//4 - E1[i])//3 for i in range(L)]
	E3 = [(((r[3][i] + r[-3][i])//2 - r0[i] - 6561*r8[i])//9 - E1[i])//8 for i in range(L)]

	# the remaining even variables
	r6 = [(E3[i] - E2[i]) // 5 for i in range(L)]
	r4 = [E2[i] - 5*r6[i]  for i in range(L)]
	r2 = [E1[i] - r4[i] - r6[i]  for i in range(L)]

	# the odd temp variables

	# start with O1, since it's not in a layer
	O1 = [(r[1][i] - r[-1][i])//2 for i in range(L)]

	# layer 1
	O2 = [((r[2][i] - r[-2][i])//4 - O1[i])//3 for i in range(L)]
	O3 = [((r[3][i] - r[-3][i])//6 - O1[i])//8 for i in range(L)]
	O4 = [((r[4][i] - r0[i] - 16*r2[i] - 256*r4[i] - 4096*r6[i] - 65536*r8[i] )//4 - O1[i])//15 for i in range(L)]

	# layer 2
	O5 = [(O3[i] - O2[i]) // 5 for i in range(L)]
	O6 = [(O4[i] - O3[i]) // 7 for i in range(L)]

	# the remaining odd variables
	r7 = [(O6[i] - O5[i]) // 12 for i in range(L)]
	r5 = [O5[i] - 14*r7[i]  for i in range(L)]
	r3 = [O2[i] - 5*r5[i] - 21*r7[i]  for i in range(L)]
	r1 = [O1[i] - r3[i] - r5[i] - r7[i]  for i in range(L)]

	return (r0, r1, r2, r3, r4, r5, r6, r7, r8)

def efficient_interpolate_6(r):
	r0 = r[0]
	r10 = r['infinity']

	L = len(r0)

	# the even temp variables

	# start with E1, since it's not in a layer
	E1 = [(r[1][i] + r[-1][i])//2 - r0[i] - r10[i] for i in range(L)]

	# layer 1
	E2 = [(((r[2][i] + r[-2][i])//2 - r0[i] - 1024*r10[i])//4 - E1[i])//3 for i in range(L)]
	E3 = [(((r[3][i] + r[-3][i])//2 - r0[i] - 59049*r10[i])//9 - E1[i])//8 for i in range(L)]
	E4 = [(((r[4][i] + r[-4][i])//2 - r0[i] - 1048576*r10[i])//16 - E1[i])//15 for i in range(L)]

	# layer 2
	E5 = [(E3[i] - E2[i]) // 5 for i in range(L)]
	E6 = [(E4[i] - E3[i]) // 7 for i in range(L)]

	# the remaining even variables
	r8 = [(E6[i] - E5[i]) // 12 for i in range(L)]
	r6 = [E5[i] - 14*r8[i]  for i in range(L)]
	r4 = [E2[i] - 5*r6[i] - 21*r8[i]  for i in range(L)]
	r2 = [E1[i] - r4[i] - r6[i] - r8[i]  for i in range(L)]

	# the odd temp variables

	# start with O1, since it's not in a layer
	O1 = [(r[1][i] - r[-1][i])//2 for i in range(L)]

	# layer 1
	O2 = [((r[2][i] - r[-2][i])//4 - O1[i])//3 for i in range(L)]
	O3 = [((r[3][i] - r[-3][i])//6 - O1[i])//8 for i in range(L)]
	O4 = [((r[4][i] - r[-4][i])//8 - O1[i])//15 for i in range(L)]
	O5 = [((r[5][i] - r0[i] - 25*r2[i] - 625*r4[i] - 15625*r6[i] - 390625*r8[i] - 9765625*r10[i] )//5 - O1[i])//24 for i in range(L)]

	# layer 2
	O6 = [(O3[i] - O2[i]) // 5 for i in range(L)]
	O7 = [(O4[i] - O3[i]) // 7 for i in range(L)]
	O8 = [(O5[i] - O4[i]) // 9 for i in range(L)]

	# layer 3
	O9 = [(O7[i] - O6[i]) // 12 for i in range(L)]
	O10 = [(O8[i] - O7[i]) // 16 for i in range(L)]

	# the remaining odd variables
	r9 = [(O10[i] - O9[i]) // 21 for i in range(L)]
	r7 = [O9[i] - 30*r9[i]  for i in range(L)]
	r5 = [O6[i] - 14*r7[i] - 147*r9[i]  for i in range(L)]
	r3 = [O2[i] - 5*r5[i] - 21*r7[i] - 85*r9[i]  for i in range(L)]
	r1 = [O1[i] - r3[i] - r5[i] - r7[i] - r9[i]  for i in range(L)]

	return (r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10)

def efficient_interpolate_7(r):
	r0 = r[0]
	r12 = r['infinity']

	L = len(r0)

	# the even temp variables

	# start with E1, since it's not in a layer
	E1 = [(r[1][i] + r[-1][i])//2 - r0[i] - r12[i] for i in range(L)]

	# layer 1
	E2 = [(((r[2][i] + r[-2][i])//2 - r0[i] - 4096*r12[i])//4 - E1[i])//3 for i in range(L)]
	E3 = [(((r[3][i] + r[-3][i])//2 - r0[i] - 531441*r12[i])//9 - E1[i])//8 for i in range(L)]
	E4 = [(((r[4][i] + r[-4][i])//2 - r0[i] - 16777216*r12[i])//16 - E1[i])//15 for i in range(L)]
	E5 = [(((r[5][i] + r[-5][i])//2 - r0[i] - 244140625*r12[i])//25 - E1[i])//24 for i in range(L)]

	# layer 2
	E6 = [(E3[i] - E2[i]) // 5 for i in range(L)]
	E7 = [(E4[i] - E3[i]) // 7 for i in range(L)]
	E8 = [(E5[i] - E4[i]) // 9 for i in range(L)]

	# layer 3
	E9 = [(E7[i] - E6[i]) // 12 for i in range(L)]
	E10 = [(E8[i] - E7[i]) // 16 for i in range(L)]

	# the remaining even variables
	r10 = [(E10[i] - E9[i]) // 21 for i in range(L)]
	r8 = [E9[i] - 30*r10[i]  for i in range(L)]
	r6 = [E6[i] - 14*r8[i] - 147*r10[i]  for i in range(L)]
	r4 = [E2[i] - 5*r6[i] - 21*r8[i] - 85*r10[i]  for i in range(L)]
	r2 = [E1[i] - r4[i] - r6[i] - r8[i] - r10[i]  for i in range(L)]

	# the odd temp variables

	# start with O1, since it's not in a layer
	O1 = [(r[1][i] - r[-1][i])//2 for i in range(L)]

	# layer 1
	O2 = [((r[2][i] - r[-2][i])//4 - O1[i])//3 for i in range(L)]
	O3 = [((r[3][i] - r[-3][i])//6 - O1[i])//8 for i in range(L)]
	O4 = [((r[4][i] - r[-4][i])//8 - O1[i])//15 for i in range(L)]
	O5 = [((r[5][i] - r[-5][i])//10 - O1[i])//24 for i in range(L)]
	O6 = [((r[6][i] - r0[i] - 36*r2[i] - 1296*r4[i] - 46656*r6[i] - 1679616*r8[i] - 60466176*r10[i] - 2176782336*r12[i] )//6 - O1[i])//35 for i in range(L)]

	# layer 2
	O7 = [(O3[i] - O2[i]) // 5 for i in range(L)]
	O8 = [(O4[i] - O3[i]) // 7 for i in range(L)]
	O9 = [(O5[i] - O4[i]) // 9 for i in range(L)]
	O10 = [(O6[i] - O5[i]) // 11 for i in range(L)]

	# layer 3
	O11 = [(O8[i] - O7[i]) // 12 for i in range(L)]
	O12 = [(O9[i] - O8[i]) // 16 for i in range(L)]
	O13 = [(O10[i] - O9[i]) // 20 for i in range(L)]

	# layer 4
	O14 = [(O12[i] - O11[i]) // 21 for i in range(L)]
	O15 = [(O13[i] - O12[i]) // 27 for i in range(L)]

	# the remaining odd variables
	r11 = [(O15[i] - O14[i]) // 32 for i in range(L)]
	r9 = [O14[i] - 55*r11[i]  for i in range(L)]
	r7 = [O11[i] - 30*r9[i] - 627*r11[i]  for i in range(L)]
	r5 = [O7[i] - 14*r7[i] - 147*r9[i] - 1408*r11[i]  for i in range(L)]
	r3 = [O2[i] - 5*r5[i] - 21*r7[i] - 85*r9[i] - 341*r11[i]  for i in range(L)]
	r1 = [O1[i] - r3[i] - r5[i] - r7[i] - r9[i] - r11[i]  for i in range(L)]

	return (r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12)

def efficient_interpolate_8(r):
	r0 = r[0]
	r14 = r['infinity']

	L = len(r0)

	# the even temp variables

	# start with E1, since it's not in a layer
	E1 = [(r[1][i] + r[-1][i])//2 - r0[i] - r14[i] for i in range(L)]

	# layer 1
	E2 = [(((r[2][i] + r[-2][i])//2 - r0[i] - 16384*r14[i])//4 - E1[i])//3 for i in range(L)]
	E3 = [(((r[3][i] + r[-3][i])//2 - r0[i] - 4782969*r14[i])//9 - E1[i])//8 for i in range(L)]
	E4 = [(((r[4][i] + r[-4][i])//2 - r0[i] - 268435456*r14[i])//16 - E1[i])//15 for i in range(L)]
	E5 = [(((r[5][i] + r[-5][i])//2 - r0[i] - 6103515625*r14[i])//25 - E1[i])//24 for i in range(L)]
	E6 = [(((r[6][i] + r[-6][i])//2 - r0[i] - 78364164096*r14[i])//36 - E1[i])//35 for i in range(L)]

	# layer 2
	E7 = [(E3[i] - E2[i]) // 5 for i in range(L)]
	E8 = [(E4[i] - E3[i]) // 7 for i in range(L)]
	E9 = [(E5[i] - E4[i]) // 9 for i in range(L)]
	E10 = [(E6[i] - E5[i]) // 11 for i in range(L)]

	# layer 3
	E11 = [(E8[i] - E7[i]) // 12 for i in range(L)]
	E12 = [(E9[i] - E8[i]) // 16 for i in range(L)]
	E13 = [(E10[i] - E9[i]) // 20 for i in range(L)]

	# layer 4
	E14 = [(E12[i] - E11[i]) // 21 for i in range(L)]
	E15 = [(E13[i] - E12[i]) // 27 for i in range(L)]

	# the remaining even variables
	r12 = [(E15[i] - E14[i]) // 32 for i in range(L)]
	r10 = [E14[i] - 55*r12[i]  for i in range(L)]
	r8 = [E11[i] - 30*r10[i] - 627*r12[i]  for i in range(L)]
	r6 = [E7[i] - 14*r8[i] - 147*r10[i] - 1408*r12[i]  for i in range(L)]
	r4 = [E2[i] - 5*r6[i] - 21*r8[i] - 85*r10[i] - 341*r12[i]  for i in range(L)]
	r2 = [E1[i] - r4[i] - r6[i] - r8[i] - r10[i] - r12[i]  for i in range(L)]

	# the odd temp variables

	# start with O1, since it's not in a layer
	O1 = [(r[1][i] - r[-1][i])//2 for i in range(L)]

	# layer 1
	O2 = [((r[2][i] - r[-2][i])//4 - O1[i])//3 for i in range(L)]
	O3 = [((r[3][i] - r[-3][i])//6 - O1[i])//8 for i in range(L)]
	O4 = [((r[4][i] - r[-4][i])//8 - O1[i])//15 for i in range(L)]
	O5 = [((r[5][i] - r[-5][i])//10 - O1[i])//24 for i in range(L)]
	O6 = [((r[6][i] - r[-6][i])//12 - O1[i])//35 for i in range(L)]
	O7 = [((r[7][i] - r0[i] - 49*r2[i] - 2401*r4[i] - 117649*r6[i] - 5764801*r8[i] - 282475249*r10[i] - 13841287201*r12[i] - 678223072849*r14[i] )//7 - O1[i])//48 for i in range(L)]

	# layer 2
	O8 = [(O3[i] - O2[i]) // 5 for i in range(L)]
	O9 = [(O4[i] - O3[i]) // 7 for i in range(L)]
	O10 = [(O5[i] - O4[i]) // 9 for i in range(L)]
	O11 = [(O6[i] - O5[i]) // 11 for i in range(L)]
	O12 = [(O7[i] - O6[i]) // 13 for i in range(L)]

	# layer 3
	O13 = [(O9[i] - O8[i]) // 12 for i in range(L)]
	O14 = [(O10[i] - O9[i]) // 16 for i in range(L)]
	O15 = [(O11[i] - O10[i]) // 20 for i in range(L)]
	O16 = [(O12[i] - O11[i]) // 24 for i in range(L)]

	# layer 4
	O17 = [(O14[i] - O13[i]) // 21 for i in range(L)]
	O18 = [(O15[i] - O14[i]) // 27 for i in range(L)]
	O19 = [(O16[i] - O15[i]) // 33 for i in range(L)]

	# layer 5
	O20 = [(O18[i] - O17[i]) // 32 for i in range(L)]
	O21 = [(O19[i] - O18[i]) // 40 for i in range(L)]

	# the remaining odd variables
	r13 = [(O21[i] - O20[i]) // 45 for i in range(L)]
	r11 = [O20[i] - 91*r13[i]  for i in range(L)]
	r9 = [O17[i] - 55*r11[i] - 2002*r13[i]  for i in range(L)]
	r7 = [O13[i] - 30*r9[i] - 627*r11[i] - 11440*r13[i]  for i in range(L)]
	r5 = [O8[i] - 14*r7[i] - 147*r9[i] - 1408*r11[i] - 13013*r13[i]  for i in range(L)]
	r3 = [O2[i] - 5*r5[i] - 21*r7[i] - 85*r9[i] - 341*r11[i] - 1365*r13[i]  for i in range(L)]
	r1 = [O1[i] - r3[i] - r5[i] - r7[i] - r9[i] - r11[i] - r13[i]  for i in range(L)]

	return (r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14)

def efficient_interpolate_9(r):
	r0 = r[0]
	r16 = r['infinity']

	L = len(r0)

	# the even temp variables

	# start with E1, since it's not in a layer
	E1 = [(r[1][i] + r[-1][i])//2 - r0[i] - r16[i] for i in range(L)]

	# layer 1
	E2 = [(((r[2][i] + r[-2][i])//2 - r0[i] - 65536*r16[i])//4 - E1[i])//3 for i in range(L)]
	E3 = [(((r[3][i] + r[-3][i])//2 - r0[i] - 43046721*r16[i])//9 - E1[i])//8 for i in range(L)]
	E4 = [(((r[4][i] + r[-4][i])//2 - r0[i] - 4294967296*r16[i])//16 - E1[i])//15 for i in range(L)]
	E5 = [(((r[5][i] + r[-5][i])//2 - r0[i] - 152587890625*r16[i])//25 - E1[i])//24 for i in range(L)]
	E6 = [(((r[6][i] + r[-6][i])//2 - r0[i] - 2821109907456*r16[i])//36 - E1[i])//35 for i in range(L)]
	E7 = [(((r[7][i] + r[-7][i])//2 - r0[i] - 33232930569601*r16[i])//49 - E1[i])//48 for i in range(L)]

	# layer 2
	E8 = [(E3[i] - E2[i]) // 5 for i in range(L)]
	E9 = [(E4[i] - E3[i]) // 7 for i in range(L)]
	E10 = [(E5[i] - E4[i]) // 9 for i in range(L)]
	E11 = [(E6[i] - E5[i]) // 11 for i in range(L)]
	E12 = [(E7[i] - E6[i]) // 13 for i in range(L)]

	# layer 3
	E13 = [(E9[i] - E8[i]) // 12 for i in range(L)]
	E14 = [(E10[i] - E9[i]) // 16 for i in range(L)]
	E15 = [(E11[i] - E10[i]) // 20 for i in range(L)]
	E16 = [(E12[i] - E11[i]) // 24 for i in range(L)]

	# layer 4
	E17 = [(E14[i] - E13[i]) // 21 for i in range(L)]
	E18 = [(E15[i] - E14[i]) // 27 for i in range(L)]
	E19 = [(E16[i] - E15[i]) // 33 for i in range(L)]

	# layer 5
	E20 = [(E18[i] - E17[i]) // 32 for i in range(L)]
	E21 = [(E19[i] - E18[i]) // 40 for i in range(L)]

	# the remaining even variables
	r14 = [(E21[i] - E20[i]) // 45 for i in range(L)]
	r12 = [E20[i] - 91*r14[i]  for i in range(L)]
	r10 = [E17[i] - 55*r12[i] - 2002*r14[i]  for i in range(L)]
	r8 = [E13[i] - 30*r10[i] - 627*r12[i] - 11440*r14[i]  for i in range(L)]
	r6 = [E8[i] - 14*r8[i] - 147*r10[i] - 1408*r12[i] - 13013*r14[i]  for i in range(L)]
	r4 = [E2[i] - 5*r6[i] - 21*r8[i] - 85*r10[i] - 341*r12[i] - 1365*r14[i]  for i in range(L)]
	r2 = [E1[i] - r4[i] - r6[i] - r8[i] - r10[i] - r12[i] - r14[i]  for i in range(L)]

	# the odd temp variables

	# start with O1, since it's not in a layer
	O1 = [(r[1][i] - r[-1][i])//2 for i in range(L)]

	# layer 1
	O2 = [((r[2][i] - r[-2][i])//4 - O1[i])//3 for i in range(L)]
	O3 = [((r[3][i] - r[-3][i])//6 - O1[i])//8 for i in range(L)]
	O4 = [((r[4][i] - r[-4][i])//8 - O1[i])//15 for i in range(L)]
	O5 = [((r[5][i] - r[-5][i])//10 - O1[i])//24 for i in range(L)]
	O6 = [((r[6][i] - r[-6][i])//12 - O1[i])//35 for i in range(L)]
	O7 = [((r[7][i] - r[-7][i])//14 - O1[i])//48 for i in range(L)]
	O8 = [((r[8][i] - r0[i] - 64*r2[i] - 4096*r4[i] - 262144*r6[i] - 16777216*r8[i] - 1073741824*r10[i] - 68719476736*r12[i] - 4398046511104*r14[i] - 281474976710656*r16[i] )//8 - O1[i])//63 for i in range(L)]

	# layer 2
	O9 = [(O3[i] - O2[i]) // 5 for i in range(L)]
	O10 = [(O4[i] - O3[i]) // 7 for i in range(L)]
	O11 = [(O5[i] - O4[i]) // 9 for i in range(L)]
	O12 = [(O6[i] - O5[i]) // 11 for i in range(L)]
	O13 = [(O7[i] - O6[i]) // 13 for i in range(L)]
	O14 = [(O8[i] - O7[i]) // 15 for i in range(L)]

	# layer 3
	O15 = [(O10[i] - O9[i]) // 12 for i in range(L)]
	O16 = [(O11[i] - O10[i]) // 16 for i in range(L)]
	O17 = [(O12[i] - O11[i]) // 20 for i in range(L)]
	O18 = [(O13[i] - O12[i]) // 24 for i in range(L)]
	O19 = [(O14[i] - O13[i]) // 28 for i in range(L)]

	# layer 4
	O20 = [(O16[i] - O15[i]) // 21 for i in range(L)]
	O21 = [(O17[i] - O16[i]) // 27 for i in range(L)]
	O22 = [(O18[i] - O17[i]) // 33 for i in range(L)]
	O23 = [(O19[i] - O18[i]) // 39 for i in range(L)]

	# layer 5
	O24 = [(O21[i] - O20[i]) // 32 for i in range(L)]
	O25 = [(O22[i] - O21[i]) // 40 for i in range(L)]
	O26 = [(O23[i] - O22[i]) // 48 for i in range(L)]

	# layer 6
	O27 = [(O25[i] - O24[i]) // 45 for i in range(L)]
	O28 = [(O26[i] - O25[i]) // 55 for i in range(L)]

	# the remaining odd variables
	r15 = [(O28[i] - O27[i]) // 60 for i in range(L)]
	r13 = [O27[i] - 140*r15[i]  for i in range(L)]
	r11 = [O24[i] - 91*r13[i] - 5278*r15[i]  for i in range(L)]
	r9 = [O20[i] - 55*r11[i] - 2002*r13[i] - 61490*r15[i]  for i in range(L)]
	r7 = [O15[i] - 30*r9[i] - 627*r11[i] - 11440*r13[i] - 196053*r15[i]  for i in range(L)]
	r5 = [O9[i] - 14*r7[i] - 147*r9[i] - 1408*r11[i] - 13013*r13[i] - 118482*r15[i]  for i in range(L)]
	r3 = [O2[i] - 5*r5[i] - 21*r7[i] - 85*r9[i] - 341*r11[i] - 1365*r13[i] - 5461*r15[i]  for i in range(L)]
	r1 = [O1[i] - r3[i] - r5[i] - r7[i] - r9[i] - r11[i] - r13[i] - r15[i]  for i in range(L)]

	return (r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16)

def efficient_interpolate_10(r):
	r0 = r[0]
	r18 = r['infinity']

	L = len(r0)

	# the even temp variables

	# start with E1, since it's not in a layer
	E1 = [(r[1][i] + r[-1][i])//2 - r0[i] - r18[i] for i in range(L)]

	# layer 1
	E2 = [(((r[2][i] + r[-2][i])//2 - r0[i] - 262144*r18[i])//4 - E1[i])//3 for i in range(L)]
	E3 = [(((r[3][i] + r[-3][i])//2 - r0[i] - 387420489*r18[i])//9 - E1[i])//8 for i in range(L)]
	E4 = [(((r[4][i] + r[-4][i])//2 - r0[i] - 68719476736*r18[i])//16 - E1[i])//15 for i in range(L)]
	E5 = [(((r[5][i] + r[-5][i])//2 - r0[i] - 3814697265625*r18[i])//25 - E1[i])//24 for i in range(L)]
	E6 = [(((r[6][i] + r[-6][i])//2 - r0[i] - 101559956668416*r18[i])//36 - E1[i])//35 for i in range(L)]
	E7 = [(((r[7][i] + r[-7][i])//2 - r0[i] - 1628413597910449*r18[i])//49 - E1[i])//48 for i in range(L)]
	E8 = [(((r[8][i] + r[-8][i])//2 - r0[i] - 18014398509481984*r18[i])//64 - E1[i])//63 for i in range(L)]

	# layer 2
	E9 = [(E3[i] - E2[i]) // 5 for i in range(L)]
	E10 = [(E4[i] - E3[i]) // 7 for i in range(L)]
	E11 = [(E5[i] - E4[i]) // 9 for i in range(L)]
	E12 = [(E6[i] - E5[i]) // 11 for i in range(L)]
	E13 = [(E7[i] - E6[i]) // 13 for i in range(L)]
	E14 = [(E8[i] - E7[i]) // 15 for i in range(L)]

	# layer 3
	E15 = [(E10[i] - E9[i]) // 12 for i in range(L)]
	E16 = [(E11[i] - E10[i]) // 16 for i in range(L)]
	E17 = [(E12[i] - E11[i]) // 20 for i in range(L)]
	E18 = [(E13[i] - E12[i]) // 24 for i in range(L)]
	E19 = [(E14[i] - E13[i]) // 28 for i in range(L)]

	# layer 4
	E20 = [(E16[i] - E15[i]) // 21 for i in range(L)]
	E21 = [(E17[i] - E16[i]) // 27 for i in range(L)]
	E22 = [(E18[i] - E17[i]) // 33 for i in range(L)]
	E23 = [(E19[i] - E18[i]) // 39 for i in range(L)]

	# layer 5
	E24 = [(E21[i] - E20[i]) // 32 for i in range(L)]
	E25 = [(E22[i] - E21[i]) // 40 for i in range(L)]
	E26 = [(E23[i] - E22[i]) // 48 for i in range(L)]

	# layer 6
	E27 = [(E25[i] - E24[i]) // 45 for i in range(L)]
	E28 = [(E26[i] - E25[i]) // 55 for i in range(L)]

	# the remaining even variables
	r16 = [(E28[i] - E27[i]) // 60 for i in range(L)]
	r14 = [E27[i] - 140*r16[i]  for i in range(L)]
	r12 = [E24[i] - 91*r14[i] - 5278*r16[i]  for i in range(L)]
	r10 = [E20[i] - 55*r12[i] - 2002*r14[i] - 61490*r16[i]  for i in range(L)]
	r8 = [E15[i] - 30*r10[i] - 627*r12[i] - 11440*r14[i] - 196053*r16[i]  for i in range(L)]
	r6 = [E9[i] - 14*r8[i] - 147*r10[i] - 1408*r12[i] - 13013*r14[i] - 118482*r16[i]  for i in range(L)]
	r4 = [E2[i] - 5*r6[i] - 21*r8[i] - 85*r10[i] - 341*r12[i] - 1365*r14[i] - 5461*r16[i]  for i in range(L)]
	r2 = [E1[i] - r4[i] - r6[i] - r8[i] - r10[i] - r12[i] - r14[i] - r16[i]  for i in range(L)]

	# the odd temp variables

	# start with O1, since it's not in a layer
	O1 = [(r[1][i] - r[-1][i])//2 for i in range(L)]

	# layer 1
	O2 = [((r[2][i] - r[-2][i])//4 - O1[i])//3 for i in range(L)]
	O3 = [((r[3][i] - r[-3][i])//6 - O1[i])//8 for i in range(L)]
	O4 = [((r[4][i] - r[-4][i])//8 - O1[i])//15 for i in range(L)]
	O5 = [((r[5][i] - r[-5][i])//10 - O1[i])//24 for i in range(L)]
	O6 = [((r[6][i] - r[-6][i])//12 - O1[i])//35 for i in range(L)]
	O7 = [((r[7][i] - r[-7][i])//14 - O1[i])//48 for i in range(L)]
	O8 = [((r[8][i] - r[-8][i])//16 - O1[i])//63 for i in range(L)]
	O9 = [((r[9][i] - r0[i] - 81*r2[i] - 6561*r4[i] - 531441*r6[i] - 43046721*r8[i] - 3486784401*r10[i] - 282429536481*r12[i] - 22876792454961*r14[i] - 1853020188851841*r16[i] - 150094635296999121*r18[i] )//9 - O1[i])//80 for i in range(L)]

	# layer 2
	O10 = [(O3[i] - O2[i]) // 5 for i in range(L)]
	O11 = [(O4[i] - O3[i]) // 7 for i in range(L)]
	O12 = [(O5[i] - O4[i]) // 9 for i in range(L)]
	O13 = [(O6[i] - O5[i]) // 11 for i in range(L)]
	O14 = [(O7[i] - O6[i]) // 13 for i in range(L)]
	O15 = [(O8[i] - O7[i]) // 15 for i in range(L)]
	O16 = [(O9[i] - O8[i]) // 17 for i in range(L)]

	# layer 3
	O17 = [(O11[i] - O10[i]) // 12 for i in range(L)]
	O18 = [(O12[i] - O11[i]) // 16 for i in range(L)]
	O19 = [(O13[i] - O12[i]) // 20 for i in range(L)]
	O20 = [(O14[i] - O13[i]) // 24 for i in range(L)]
	O21 = [(O15[i] - O14[i]) // 28 for i in range(L)]
	O22 = [(O16[i] - O15[i]) // 32 for i in range(L)]

	# layer 4
	O23 = [(O18[i] - O17[i]) // 21 for i in range(L)]
	O24 = [(O19[i] - O18[i]) // 27 for i in range(L)]
	O25 = [(O20[i] - O19[i]) // 33 for i in range(L)]
	O26 = [(O21[i] - O20[i]) // 39 for i in range(L)]
	O27 = [(O22[i] - O21[i]) // 45 for i in range(L)]

	# layer 5
	O28 = [(O24[i] - O23[i]) // 32 for i in range(L)]
	O29 = [(O25[i] - O24[i]) // 40 for i in range(L)]
	O30 = [(O26[i] - O25[i]) // 48 for i in range(L)]
	O31 = [(O27[i] - O26[i]) // 56 for i in range(L)]

	# layer 6
	O32 = [(O29[i] - O28[i]) // 45 for i in range(L)]
	O33 = [(O30[i] - O29[i]) // 55 for i in range(L)]
	O34 = [(O31[i] - O30[i]) // 65 for i in range(L)]

	# layer 7
	O35 = [(O33[i] - O32[i]) // 60 for i in range(L)]
	O36 = [(O34[i] - O33[i]) // 72 for i in range(L)]

	# the remaining odd variables
	r17 = [(O36[i] - O35[i]) // 77 for i in range(L)]
	r15 = [O35[i] - 204*r17[i]  for i in range(L)]
	r13 = [O32[i] - 140*r15[i] - 12138*r17[i]  for i in range(L)]
	r11 = [O28[i] - 91*r13[i] - 5278*r15[i] - 251498*r17[i]  for i in range(L)]
	r9 = [O23[i] - 55*r11[i] - 2002*r13[i] - 61490*r15[i] - 1733303*r17[i]  for i in range(L)]
	r7 = [O17[i] - 30*r9[i] - 627*r11[i] - 11440*r13[i] - 196053*r15[i] - 3255330*r17[i]  for i in range(L)]
	r5 = [O10[i] - 14*r7[i] - 147*r9[i] - 1408*r11[i] - 13013*r13[i] - 118482*r15[i] - 1071799*r17[i]  for i in range(L)]
	r3 = [O2[i] - 5*r5[i] - 21*r7[i] - 85*r9[i] - 341*r11[i] - 1365*r13[i] - 5461*r15[i] - 21845*r17[i]  for i in range(L)]
	r1 = [O1[i] - r3[i] - r5[i] - r7[i] - r9[i] - r11[i] - r13[i] - r15[i] - r17[i]  for i in range(L)]

	return (r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18)

def efficient_interpolate_11(r):
	r0 = r[0]
	r20 = r['infinity']

	L = len(r0)

	# the even temp variables

	# start with E1, since it's not in a layer
	E1 = [(r[1][i] + r[-1][i])//2 - r0[i] - r20[i] for i in range(L)]

	# layer 1
	E2 = [(((r[2][i] + r[-2][i])//2 - r0[i] - 1048576*r20[i])//4 - E1[i])//3 for i in range(L)]
	E3 = [(((r[3][i] + r[-3][i])//2 - r0[i] - 3486784401*r20[i])//9 - E1[i])//8 for i in range(L)]
	E4 = [(((r[4][i] + r[-4][i])//2 - r0[i] - 1099511627776*r20[i])//16 - E1[i])//15 for i in range(L)]
	E5 = [(((r[5][i] + r[-5][i])//2 - r0[i] - 95367431640625*r20[i])//25 - E1[i])//24 for i in range(L)]
	E6 = [(((r[6][i] + r[-6][i])//2 - r0[i] - 3656158440062976*r20[i])//36 - E1[i])//35 for i in range(L)]
	E7 = [(((r[7][i] + r[-7][i])//2 - r0[i] - 79792266297612001*r20[i])//49 - E1[i])//48 for i in range(L)]
	E8 = [(((r[8][i] + r[-8][i])//2 - r0[i] - 1152921504606846976*r20[i])//64 - E1[i])//63 for i in range(L)]
	E9 = [(((r[9][i] + r[-9][i])//2 - r0[i] - 12157665459056928801*r20[i])//81 - E1[i])//80 for i in range(L)]

	# layer 2
	E10 = [(E3[i] - E2[i]) // 5 for i in range(L)]
	E11 = [(E4[i] - E3[i]) // 7 for i in range(L)]
	E12 = [(E5[i] - E4[i]) // 9 for i in range(L)]
	E13 = [(E6[i] - E5[i]) // 11 for i in range(L)]
	E14 = [(E7[i] - E6[i]) // 13 for i in range(L)]
	E15 = [(E8[i] - E7[i]) // 15 for i in range(L)]
	E16 = [(E9[i] - E8[i]) // 17 for i in range(L)]

	# layer 3
	E17 = [(E11[i] - E10[i]) // 12 for i in range(L)]
	E18 = [(E12[i] - E11[i]) // 16 for i in range(L)]
	E19 = [(E13[i] - E12[i]) // 20 for i in range(L)]
	E20 = [(E14[i] - E13[i]) // 24 for i in range(L)]
	E21 = [(E15[i] - E14[i]) // 28 for i in range(L)]
	E22 = [(E16[i] - E15[i]) // 32 for i in range(L)]

	# layer 4
	E23 = [(E18[i] - E17[i]) // 21 for i in range(L)]
	E24 = [(E19[i] - E18[i]) // 27 for i in range(L)]
	E25 = [(E20[i] - E19[i]) // 33 for i in range(L)]
	E26 = [(E21[i] - E20[i]) // 39 for i in range(L)]
	E27 = [(E22[i] - E21[i]) // 45 for i in range(L)]

	# layer 5
	E28 = [(E24[i] - E23[i]) // 32 for i in range(L)]
	E29 = [(E25[i] - E24[i]) // 40 for i in range(L)]
	E30 = [(E26[i] - E25[i]) // 48 for i in range(L)]
	E31 = [(E27[i] - E26[i]) // 56 for i in range(L)]

	# layer 6
	E32 = [(E29[i] - E28[i]) // 45 for i in range(L)]
	E33 = [(E30[i] - E29[i]) // 55 for i in range(L)]
	E34 = [(E31[i] - E30[i]) // 65 for i in range(L)]

	# layer 7
	E35 = [(E33[i] - E32[i]) // 60 for i in range(L)]
	E36 = [(E34[i] - E33[i]) // 72 for i in range(L)]

	# the remaining even variables
	r18 = [(E36[i] - E35[i]) // 77 for i in range(L)]
	r16 = [E35[i] - 204*r18[i]  for i in range(L)]
	r14 = [E32[i] - 140*r16[i] - 12138*r18[i]  for i in range(L)]
	r12 = [E28[i] - 91*r14[i] - 5278*r16[i] - 251498*r18[i]  for i in range(L)]
	r10 = [E23[i] - 55*r12[i] - 2002*r14[i] - 61490*r16[i] - 1733303*r18[i]  for i in range(L)]
	r8 = [E17[i] - 30*r10[i] - 627*r12[i] - 11440*r14[i] - 196053*r16[i] - 3255330*r18[i]  for i in range(L)]
	r6 = [E10[i] - 14*r8[i] - 147*r10[i] - 1408*r12[i] - 13013*r14[i] - 118482*r16[i] - 1071799*r18[i]  for i in range(L)]
	r4 = [E2[i] - 5*r6[i] - 21*r8[i] - 85*r10[i] - 341*r12[i] - 1365*r14[i] - 5461*r16[i] - 21845*r18[i]  for i in range(L)]
	r2 = [E1[i] - r4[i] - r6[i] - r8[i] - r10[i] - r12[i] - r14[i] - r16[i] - r18[i]  for i in range(L)]

	# the odd temp variables

	# start with O1, since it's not in a layer
	O1 = [(r[1][i] - r[-1][i])//2 for i in range(L)]

	# layer 1
	O2 = [((r[2][i] - r[-2][i])//4 - O1[i])//3 for i in range(L)]
	O3 = [((r[3][i] - r[-3][i])//6 - O1[i])//8 for i in range(L)]
	O4 = [((r[4][i] - r[-4][i])//8 - O1[i])//15 for i in range(L)]
	O5 = [((r[5][i] - r[-5][i])//10 - O1[i])//24 for i in range(L)]
	O6 = [((r[6][i] - r[-6][i])//12 - O1[i])//35 for i in range(L)]
	O7 = [((r[7][i] - r[-7][i])//14 - O1[i])//48 for i in range(L)]
	O8 = [((r[8][i] - r[-8][i])//16 - O1[i])//63 for i in range(L)]
	O9 = [((r[9][i] - r[-9][i])//18 - O1[i])//80 for i in range(L)]
	O10 = [((r[10][i] - r0[i] - 100*r2[i] - 10000*r4[i] - 1000000*r6[i] - 100000000*r8[i] - 10000000000*r10[i] - 1000000000000*r12[i] - 100000000000000*r14[i] - 10000000000000000*r16[i] - 1000000000000000000*r18[i] - 100000000000000000000*r20[i] )//10 - O1[i])//99 for i in range(L)]

	# layer 2
	O11 = [(O3[i] - O2[i]) // 5 for i in range(L)]
	O12 = [(O4[i] - O3[i]) // 7 for i in range(L)]
	O13 = [(O5[i] - O4[i]) // 9 for i in range(L)]
	O14 = [(O6[i] - O5[i]) // 11 for i in range(L)]
	O15 = [(O7[i] - O6[i]) // 13 for i in range(L)]
	O16 = [(O8[i] - O7[i]) // 15 for i in range(L)]
	O17 = [(O9[i] - O8[i]) // 17 for i in range(L)]
	O18 = [(O10[i] - O9[i]) // 19 for i in range(L)]

	# layer 3
	O19 = [(O12[i] - O11[i]) // 12 for i in range(L)]
	O20 = [(O13[i] - O12[i]) // 16 for i in range(L)]
	O21 = [(O14[i] - O13[i]) // 20 for i in range(L)]
	O22 = [(O15[i] - O14[i]) // 24 for i in range(L)]
	O23 = [(O16[i] - O15[i]) // 28 for i in range(L)]
	O24 = [(O17[i] - O16[i]) // 32 for i in range(L)]
	O25 = [(O18[i] - O17[i]) // 36 for i in range(L)]

	# layer 4
	O26 = [(O20[i] - O19[i]) // 21 for i in range(L)]
	O27 = [(O21[i] - O20[i]) // 27 for i in range(L)]
	O28 = [(O22[i] - O21[i]) // 33 for i in range(L)]
	O29 = [(O23[i] - O22[i]) // 39 for i in range(L)]
	O30 = [(O24[i] - O23[i]) // 45 for i in range(L)]
	O31 = [(O25[i] - O24[i]) // 51 for i in range(L)]

	# layer 5
	O32 = [(O27[i] - O26[i]) // 32 for i in range(L)]
	O33 = [(O28[i] - O27[i]) // 40 for i in range(L)]
	O34 = [(O29[i] - O28[i]) // 48 for i in range(L)]
	O35 = [(O30[i] - O29[i]) // 56 for i in range(L)]
	O36 = [(O31[i] - O30[i]) // 64 for i in range(L)]

	# layer 6
	O37 = [(O33[i] - O32[i]) // 45 for i in range(L)]
	O38 = [(O34[i] - O33[i]) // 55 for i in range(L)]
	O39 = [(O35[i] - O34[i]) // 65 for i in range(L)]
	O40 = [(O36[i] - O35[i]) // 75 for i in range(L)]

	# layer 7
	O41 = [(O38[i] - O37[i]) // 60 for i in range(L)]
	O42 = [(O39[i] - O38[i]) // 72 for i in range(L)]
	O43 = [(O40[i] - O39[i]) // 84 for i in range(L)]

	# layer 8
	O44 = [(O42[i] - O41[i]) // 77 for i in range(L)]
	O45 = [(O43[i] - O42[i]) // 91 for i in range(L)]

	# the remaining odd variables
	r19 = [(O45[i] - O44[i]) // 96 for i in range(L)]
	r17 = [O44[i] - 285*r19[i]  for i in range(L)]
	r15 = [O41[i] - 204*r17[i] - 25194*r19[i]  for i in range(L)]
	r13 = [O37[i] - 140*r15[i] - 12138*r17[i] - 846260*r19[i]  for i in range(L)]
	r11 = [O32[i] - 91*r13[i] - 5278*r15[i] - 251498*r17[i] - 10787231*r19[i]  for i in range(L)]
	r9 = [O26[i] - 55*r11[i] - 2002*r13[i] - 61490*r15[i] - 1733303*r17[i] - 46587905*r19[i]  for i in range(L)]
	r7 = [O19[i] - 30*r9[i] - 627*r11[i] - 11440*r13[i] - 196053*r15[i] - 3255330*r17[i] - 53157079*r19[i]  for i in range(L)]
	r5 = [O11[i] - 14*r7[i] - 147*r9[i] - 1408*r11[i] - 13013*r13[i] - 118482*r15[i] - 1071799*r17[i] - 9668036*r19[i]  for i in range(L)]
	r3 = [O2[i] - 5*r5[i] - 21*r7[i] - 85*r9[i] - 341*r11[i] - 1365*r13[i] - 5461*r15[i] - 21845*r17[i] - 87381*r19[i]  for i in range(L)]
	r1 = [O1[i] - r3[i] - r5[i] - r7[i] - r9[i] - r11[i] - r13[i] - r15[i] - r17[i] - r19[i]  for i in range(L)]

	return (r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20)

def efficient_interpolate_12(r):
	r0 = r[0]
	r22 = r['infinity']

	L = len(r0)

	# the even temp variables

	# start with E1, since it's not in a layer
	E1 = [(r[1][i] + r[-1][i])//2 - r0[i] - r22[i] for i in range(L)]

	# layer 1
	E2 = [(((r[2][i] + r[-2][i])//2 - r0[i] - 4194304*r22[i])//4 - E1[i])//3 for i in range(L)]
	E3 = [(((r[3][i] + r[-3][i])//2 - r0[i] - 31381059609*r22[i])//9 - E1[i])//8 for i in range(L)]
	E4 = [(((r[4][i] + r[-4][i])//2 - r0[i] - 17592186044416*r22[i])//16 - E1[i])//15 for i in range(L)]
	E5 = [(((r[5][i] + r[-5][i])//2 - r0[i] - 2384185791015625*r22[i])//25 - E1[i])//24 for i in range(L)]
	E6 = [(((r[6][i] + r[-6][i])//2 - r0[i] - 131621703842267136*r22[i])//36 - E1[i])//35 for i in range(L)]
	E7 = [(((r[7][i] + r[-7][i])//2 - r0[i] - 3909821048582988049*r22[i])//49 - E1[i])//48 for i in range(L)]
	E8 = [(((r[8][i] + r[-8][i])//2 - r0[i] - 73786976294838206464*r22[i])//64 - E1[i])//63 for i in range(L)]
	E9 = [(((r[9][i] + r[-9][i])//2 - r0[i] - 984770902183611232881*r22[i])//81 - E1[i])//80 for i in range(L)]
	E10 = [(((r[10][i] + r[-10][i])//2 - r0[i] - 10000000000000000000000*r22[i])//100 - E1[i])//99 for i in range(L)]

	# layer 2
	E11 = [(E3[i] - E2[i]) // 5 for i in range(L)]
	E12 = [(E4[i] - E3[i]) // 7 for i in range(L)]
	E13 = [(E5[i] - E4[i]) // 9 for i in range(L)]
	E14 = [(E6[i] - E5[i]) // 11 for i in range(L)]
	E15 = [(E7[i] - E6[i]) // 13 for i in range(L)]
	E16 = [(E8[i] - E7[i]) // 15 for i in range(L)]
	E17 = [(E9[i] - E8[i]) // 17 for i in range(L)]
	E18 = [(E10[i] - E9[i]) // 19 for i in range(L)]

	# layer 3
	E19 = [(E12[i] - E11[i]) // 12 for i in range(L)]
	E20 = [(E13[i] - E12[i]) // 16 for i in range(L)]
	E21 = [(E14[i] - E13[i]) // 20 for i in range(L)]
	E22 = [(E15[i] - E14[i]) // 24 for i in range(L)]
	E23 = [(E16[i] - E15[i]) // 28 for i in range(L)]
	E24 = [(E17[i] - E16[i]) // 32 for i in range(L)]
	E25 = [(E18[i] - E17[i]) // 36 for i in range(L)]

	# layer 4
	E26 = [(E20[i] - E19[i]) // 21 for i in range(L)]
	E27 = [(E21[i] - E20[i]) // 27 for i in range(L)]
	E28 = [(E22[i] - E21[i]) // 33 for i in range(L)]
	E29 = [(E23[i] - E22[i]) // 39 for i in range(L)]
	E30 = [(E24[i] - E23[i]) // 45 for i in range(L)]
	E31 = [(E25[i] - E24[i]) // 51 for i in range(L)]

	# layer 5
	E32 = [(E27[i] - E26[i]) // 32 for i in range(L)]
	E33 = [(E28[i] - E27[i]) // 40 for i in range(L)]
	E34 = [(E29[i] - E28[i]) // 48 for i in range(L)]
	E35 = [(E30[i] - E29[i]) // 56 for i in range(L)]
	E36 = [(E31[i] - E30[i]) // 64 for i in range(L)]

	# layer 6
	E37 = [(E33[i] - E32[i]) // 45 for i in range(L)]
	E38 = [(E34[i] - E33[i]) // 55 for i in range(L)]
	E39 = [(E35[i] - E34[i]) // 65 for i in range(L)]
	E40 = [(E36[i] - E35[i]) // 75 for i in range(L)]

	# layer 7
	E41 = [(E38[i] - E37[i]) // 60 for i in range(L)]
	E42 = [(E39[i] - E38[i]) // 72 for i in range(L)]
	E43 = [(E40[i] - E39[i]) // 84 for i in range(L)]

	# layer 8
	E44 = [(E42[i] - E41[i]) // 77 for i in range(L)]
	E45 = [(E43[i] - E42[i]) // 91 for i in range(L)]

	# the remaining even variables
	r20 = [(E45[i] - E44[i]) // 96 for i in range(L)]
	r18 = [E44[i] - 285*r20[i]  for i in range(L)]
	r16 = [E41[i] - 204*r18[i] - 25194*r20[i]  for i in range(L)]
	r14 = [E37[i] - 140*r16[i] - 12138*r18[i] - 846260*r20[i]  for i in range(L)]
	r12 = [E32[i] - 91*r14[i] - 5278*r16[i] - 251498*r18[i] - 10787231*r20[i]  for i in range(L)]
	r10 = [E26[i] - 55*r12[i] - 2002*r14[i] - 61490*r16[i] - 1733303*r18[i] - 46587905*r20[i]  for i in range(L)]
	r8 = [E19[i] - 30*r10[i] - 627*r12[i] - 11440*r14[i] - 196053*r16[i] - 3255330*r18[i] - 53157079*r20[i]  for i in range(L)]
	r6 = [E11[i] - 14*r8[i] - 147*r10[i] - 1408*r12[i] - 13013*r14[i] - 118482*r16[i] - 1071799*r18[i] - 9668036*r20[i]  for i in range(L)]
	r4 = [E2[i] - 5*r6[i] - 21*r8[i] - 85*r10[i] - 341*r12[i] - 1365*r14[i] - 5461*r16[i] - 21845*r18[i] - 87381*r20[i]  for i in range(L)]
	r2 = [E1[i] - r4[i] - r6[i] - r8[i] - r10[i] - r12[i] - r14[i] - r16[i] - r18[i] - r20[i]  for i in range(L)]

	# the odd temp variables

	# start with O1, since it's not in a layer
	O1 = [(r[1][i] - r[-1][i])//2 for i in range(L)]

	# layer 1
	O2 = [((r[2][i] - r[-2][i])//4 - O1[i])//3 for i in range(L)]
	O3 = [((r[3][i] - r[-3][i])//6 - O1[i])//8 for i in range(L)]
	O4 = [((r[4][i] - r[-4][i])//8 - O1[i])//15 for i in range(L)]
	O5 = [((r[5][i] - r[-5][i])//10 - O1[i])//24 for i in range(L)]
	O6 = [((r[6][i] - r[-6][i])//12 - O1[i])//35 for i in range(L)]
	O7 = [((r[7][i] - r[-7][i])//14 - O1[i])//48 for i in range(L)]
	O8 = [((r[8][i] - r[-8][i])//16 - O1[i])//63 for i in range(L)]
	O9 = [((r[9][i] - r[-9][i])//18 - O1[i])//80 for i in range(L)]
	O10 = [((r[10][i] - r[-10][i])//20 - O1[i])//99 for i in range(L)]
	O11 = [((r[11][i] - r0[i] - 121*r2[i] - 14641*r4[i] - 1771561*r6[i] - 214358881*r8[i] - 25937424601*r10[i] - 3138428376721*r12[i] - 379749833583241*r14[i] - 45949729863572161*r16[i] - 5559917313492231481*r18[i] - 672749994932560009201*r20[i] - 81402749386839761113321*r22[i] )//11 - O1[i])//120 for i in range(L)]

	# layer 2
	O12 = [(O3[i] - O2[i]) // 5 for i in range(L)]
	O13 = [(O4[i] - O3[i]) // 7 for i in range(L)]
	O14 = [(O5[i] - O4[i]) // 9 for i in range(L)]
	O15 = [(O6[i] - O5[i]) // 11 for i in range(L)]
	O16 = [(O7[i] - O6[i]) // 13 for i in range(L)]
	O17 = [(O8[i] - O7[i]) // 15 for i in range(L)]
	O18 = [(O9[i] - O8[i]) // 17 for i in range(L)]
	O19 = [(O10[i] - O9[i]) // 19 for i in range(L)]
	O20 = [(O11[i] - O10[i]) // 21 for i in range(L)]

	# layer 3
	O21 = [(O13[i] - O12[i]) // 12 for i in range(L)]
	O22 = [(O14[i] - O13[i]) // 16 for i in range(L)]
	O23 = [(O15[i] - O14[i]) // 20 for i in range(L)]
	O24 = [(O16[i] - O15[i]) // 24 for i in range(L)]
	O25 = [(O17[i] - O16[i]) // 28 for i in range(L)]
	O26 = [(O18[i] - O17[i]) // 32 for i in range(L)]
	O27 = [(O19[i] - O18[i]) // 36 for i in range(L)]
	O28 = [(O20[i] - O19[i]) // 40 for i in range(L)]

	# layer 4
	O29 = [(O22[i] - O21[i]) // 21 for i in range(L)]
	O30 = [(O23[i] - O22[i]) // 27 for i in range(L)]
	O31 = [(O24[i] - O23[i]) // 33 for i in range(L)]
	O32 = [(O25[i] - O24[i]) // 39 for i in range(L)]
	O33 = [(O26[i] - O25[i]) // 45 for i in range(L)]
	O34 = [(O27[i] - O26[i]) // 51 for i in range(L)]
	O35 = [(O28[i] - O27[i]) // 57 for i in range(L)]

	# layer 5
	O36 = [(O30[i] - O29[i]) // 32 for i in range(L)]
	O37 = [(O31[i] - O30[i]) // 40 for i in range(L)]
	O38 = [(O32[i] - O31[i]) // 48 for i in range(L)]
	O39 = [(O33[i] - O32[i]) // 56 for i in range(L)]
	O40 = [(O34[i] - O33[i]) // 64 for i in range(L)]
	O41 = [(O35[i] - O34[i]) // 72 for i in range(L)]

	# layer 6
	O42 = [(O37[i] - O36[i]) // 45 for i in range(L)]
	O43 = [(O38[i] - O37[i]) // 55 for i in range(L)]
	O44 = [(O39[i] - O38[i]) // 65 for i in range(L)]
	O45 = [(O40[i] - O39[i]) // 75 for i in range(L)]
	O46 = [(O41[i] - O40[i]) // 85 for i in range(L)]

	# layer 7
	O47 = [(O43[i] - O42[i]) // 60 for i in range(L)]
	O48 = [(O44[i] - O43[i]) // 72 for i in range(L)]
	O49 = [(O45[i] - O44[i]) // 84 for i in range(L)]
	O50 = [(O46[i] - O45[i]) // 96 for i in range(L)]

	# layer 8
	O51 = [(O48[i] - O47[i]) // 77 for i in range(L)]
	O52 = [(O49[i] - O48[i]) // 91 for i in range(L)]
	O53 = [(O50[i] - O49[i]) // 105 for i in range(L)]

	# layer 9
	O54 = [(O52[i] - O51[i]) // 96 for i in range(L)]
	O55 = [(O53[i] - O52[i]) // 112 for i in range(L)]

	# the remaining odd variables
	r21 = [(O55[i] - O54[i]) // 117 for i in range(L)]
	r19 = [O54[i] - 385*r21[i]  for i in range(L)]
	r17 = [O51[i] - 285*r19[i] - 48279*r21[i]  for i in range(L)]
	r15 = [O47[i] - 204*r17[i] - 25194*r19[i] - 2458676*r21[i]  for i in range(L)]
	r13 = [O42[i] - 140*r15[i] - 12138*r17[i] - 846260*r19[i] - 52253971*r21[i]  for i in range(L)]
	r11 = [O36[i] - 91*r13[i] - 5278*r15[i] - 251498*r17[i] - 10787231*r19[i] - 434928221*r21[i]  for i in range(L)]
	r9 = [O29[i] - 55*r11[i] - 2002*r13[i] - 61490*r15[i] - 1733303*r17[i] - 46587905*r19[i] - 1217854704*r21[i]  for i in range(L)]
	r7 = [O21[i] - 30*r9[i] - 627*r11[i] - 11440*r13[i] - 196053*r15[i] - 3255330*r17[i] - 53157079*r19[i] - 860181300*r21[i]  for i in range(L)]
	r5 = [O12[i] - 14*r7[i] - 147*r9[i] - 1408*r11[i] - 13013*r13[i] - 118482*r15[i] - 1071799*r17[i] - 9668036*r19[i] - 87099705*r21[i]  for i in range(L)]
	r3 = [O2[i] - 5*r5[i] - 21*r7[i] - 85*r9[i] - 341*r11[i] - 1365*r13[i] - 5461*r15[i] - 21845*r17[i] - 87381*r19[i] - 349525*r21[i]  for i in range(L)]
	r1 = [O1[i] - r3[i] - r5[i] - r7[i] - r9[i] - r11[i] - r13[i] - r15[i] - r17[i] - r19[i] - r21[i]  for i in range(L)]

	return (r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22)

def efficient_interpolate_13(r):
	r0 = r[0]
	r24 = r['infinity']

	L = len(r0)

	# the even temp variables

	# start with E1, since it's not in a layer
	E1 = [(r[1][i] + r[-1][i])//2 - r0[i] - r24[i] for i in range(L)]

	# layer 1
	E2 = [(((r[2][i] + r[-2][i])//2 - r0[i] - 16777216*r24[i])//4 - E1[i])//3 for i in range(L)]
	E3 = [(((r[3][i] + r[-3][i])//2 - r0[i] - 282429536481*r24[i])//9 - E1[i])//8 for i in range(L)]
	E4 = [(((r[4][i] + r[-4][i])//2 - r0[i] - 281474976710656*r24[i])//16 - E1[i])//15 for i in range(L)]
	E5 = [(((r[5][i] + r[-5][i])//2 - r0[i] - 59604644775390625*r24[i])//25 - E1[i])//24 for i in range(L)]
	E6 = [(((r[6][i] + r[-6][i])//2 - r0[i] - 4738381338321616896*r24[i])//36 - E1[i])//35 for i in range(L)]
	E7 = [(((r[7][i] + r[-7][i])//2 - r0[i] - 191581231380566414401*r24[i])//49 - E1[i])//48 for i in range(L)]
	E8 = [(((r[8][i] + r[-8][i])//2 - r0[i] - 4722366482869645213696*r24[i])//64 - E1[i])//63 for i in range(L)]
	E9 = [(((r[9][i] + r[-9][i])//2 - r0[i] - 79766443076872509863361*r24[i])//81 - E1[i])//80 for i in range(L)]
	E10 = [(((r[10][i] + r[-10][i])//2 - r0[i] - 1000000000000000000000000*r24[i])//100 - E1[i])//99 for i in range(L)]
	E11 = [(((r[11][i] + r[-11][i])//2 - r0[i] - 9849732675807611094711841*r24[i])//121 - E1[i])//120 for i in range(L)]

	# layer 2
	E12 = [(E3[i] - E2[i]) // 5 for i in range(L)]
	E13 = [(E4[i] - E3[i]) // 7 for i in range(L)]
	E14 = [(E5[i] - E4[i]) // 9 for i in range(L)]
	E15 = [(E6[i] - E5[i]) // 11 for i in range(L)]
	E16 = [(E7[i] - E6[i]) // 13 for i in range(L)]
	E17 = [(E8[i] - E7[i]) // 15 for i in range(L)]
	E18 = [(E9[i] - E8[i]) // 17 for i in range(L)]
	E19 = [(E10[i] - E9[i]) // 19 for i in range(L)]
	E20 = [(E11[i] - E10[i]) // 21 for i in range(L)]

	# layer 3
	E21 = [(E13[i] - E12[i]) // 12 for i in range(L)]
	E22 = [(E14[i] - E13[i]) // 16 for i in range(L)]
	E23 = [(E15[i] - E14[i]) // 20 for i in range(L)]
	E24 = [(E16[i] - E15[i]) // 24 for i in range(L)]
	E25 = [(E17[i] - E16[i]) // 28 for i in range(L)]
	E26 = [(E18[i] - E17[i]) // 32 for i in range(L)]
	E27 = [(E19[i] - E18[i]) // 36 for i in range(L)]
	E28 = [(E20[i] - E19[i]) // 40 for i in range(L)]

	# layer 4
	E29 = [(E22[i] - E21[i]) // 21 for i in range(L)]
	E30 = [(E23[i] - E22[i]) // 27 for i in range(L)]
	E31 = [(E24[i] - E23[i]) // 33 for i in range(L)]
	E32 = [(E25[i] - E24[i]) // 39 for i in range(L)]
	E33 = [(E26[i] - E25[i]) // 45 for i in range(L)]
	E34 = [(E27[i] - E26[i]) // 51 for i in range(L)]
	E35 = [(E28[i] - E27[i]) // 57 for i in range(L)]

	# layer 5
	E36 = [(E30[i] - E29[i]) // 32 for i in range(L)]
	E37 = [(E31[i] - E30[i]) // 40 for i in range(L)]
	E38 = [(E32[i] - E31[i]) // 48 for i in range(L)]
	E39 = [(E33[i] - E32[i]) // 56 for i in range(L)]
	E40 = [(E34[i] - E33[i]) // 64 for i in range(L)]
	E41 = [(E35[i] - E34[i]) // 72 for i in range(L)]

	# layer 6
	E42 = [(E37[i] - E36[i]) // 45 for i in range(L)]
	E43 = [(E38[i] - E37[i]) // 55 for i in range(L)]
	E44 = [(E39[i] - E38[i]) // 65 for i in range(L)]
	E45 = [(E40[i] - E39[i]) // 75 for i in range(L)]
	E46 = [(E41[i] - E40[i]) // 85 for i in range(L)]

	# layer 7
	E47 = [(E43[i] - E42[i]) // 60 for i in range(L)]
	E48 = [(E44[i] - E43[i]) // 72 for i in range(L)]
	E49 = [(E45[i] - E44[i]) // 84 for i in range(L)]
	E50 = [(E46[i] - E45[i]) // 96 for i in range(L)]

	# layer 8
	E51 = [(E48[i] - E47[i]) // 77 for i in range(L)]
	E52 = [(E49[i] - E48[i]) // 91 for i in range(L)]
	E53 = [(E50[i] - E49[i]) // 105 for i in range(L)]

	# layer 9
	E54 = [(E52[i] - E51[i]) // 96 for i in range(L)]
	E55 = [(E53[i] - E52[i]) // 112 for i in range(L)]

	# the remaining even variables
	r22 = [(E55[i] - E54[i]) // 117 for i in range(L)]
	r20 = [E54[i] - 385*r22[i]  for i in range(L)]
	r18 = [E51[i] - 285*r20[i] - 48279*r22[i]  for i in range(L)]
	r16 = [E47[i] - 204*r18[i] - 25194*r20[i] - 2458676*r22[i]  for i in range(L)]
	r14 = [E42[i] - 140*r16[i] - 12138*r18[i] - 846260*r20[i] - 52253971*r22[i]  for i in range(L)]
	r12 = [E36[i] - 91*r14[i] - 5278*r16[i] - 251498*r18[i] - 10787231*r20[i] - 434928221*r22[i]  for i in range(L)]
	r10 = [E29[i] - 55*r12[i] - 2002*r14[i] - 61490*r16[i] - 1733303*r18[i] - 46587905*r20[i] - 1217854704*r22[i]  for i in range(L)]
	r8 = [E21[i] - 30*r10[i] - 627*r12[i] - 11440*r14[i] - 196053*r16[i] - 3255330*r18[i] - 53157079*r20[i] - 860181300*r22[i]  for i in range(L)]
	r6 = [E12[i] - 14*r8[i] - 147*r10[i] - 1408*r12[i] - 13013*r14[i] - 118482*r16[i] - 1071799*r18[i] - 9668036*r20[i] - 87099705*r22[i]  for i in range(L)]
	r4 = [E2[i] - 5*r6[i] - 21*r8[i] - 85*r10[i] - 341*r12[i] - 1365*r14[i] - 5461*r16[i] - 21845*r18[i] - 87381*r20[i] - 349525*r22[i]  for i in range(L)]
	r2 = [E1[i] - r4[i] - r6[i] - r8[i] - r10[i] - r12[i] - r14[i] - r16[i] - r18[i] - r20[i] - r22[i]  for i in range(L)]

	# the odd temp variables

	# start with O1, since it's not in a layer
	O1 = [(r[1][i] - r[-1][i])//2 for i in range(L)]

	# layer 1
	O2 = [((r[2][i] - r[-2][i])//4 - O1[i])//3 for i in range(L)]
	O3 = [((r[3][i] - r[-3][i])//6 - O1[i])//8 for i in range(L)]
	O4 = [((r[4][i] - r[-4][i])//8 - O1[i])//15 for i in range(L)]
	O5 = [((r[5][i] - r[-5][i])//10 - O1[i])//24 for i in range(L)]
	O6 = [((r[6][i] - r[-6][i])//12 - O1[i])//35 for i in range(L)]
	O7 = [((r[7][i] - r[-7][i])//14 - O1[i])//48 for i in range(L)]
	O8 = [((r[8][i] - r[-8][i])//16 - O1[i])//63 for i in range(L)]
	O9 = [((r[9][i] - r[-9][i])//18 - O1[i])//80 for i in range(L)]
	O10 = [((r[10][i] - r[-10][i])//20 - O1[i])//99 for i in range(L)]
	O11 = [((r[11][i] - r[-11][i])//22 - O1[i])//120 for i in range(L)]
	O12 = [((r[12][i] - r0[i] - 144*r2[i] - 20736*r4[i] - 2985984*r6[i] - 429981696*r8[i] - 61917364224*r10[i] - 8916100448256*r12[i] - 1283918464548864*r14[i] - 184884258895036416*r16[i] - 26623333280885243904*r18[i] - 3833759992447475122176*r20[i] - 552061438912436417593344*r22[i] - 79496847203390844133441536*r24[i] )//12 - O1[i])//143 for i in range(L)]

	# layer 2
	O13 = [(O3[i] - O2[i]) // 5 for i in range(L)]
	O14 = [(O4[i] - O3[i]) // 7 for i in range(L)]
	O15 = [(O5[i] - O4[i]) // 9 for i in range(L)]
	O16 = [(O6[i] - O5[i]) // 11 for i in range(L)]
	O17 = [(O7[i] - O6[i]) // 13 for i in range(L)]
	O18 = [(O8[i] - O7[i]) // 15 for i in range(L)]
	O19 = [(O9[i] - O8[i]) // 17 for i in range(L)]
	O20 = [(O10[i] - O9[i]) // 19 for i in range(L)]
	O21 = [(O11[i] - O10[i]) // 21 for i in range(L)]
	O22 = [(O12[i] - O11[i]) // 23 for i in range(L)]

	# layer 3
	O23 = [(O14[i] - O13[i]) // 12 for i in range(L)]
	O24 = [(O15[i] - O14[i]) // 16 for i in range(L)]
	O25 = [(O16[i] - O15[i]) // 20 for i in range(L)]
	O26 = [(O17[i] - O16[i]) // 24 for i in range(L)]
	O27 = [(O18[i] - O17[i]) // 28 for i in range(L)]
	O28 = [(O19[i] - O18[i]) // 32 for i in range(L)]
	O29 = [(O20[i] - O19[i]) // 36 for i in range(L)]
	O30 = [(O21[i] - O20[i]) // 40 for i in range(L)]
	O31 = [(O22[i] - O21[i]) // 44 for i in range(L)]

	# layer 4
	O32 = [(O24[i] - O23[i]) // 21 for i in range(L)]
	O33 = [(O25[i] - O24[i]) // 27 for i in range(L)]
	O34 = [(O26[i] - O25[i]) // 33 for i in range(L)]
	O35 = [(O27[i] - O26[i]) // 39 for i in range(L)]
	O36 = [(O28[i] - O27[i]) // 45 for i in range(L)]
	O37 = [(O29[i] - O28[i]) // 51 for i in range(L)]
	O38 = [(O30[i] - O29[i]) // 57 for i in range(L)]
	O39 = [(O31[i] - O30[i]) // 63 for i in range(L)]

	# layer 5
	O40 = [(O33[i] - O32[i]) // 32 for i in range(L)]
	O41 = [(O34[i] - O33[i]) // 40 for i in range(L)]
	O42 = [(O35[i] - O34[i]) // 48 for i in range(L)]
	O43 = [(O36[i] - O35[i]) // 56 for i in range(L)]
	O44 = [(O37[i] - O36[i]) // 64 for i in range(L)]
	O45 = [(O38[i] - O37[i]) // 72 for i in range(L)]
	O46 = [(O39[i] - O38[i]) // 80 for i in range(L)]

	# layer 6
	O47 = [(O41[i] - O40[i]) // 45 for i in range(L)]
	O48 = [(O42[i] - O41[i]) // 55 for i in range(L)]
	O49 = [(O43[i] - O42[i]) // 65 for i in range(L)]
	O50 = [(O44[i] - O43[i]) // 75 for i in range(L)]
	O51 = [(O45[i] - O44[i]) // 85 for i in range(L)]
	O52 = [(O46[i] - O45[i]) // 95 for i in range(L)]

	# layer 7
	O53 = [(O48[i] - O47[i]) // 60 for i in range(L)]
	O54 = [(O49[i] - O48[i]) // 72 for i in range(L)]
	O55 = [(O50[i] - O49[i]) // 84 for i in range(L)]
	O56 = [(O51[i] - O50[i]) // 96 for i in range(L)]
	O57 = [(O52[i] - O51[i]) // 108 for i in range(L)]

	# layer 8
	O58 = [(O54[i] - O53[i]) // 77 for i in range(L)]
	O59 = [(O55[i] - O54[i]) // 91 for i in range(L)]
	O60 = [(O56[i] - O55[i]) // 105 for i in range(L)]
	O61 = [(O57[i] - O56[i]) // 119 for i in range(L)]

	# layer 9
	O62 = [(O59[i] - O58[i]) // 96 for i in range(L)]
	O63 = [(O60[i] - O59[i]) // 112 for i in range(L)]
	O64 = [(O61[i] - O60[i]) // 128 for i in range(L)]

	# layer 10
	O65 = [(O63[i] - O62[i]) // 117 for i in range(L)]
	O66 = [(O64[i] - O63[i]) // 135 for i in range(L)]

	# the remaining odd variables
	r23 = [(O66[i] - O65[i]) // 140 for i in range(L)]
	r21 = [O65[i] - 506*r23[i]  for i in range(L)]
	r19 = [O62[i] - 385*r21[i] - 86779*r23[i]  for i in range(L)]
	r17 = [O58[i] - 285*r19[i] - 48279*r21[i] - 6369275*r23[i]  for i in range(L)]
	r15 = [O53[i] - 204*r17[i] - 25194*r19[i] - 2458676*r21[i] - 209609235*r23[i]  for i in range(L)]
	r13 = [O47[i] - 140*r15[i] - 12138*r17[i] - 846260*r19[i] - 52253971*r21[i] - 2995372800*r23[i]  for i in range(L)]
	r11 = [O40[i] - 91*r13[i] - 5278*r15[i] - 251498*r17[i] - 10787231*r19[i] - 434928221*r21[i] - 16875270660*r23[i]  for i in range(L)]
	r9 = [O32[i] - 55*r11[i] - 2002*r13[i] - 61490*r15[i] - 1733303*r17[i] - 46587905*r19[i] - 1217854704*r21[i] - 31306548900*r23[i]  for i in range(L)]
	r7 = [O23[i] - 30*r9[i] - 627*r11[i] - 11440*r13[i] - 196053*r15[i] - 3255330*r17[i] - 53157079*r19[i] - 860181300*r21[i] - 13850000505*r23[i]  for i in range(L)]
	r5 = [O13[i] - 14*r7[i] - 147*r9[i] - 1408*r11[i] - 13013*r13[i] - 118482*r15[i] - 1071799*r17[i] - 9668036*r19[i] - 87099705*r21[i] - 784246870*r23[i]  for i in range(L)]
	r3 = [O2[i] - 5*r5[i] - 21*r7[i] - 85*r9[i] - 341*r11[i] - 1365*r13[i] - 5461*r15[i] - 21845*r17[i] - 87381*r19[i] - 349525*r21[i] - 1398101*r23[i]  for i in range(L)]
	r1 = [O1[i] - r3[i] - r5[i] - r7[i] - r9[i] - r11[i] - r13[i] - r15[i] - r17[i] - r19[i] - r21[i] - r23[i]  for i in range(L)]

	return (r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24)

def efficient_interpolate_14(r):
	r0 = r[0]
	r26 = r['infinity']

	L = len(r0)

	# the even temp variables

	# start with E1, since it's not in a layer
	E1 = [(r[1][i] + r[-1][i])//2 - r0[i] - r26[i] for i in range(L)]

	# layer 1
	E2 = [(((r[2][i] + r[-2][i])//2 - r0[i] - 67108864*r26[i])//4 - E1[i])//3 for i in range(L)]
	E3 = [(((r[3][i] + r[-3][i])//2 - r0[i] - 2541865828329*r26[i])//9 - E1[i])//8 for i in range(L)]
	E4 = [(((r[4][i] + r[-4][i])//2 - r0[i] - 4503599627370496*r26[i])//16 - E1[i])//15 for i in range(L)]
	E5 = [(((r[5][i] + r[-5][i])//2 - r0[i] - 1490116119384765625*r26[i])//25 - E1[i])//24 for i in range(L)]
	E6 = [(((r[6][i] + r[-6][i])//2 - r0[i] - 170581728179578208256*r26[i])//36 - E1[i])//35 for i in range(L)]
	E7 = [(((r[7][i] + r[-7][i])//2 - r0[i] - 9387480337647754305649*r26[i])//49 - E1[i])//48 for i in range(L)]
	E8 = [(((r[8][i] + r[-8][i])//2 - r0[i] - 302231454903657293676544*r26[i])//64 - E1[i])//63 for i in range(L)]
	E9 = [(((r[9][i] + r[-9][i])//2 - r0[i] - 6461081889226673298932241*r26[i])//81 - E1[i])//80 for i in range(L)]
	E10 = [(((r[10][i] + r[-10][i])//2 - r0[i] - 100000000000000000000000000*r26[i])//100 - E1[i])//99 for i in range(L)]
	E11 = [(((r[11][i] + r[-11][i])//2 - r0[i] - 1191817653772720942460132761*r26[i])//121 - E1[i])//120 for i in range(L)]
	E12 = [(((r[12][i] + r[-12][i])//2 - r0[i] - 11447545997288281555215581184*r26[i])//144 - E1[i])//143 for i in range(L)]

	# layer 2
	E13 = [(E3[i] - E2[i]) // 5 for i in range(L)]
	E14 = [(E4[i] - E3[i]) // 7 for i in range(L)]
	E15 = [(E5[i] - E4[i]) // 9 for i in range(L)]
	E16 = [(E6[i] - E5[i]) // 11 for i in range(L)]
	E17 = [(E7[i] - E6[i]) // 13 for i in range(L)]
	E18 = [(E8[i] - E7[i]) // 15 for i in range(L)]
	E19 = [(E9[i] - E8[i]) // 17 for i in range(L)]
	E20 = [(E10[i] - E9[i]) // 19 for i in range(L)]
	E21 = [(E11[i] - E10[i]) // 21 for i in range(L)]
	E22 = [(E12[i] - E11[i]) // 23 for i in range(L)]

	# layer 3
	E23 = [(E14[i] - E13[i]) // 12 for i in range(L)]
	E24 = [(E15[i] - E14[i]) // 16 for i in range(L)]
	E25 = [(E16[i] - E15[i]) // 20 for i in range(L)]
	E26 = [(E17[i] - E16[i]) // 24 for i in range(L)]
	E27 = [(E18[i] - E17[i]) // 28 for i in range(L)]
	E28 = [(E19[i] - E18[i]) // 32 for i in range(L)]
	E29 = [(E20[i] - E19[i]) // 36 for i in range(L)]
	E30 = [(E21[i] - E20[i]) // 40 for i in range(L)]
	E31 = [(E22[i] - E21[i]) // 44 for i in range(L)]

	# layer 4
	E32 = [(E24[i] - E23[i]) // 21 for i in range(L)]
	E33 = [(E25[i] - E24[i]) // 27 for i in range(L)]
	E34 = [(E26[i] - E25[i]) // 33 for i in range(L)]
	E35 = [(E27[i] - E26[i]) // 39 for i in range(L)]
	E36 = [(E28[i] - E27[i]) // 45 for i in range(L)]
	E37 = [(E29[i] - E28[i]) // 51 for i in range(L)]
	E38 = [(E30[i] - E29[i]) // 57 for i in range(L)]
	E39 = [(E31[i] - E30[i]) // 63 for i in range(L)]

	# layer 5
	E40 = [(E33[i] - E32[i]) // 32 for i in range(L)]
	E41 = [(E34[i] - E33[i]) // 40 for i in range(L)]
	E42 = [(E35[i] - E34[i]) // 48 for i in range(L)]
	E43 = [(E36[i] - E35[i]) // 56 for i in range(L)]
	E44 = [(E37[i] - E36[i]) // 64 for i in range(L)]
	E45 = [(E38[i] - E37[i]) // 72 for i in range(L)]
	E46 = [(E39[i] - E38[i]) // 80 for i in range(L)]

	# layer 6
	E47 = [(E41[i] - E40[i]) // 45 for i in range(L)]
	E48 = [(E42[i] - E41[i]) // 55 for i in range(L)]
	E49 = [(E43[i] - E42[i]) // 65 for i in range(L)]
	E50 = [(E44[i] - E43[i]) // 75 for i in range(L)]
	E51 = [(E45[i] - E44[i]) // 85 for i in range(L)]
	E52 = [(E46[i] - E45[i]) // 95 for i in range(L)]

	# layer 7
	E53 = [(E48[i] - E47[i]) // 60 for i in range(L)]
	E54 = [(E49[i] - E48[i]) // 72 for i in range(L)]
	E55 = [(E50[i] - E49[i]) // 84 for i in range(L)]
	E56 = [(E51[i] - E50[i]) // 96 for i in range(L)]
	E57 = [(E52[i] - E51[i]) // 108 for i in range(L)]

	# layer 8
	E58 = [(E54[i] - E53[i]) // 77 for i in range(L)]
	E59 = [(E55[i] - E54[i]) // 91 for i in range(L)]
	E60 = [(E56[i] - E55[i]) // 105 for i in range(L)]
	E61 = [(E57[i] - E56[i]) // 119 for i in range(L)]

	# layer 9
	E62 = [(E59[i] - E58[i]) // 96 for i in range(L)]
	E63 = [(E60[i] - E59[i]) // 112 for i in range(L)]
	E64 = [(E61[i] - E60[i]) // 128 for i in range(L)]

	# layer 10
	E65 = [(E63[i] - E62[i]) // 117 for i in range(L)]
	E66 = [(E64[i] - E63[i]) // 135 for i in range(L)]

	# the remaining even variables
	r24 = [(E66[i] - E65[i]) // 140 for i in range(L)]
	r22 = [E65[i] - 506*r24[i]  for i in range(L)]
	r20 = [E62[i] - 385*r22[i] - 86779*r24[i]  for i in range(L)]
	r18 = [E58[i] - 285*r20[i] - 48279*r22[i] - 6369275*r24[i]  for i in range(L)]
	r16 = [E53[i] - 204*r18[i] - 25194*r20[i] - 2458676*r22[i] - 209609235*r24[i]  for i in range(L)]
	r14 = [E47[i] - 140*r16[i] - 12138*r18[i] - 846260*r20[i] - 52253971*r22[i] - 2995372800*r24[i]  for i in range(L)]
	r12 = [E40[i] - 91*r14[i] - 5278*r16[i] - 251498*r18[i] - 10787231*r20[i] - 434928221*r22[i] - 16875270660*r24[i]  for i in range(L)]
	r10 = [E32[i] - 55*r12[i] - 2002*r14[i] - 61490*r16[i] - 1733303*r18[i] - 46587905*r20[i] - 1217854704*r22[i] - 31306548900*r24[i]  for i in range(L)]
	r8 = [E23[i] - 30*r10[i] - 627*r12[i] - 11440*r14[i] - 196053*r16[i] - 3255330*r18[i] - 53157079*r20[i] - 860181300*r22[i] - 13850000505*r24[i]  for i in range(L)]
	r6 = [E13[i] - 14*r8[i] - 147*r10[i] - 1408*r12[i] - 13013*r14[i] - 118482*r16[i] - 1071799*r18[i] - 9668036*r20[i] - 87099705*r22[i] - 784246870*r24[i]  for i in range(L)]
	r4 = [E2[i] - 5*r6[i] - 21*r8[i] - 85*r10[i] - 341*r12[i] - 1365*r14[i] - 5461*r16[i] - 21845*r18[i] - 87381*r20[i] - 349525*r22[i] - 1398101*r24[i]  for i in range(L)]
	r2 = [E1[i] - r4[i] - r6[i] - r8[i] - r10[i] - r12[i] - r14[i] - r16[i] - r18[i] - r20[i] - r22[i] - r24[i]  for i in range(L)]

	# the odd temp variables

	# start with O1, since it's not in a layer
	O1 = [(r[1][i] - r[-1][i])//2 for i in range(L)]

	# layer 1
	O2 = [((r[2][i] - r[-2][i])//4 - O1[i])//3 for i in range(L)]
	O3 = [((r[3][i] - r[-3][i])//6 - O1[i])//8 for i in range(L)]
	O4 = [((r[4][i] - r[-4][i])//8 - O1[i])//15 for i in range(L)]
	O5 = [((r[5][i] - r[-5][i])//10 - O1[i])//24 for i in range(L)]
	O6 = [((r[6][i] - r[-6][i])//12 - O1[i])//35 for i in range(L)]
	O7 = [((r[7][i] - r[-7][i])//14 - O1[i])//48 for i in range(L)]
	O8 = [((r[8][i] - r[-8][i])//16 - O1[i])//63 for i in range(L)]
	O9 = [((r[9][i] - r[-9][i])//18 - O1[i])//80 for i in range(L)]
	O10 = [((r[10][i] - r[-10][i])//20 - O1[i])//99 for i in range(L)]
	O11 = [((r[11][i] - r[-11][i])//22 - O1[i])//120 for i in range(L)]
	O12 = [((r[12][i] - r[-12][i])//24 - O1[i])//143 for i in range(L)]
	O13 = [((r[13][i] - r0[i] - 169*r2[i] - 28561*r4[i] - 4826809*r6[i] - 815730721*r8[i] - 137858491849*r10[i] - 23298085122481*r12[i] - 3937376385699289*r14[i] - 665416609183179841*r16[i] - 112455406951957393129*r18[i] - 19004963774880799438801*r20[i] - 3211838877954855105157369*r22[i] - 542800770374370512771595361*r24[i] - 91733330193268616658399616009*r26[i] )//13 - O1[i])//168 for i in range(L)]

	# layer 2
	O14 = [(O3[i] - O2[i]) // 5 for i in range(L)]
	O15 = [(O4[i] - O3[i]) // 7 for i in range(L)]
	O16 = [(O5[i] - O4[i]) // 9 for i in range(L)]
	O17 = [(O6[i] - O5[i]) // 11 for i in range(L)]
	O18 = [(O7[i] - O6[i]) // 13 for i in range(L)]
	O19 = [(O8[i] - O7[i]) // 15 for i in range(L)]
	O20 = [(O9[i] - O8[i]) // 17 for i in range(L)]
	O21 = [(O10[i] - O9[i]) // 19 for i in range(L)]
	O22 = [(O11[i] - O10[i]) // 21 for i in range(L)]
	O23 = [(O12[i] - O11[i]) // 23 for i in range(L)]
	O24 = [(O13[i] - O12[i]) // 25 for i in range(L)]

	# layer 3
	O25 = [(O15[i] - O14[i]) // 12 for i in range(L)]
	O26 = [(O16[i] - O15[i]) // 16 for i in range(L)]
	O27 = [(O17[i] - O16[i]) // 20 for i in range(L)]
	O28 = [(O18[i] - O17[i]) // 24 for i in range(L)]
	O29 = [(O19[i] - O18[i]) // 28 for i in range(L)]
	O30 = [(O20[i] - O19[i]) // 32 for i in range(L)]
	O31 = [(O21[i] - O20[i]) // 36 for i in range(L)]
	O32 = [(O22[i] - O21[i]) // 40 for i in range(L)]
	O33 = [(O23[i] - O22[i]) // 44 for i in range(L)]
	O34 = [(O24[i] - O23[i]) // 48 for i in range(L)]

	# layer 4
	O35 = [(O26[i] - O25[i]) // 21 for i in range(L)]
	O36 = [(O27[i] - O26[i]) // 27 for i in range(L)]
	O37 = [(O28[i] - O27[i]) // 33 for i in range(L)]
	O38 = [(O29[i] - O28[i]) // 39 for i in range(L)]
	O39 = [(O30[i] - O29[i]) // 45 for i in range(L)]
	O40 = [(O31[i] - O30[i]) // 51 for i in range(L)]
	O41 = [(O32[i] - O31[i]) // 57 for i in range(L)]
	O42 = [(O33[i] - O32[i]) // 63 for i in range(L)]
	O43 = [(O34[i] - O33[i]) // 69 for i in range(L)]

	# layer 5
	O44 = [(O36[i] - O35[i]) // 32 for i in range(L)]
	O45 = [(O37[i] - O36[i]) // 40 for i in range(L)]
	O46 = [(O38[i] - O37[i]) // 48 for i in range(L)]
	O47 = [(O39[i] - O38[i]) // 56 for i in range(L)]
	O48 = [(O40[i] - O39[i]) // 64 for i in range(L)]
	O49 = [(O41[i] - O40[i]) // 72 for i in range(L)]
	O50 = [(O42[i] - O41[i]) // 80 for i in range(L)]
	O51 = [(O43[i] - O42[i]) // 88 for i in range(L)]

	# layer 6
	O52 = [(O45[i] - O44[i]) // 45 for i in range(L)]
	O53 = [(O46[i] - O45[i]) // 55 for i in range(L)]
	O54 = [(O47[i] - O46[i]) // 65 for i in range(L)]
	O55 = [(O48[i] - O47[i]) // 75 for i in range(L)]
	O56 = [(O49[i] - O48[i]) // 85 for i in range(L)]
	O57 = [(O50[i] - O49[i]) // 95 for i in range(L)]
	O58 = [(O51[i] - O50[i]) // 105 for i in range(L)]

	# layer 7
	O59 = [(O53[i] - O52[i]) // 60 for i in range(L)]
	O60 = [(O54[i] - O53[i]) // 72 for i in range(L)]
	O61 = [(O55[i] - O54[i]) // 84 for i in range(L)]
	O62 = [(O56[i] - O55[i]) // 96 for i in range(L)]
	O63 = [(O57[i] - O56[i]) // 108 for i in range(L)]
	O64 = [(O58[i] - O57[i]) // 120 for i in range(L)]

	# layer 8
	O65 = [(O60[i] - O59[i]) // 77 for i in range(L)]
	O66 = [(O61[i] - O60[i]) // 91 for i in range(L)]
	O67 = [(O62[i] - O61[i]) // 105 for i in range(L)]
	O68 = [(O63[i] - O62[i]) // 119 for i in range(L)]
	O69 = [(O64[i] - O63[i]) // 133 for i in range(L)]

	# layer 9
	O70 = [(O66[i] - O65[i]) // 96 for i in range(L)]
	O71 = [(O67[i] - O66[i]) // 112 for i in range(L)]
	O72 = [(O68[i] - O67[i]) // 128 for i in range(L)]
	O73 = [(O69[i] - O68[i]) // 144 for i in range(L)]

	# layer 10
	O74 = [(O71[i] - O70[i]) // 117 for i in range(L)]
	O75 = [(O72[i] - O71[i]) // 135 for i in range(L)]
	O76 = [(O73[i] - O72[i]) // 153 for i in range(L)]

	# layer 11
	O77 = [(O75[i] - O74[i]) // 140 for i in range(L)]
	O78 = [(O76[i] - O75[i]) // 160 for i in range(L)]

	# the remaining odd variables
	r25 = [(O78[i] - O77[i]) // 165 for i in range(L)]
	r23 = [O77[i] - 650*r25[i]  for i in range(L)]
	r21 = [O74[i] - 506*r23[i] - 148005*r25[i]  for i in range(L)]
	r19 = [O70[i] - 385*r21[i] - 86779*r23[i] - 15047175*r25[i]  for i in range(L)]
	r17 = [O65[i] - 285*r19[i] - 48279*r21[i] - 6369275*r23[i] - 725520510*r25[i]  for i in range(L)]
	r15 = [O59[i] - 204*r17[i] - 25194*r19[i] - 2458676*r21[i] - 209609235*r23[i] - 16410363840*r25[i]  for i in range(L)]
	r13 = [O52[i] - 140*r15[i] - 12138*r17[i] - 846260*r19[i] - 52253971*r21[i] - 2995372800*r23[i] - 163648537860*r25[i]  for i in range(L)]
	r11 = [O44[i] - 91*r13[i] - 5278*r15[i] - 251498*r17[i] - 10787231*r19[i] - 434928221*r21[i] - 16875270660*r23[i] - 638816292660*r25[i]  for i in range(L)]
	r9 = [O35[i] - 55*r11[i] - 2002*r13[i] - 61490*r15[i] - 1733303*r17[i] - 46587905*r19[i] - 1217854704*r21[i] - 31306548900*r23[i] - 796513723005*r25[i]  for i in range(L)]
	r7 = [O25[i] - 30*r9[i] - 627*r11[i] - 11440*r13[i] - 196053*r15[i] - 3255330*r17[i] - 53157079*r19[i] - 860181300*r21[i] - 13850000505*r23[i] - 222384254950*r25[i]  for i in range(L)]
	r5 = [O14[i] - 14*r7[i] - 147*r9[i] - 1408*r11[i] - 13013*r13[i] - 118482*r15[i] - 1071799*r17[i] - 9668036*r19[i] - 87099705*r21[i] - 784246870*r23[i] - 7059619931*r25[i]  for i in range(L)]
	r3 = [O2[i] - 5*r5[i] - 21*r7[i] - 85*r9[i] - 341*r11[i] - 1365*r13[i] - 5461*r15[i] - 21845*r17[i] - 87381*r19[i] - 349525*r21[i] - 1398101*r23[i] - 5592405*r25[i]  for i in range(L)]
	r1 = [O1[i] - r3[i] - r5[i] - r7[i] - r9[i] - r11[i] - r13[i] - r15[i] - r17[i] - r19[i] - r21[i] - r23[i] - r25[i]  for i in range(L)]

	return (r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, r26)

def efficient_interpolate_15(r):
	r0 = r[0]
	r28 = r['infinity']

	L = len(r0)

	# the even temp variables

	# start with E1, since it's not in a layer
	E1 = [(r[1][i] + r[-1][i])//2 - r0[i] - r28[i] for i in range(L)]

	# layer 1
	E2 = [(((r[2][i] + r[-2][i])//2 - r0[i] - 268435456*r28[i])//4 - E1[i])//3 for i in range(L)]
	E3 = [(((r[3][i] + r[-3][i])//2 - r0[i] - 22876792454961*r28[i])//9 - E1[i])//8 for i in range(L)]
	E4 = [(((r[4][i] + r[-4][i])//2 - r0[i] - 72057594037927936*r28[i])//16 - E1[i])//15 for i in range(L)]
	E5 = [(((r[5][i] + r[-5][i])//2 - r0[i] - 37252902984619140625*r28[i])//25 - E1[i])//24 for i in range(L)]
	E6 = [(((r[6][i] + r[-6][i])//2 - r0[i] - 6140942214464815497216*r28[i])//36 - E1[i])//35 for i in range(L)]
	E7 = [(((r[7][i] + r[-7][i])//2 - r0[i] - 459986536544739960976801*r28[i])//49 - E1[i])//48 for i in range(L)]
	E8 = [(((r[8][i] + r[-8][i])//2 - r0[i] - 19342813113834066795298816*r28[i])//64 - E1[i])//63 for i in range(L)]
	E9 = [(((r[9][i] + r[-9][i])//2 - r0[i] - 523347633027360537213511521*r28[i])//81 - E1[i])//80 for i in range(L)]
	E10 = [(((r[10][i] + r[-10][i])//2 - r0[i] - 10000000000000000000000000000*r28[i])//100 - E1[i])//99 for i in range(L)]
	E11 = [(((r[11][i] + r[-11][i])//2 - r0[i] - 144209936106499234037676064081*r28[i])//121 - E1[i])//120 for i in range(L)]
	E12 = [(((r[12][i] + r[-12][i])//2 - r0[i] - 1648446623609512543951043690496*r28[i])//144 - E1[i])//143 for i in range(L)]
	E13 = [(((r[13][i] + r[-13][i])//2 - r0[i] - 15502932802662396215269535105521*r28[i])//169 - E1[i])//168 for i in range(L)]

	# layer 2
	E14 = [(E3[i] - E2[i]) // 5 for i in range(L)]
	E15 = [(E4[i] - E3[i]) // 7 for i in range(L)]
	E16 = [(E5[i] - E4[i]) // 9 for i in range(L)]
	E17 = [(E6[i] - E5[i]) // 11 for i in range(L)]
	E18 = [(E7[i] - E6[i]) // 13 for i in range(L)]
	E19 = [(E8[i] - E7[i]) // 15 for i in range(L)]
	E20 = [(E9[i] - E8[i]) // 17 for i in range(L)]
	E21 = [(E10[i] - E9[i]) // 19 for i in range(L)]
	E22 = [(E11[i] - E10[i]) // 21 for i in range(L)]
	E23 = [(E12[i] - E11[i]) // 23 for i in range(L)]
	E24 = [(E13[i] - E12[i]) // 25 for i in range(L)]

	# layer 3
	E25 = [(E15[i] - E14[i]) // 12 for i in range(L)]
	E26 = [(E16[i] - E15[i]) // 16 for i in range(L)]
	E27 = [(E17[i] - E16[i]) // 20 for i in range(L)]
	E28 = [(E18[i] - E17[i]) // 24 for i in range(L)]
	E29 = [(E19[i] - E18[i]) // 28 for i in range(L)]
	E30 = [(E20[i] - E19[i]) // 32 for i in range(L)]
	E31 = [(E21[i] - E20[i]) // 36 for i in range(L)]
	E32 = [(E22[i] - E21[i]) // 40 for i in range(L)]
	E33 = [(E23[i] - E22[i]) // 44 for i in range(L)]
	E34 = [(E24[i] - E23[i]) // 48 for i in range(L)]

	# layer 4
	E35 = [(E26[i] - E25[i]) // 21 for i in range(L)]
	E36 = [(E27[i] - E26[i]) // 27 for i in range(L)]
	E37 = [(E28[i] - E27[i]) // 33 for i in range(L)]
	E38 = [(E29[i] - E28[i]) // 39 for i in range(L)]
	E39 = [(E30[i] - E29[i]) // 45 for i in range(L)]
	E40 = [(E31[i] - E30[i]) // 51 for i in range(L)]
	E41 = [(E32[i] - E31[i]) // 57 for i in range(L)]
	E42 = [(E33[i] - E32[i]) // 63 for i in range(L)]
	E43 = [(E34[i] - E33[i]) // 69 for i in range(L)]

	# layer 5
	E44 = [(E36[i] - E35[i]) // 32 for i in range(L)]
	E45 = [(E37[i] - E36[i]) // 40 for i in range(L)]
	E46 = [(E38[i] - E37[i]) // 48 for i in range(L)]
	E47 = [(E39[i] - E38[i]) // 56 for i in range(L)]
	E48 = [(E40[i] - E39[i]) // 64 for i in range(L)]
	E49 = [(E41[i] - E40[i]) // 72 for i in range(L)]
	E50 = [(E42[i] - E41[i]) // 80 for i in range(L)]
	E51 = [(E43[i] - E42[i]) // 88 for i in range(L)]

	# layer 6
	E52 = [(E45[i] - E44[i]) // 45 for i in range(L)]
	E53 = [(E46[i] - E45[i]) // 55 for i in range(L)]
	E54 = [(E47[i] - E46[i]) // 65 for i in range(L)]
	E55 = [(E48[i] - E47[i]) // 75 for i in range(L)]
	E56 = [(E49[i] - E48[i]) // 85 for i in range(L)]
	E57 = [(E50[i] - E49[i]) // 95 for i in range(L)]
	E58 = [(E51[i] - E50[i]) // 105 for i in range(L)]

	# layer 7
	E59 = [(E53[i] - E52[i]) // 60 for i in range(L)]
	E60 = [(E54[i] - E53[i]) // 72 for i in range(L)]
	E61 = [(E55[i] - E54[i]) // 84 for i in range(L)]
	E62 = [(E56[i] - E55[i]) // 96 for i in range(L)]
	E63 = [(E57[i] - E56[i]) // 108 for i in range(L)]
	E64 = [(E58[i] - E57[i]) // 120 for i in range(L)]

	# layer 8
	E65 = [(E60[i] - E59[i]) // 77 for i in range(L)]
	E66 = [(E61[i] - E60[i]) // 91 for i in range(L)]
	E67 = [(E62[i] - E61[i]) // 105 for i in range(L)]
	E68 = [(E63[i] - E62[i]) // 119 for i in range(L)]
	E69 = [(E64[i] - E63[i]) // 133 for i in range(L)]

	# layer 9
	E70 = [(E66[i] - E65[i]) // 96 for i in range(L)]
	E71 = [(E67[i] - E66[i]) // 112 for i in range(L)]
	E72 = [(E68[i] - E67[i]) // 128 for i in range(L)]
	E73 = [(E69[i] - E68[i]) // 144 for i in range(L)]

	# layer 10
	E74 = [(E71[i] - E70[i]) // 117 for i in range(L)]
	E75 = [(E72[i] - E71[i]) // 135 for i in range(L)]
	E76 = [(E73[i] - E72[i]) // 153 for i in range(L)]

	# layer 11
	E77 = [(E75[i] - E74[i]) // 140 for i in range(L)]
	E78 = [(E76[i] - E75[i]) // 160 for i in range(L)]

	# the remaining even variables
	r26 = [(E78[i] - E77[i]) // 165 for i in range(L)]
	r24 = [E77[i] - 650*r26[i]  for i in range(L)]
	r22 = [E74[i] - 506*r24[i] - 148005*r26[i]  for i in range(L)]
	r20 = [E70[i] - 385*r22[i] - 86779*r24[i] - 15047175*r26[i]  for i in range(L)]
	r18 = [E65[i] - 285*r20[i] - 48279*r22[i] - 6369275*r24[i] - 725520510*r26[i]  for i in range(L)]
	r16 = [E59[i] - 204*r18[i] - 25194*r20[i] - 2458676*r22[i] - 209609235*r24[i] - 16410363840*r26[i]  for i in range(L)]
	r14 = [E52[i] - 140*r16[i] - 12138*r18[i] - 846260*r20[i] - 52253971*r22[i] - 2995372800*r24[i] - 163648537860*r26[i]  for i in range(L)]
	r12 = [E44[i] - 91*r14[i] - 5278*r16[i] - 251498*r18[i] - 10787231*r20[i] - 434928221*r22[i] - 16875270660*r24[i] - 638816292660*r26[i]  for i in range(L)]
	r10 = [E35[i] - 55*r12[i] - 2002*r14[i] - 61490*r16[i] - 1733303*r18[i] - 46587905*r20[i] - 1217854704*r22[i] - 31306548900*r24[i] - 796513723005*r26[i]  for i in range(L)]
	r8 = [E25[i] - 30*r10[i] - 627*r12[i] - 11440*r14[i] - 196053*r16[i] - 3255330*r18[i] - 53157079*r20[i] - 860181300*r22[i] - 13850000505*r24[i] - 222384254950*r26[i]  for i in range(L)]
	r6 = [E14[i] - 14*r8[i] - 147*r10[i] - 1408*r12[i] - 13013*r14[i] - 118482*r16[i] - 1071799*r18[i] - 9668036*r20[i] - 87099705*r22[i] - 784246870*r24[i] - 7059619931*r26[i]  for i in range(L)]
	r4 = [E2[i] - 5*r6[i] - 21*r8[i] - 85*r10[i] - 341*r12[i] - 1365*r14[i] - 5461*r16[i] - 21845*r18[i] - 87381*r20[i] - 349525*r22[i] - 1398101*r24[i] - 5592405*r26[i]  for i in range(L)]
	r2 = [E1[i] - r4[i] - r6[i] - r8[i] - r10[i] - r12[i] - r14[i] - r16[i] - r18[i] - r20[i] - r22[i] - r24[i] - r26[i]  for i in range(L)]

	# the odd temp variables

	# start with O1, since it's not in a layer
	O1 = [(r[1][i] - r[-1][i])//2 for i in range(L)]

	# layer 1
	O2 = [((r[2][i] - r[-2][i])//4 - O1[i])//3 for i in range(L)]
	O3 = [((r[3][i] - r[-3][i])//6 - O1[i])//8 for i in range(L)]
	O4 = [((r[4][i] - r[-4][i])//8 - O1[i])//15 for i in range(L)]
	O5 = [((r[5][i] - r[-5][i])//10 - O1[i])//24 for i in range(L)]
	O6 = [((r[6][i] - r[-6][i])//12 - O1[i])//35 for i in range(L)]
	O7 = [((r[7][i] - r[-7][i])//14 - O1[i])//48 for i in range(L)]
	O8 = [((r[8][i] - r[-8][i])//16 - O1[i])//63 for i in range(L)]
	O9 = [((r[9][i] - r[-9][i])//18 - O1[i])//80 for i in range(L)]
	O10 = [((r[10][i] - r[-10][i])//20 - O1[i])//99 for i in range(L)]
	O11 = [((r[11][i] - r[-11][i])//22 - O1[i])//120 for i in range(L)]
	O12 = [((r[12][i] - r[-12][i])//24 - O1[i])//143 for i in range(L)]
	O13 = [((r[13][i] - r[-13][i])//26 - O1[i])//168 for i in range(L)]
	O14 = [((r[14][i] - r0[i] - 196*r2[i] - 38416*r4[i] - 7529536*r6[i] - 1475789056*r8[i] - 289254654976*r10[i] - 56693912375296*r12[i] - 11112006825558016*r14[i] - 2177953337809371136*r16[i] - 426878854210636742656*r18[i] - 83668255425284801560576*r20[i] - 16398978063355821105872896*r22[i] - 3214199700417740936751087616*r24[i] - 629983141281877223603213172736*r26[i] - 123476695691247935826229781856256*r28[i] )//14 - O1[i])//195 for i in range(L)]

	# layer 2
	O15 = [(O3[i] - O2[i]) // 5 for i in range(L)]
	O16 = [(O4[i] - O3[i]) // 7 for i in range(L)]
	O17 = [(O5[i] - O4[i]) // 9 for i in range(L)]
	O18 = [(O6[i] - O5[i]) // 11 for i in range(L)]
	O19 = [(O7[i] - O6[i]) // 13 for i in range(L)]
	O20 = [(O8[i] - O7[i]) // 15 for i in range(L)]
	O21 = [(O9[i] - O8[i]) // 17 for i in range(L)]
	O22 = [(O10[i] - O9[i]) // 19 for i in range(L)]
	O23 = [(O11[i] - O10[i]) // 21 for i in range(L)]
	O24 = [(O12[i] - O11[i]) // 23 for i in range(L)]
	O25 = [(O13[i] - O12[i]) // 25 for i in range(L)]
	O26 = [(O14[i] - O13[i]) // 27 for i in range(L)]

	# layer 3
	O27 = [(O16[i] - O15[i]) // 12 for i in range(L)]
	O28 = [(O17[i] - O16[i]) // 16 for i in range(L)]
	O29 = [(O18[i] - O17[i]) // 20 for i in range(L)]
	O30 = [(O19[i] - O18[i]) // 24 for i in range(L)]
	O31 = [(O20[i] - O19[i]) // 28 for i in range(L)]
	O32 = [(O21[i] - O20[i]) // 32 for i in range(L)]
	O33 = [(O22[i] - O21[i]) // 36 for i in range(L)]
	O34 = [(O23[i] - O22[i]) // 40 for i in range(L)]
	O35 = [(O24[i] - O23[i]) // 44 for i in range(L)]
	O36 = [(O25[i] - O24[i]) // 48 for i in range(L)]
	O37 = [(O26[i] - O25[i]) // 52 for i in range(L)]

	# layer 4
	O38 = [(O28[i] - O27[i]) // 21 for i in range(L)]
	O39 = [(O29[i] - O28[i]) // 27 for i in range(L)]
	O40 = [(O30[i] - O29[i]) // 33 for i in range(L)]
	O41 = [(O31[i] - O30[i]) // 39 for i in range(L)]
	O42 = [(O32[i] - O31[i]) // 45 for i in range(L)]
	O43 = [(O33[i] - O32[i]) // 51 for i in range(L)]
	O44 = [(O34[i] - O33[i]) // 57 for i in range(L)]
	O45 = [(O35[i] - O34[i]) // 63 for i in range(L)]
	O46 = [(O36[i] - O35[i]) // 69 for i in range(L)]
	O47 = [(O37[i] - O36[i]) // 75 for i in range(L)]

	# layer 5
	O48 = [(O39[i] - O38[i]) // 32 for i in range(L)]
	O49 = [(O40[i] - O39[i]) // 40 for i in range(L)]
	O50 = [(O41[i] - O40[i]) // 48 for i in range(L)]
	O51 = [(O42[i] - O41[i]) // 56 for i in range(L)]
	O52 = [(O43[i] - O42[i]) // 64 for i in range(L)]
	O53 = [(O44[i] - O43[i]) // 72 for i in range(L)]
	O54 = [(O45[i] - O44[i]) // 80 for i in range(L)]
	O55 = [(O46[i] - O45[i]) // 88 for i in range(L)]
	O56 = [(O47[i] - O46[i]) // 96 for i in range(L)]

	# layer 6
	O57 = [(O49[i] - O48[i]) // 45 for i in range(L)]
	O58 = [(O50[i] - O49[i]) // 55 for i in range(L)]
	O59 = [(O51[i] - O50[i]) // 65 for i in range(L)]
	O60 = [(O52[i] - O51[i]) // 75 for i in range(L)]
	O61 = [(O53[i] - O52[i]) // 85 for i in range(L)]
	O62 = [(O54[i] - O53[i]) // 95 for i in range(L)]
	O63 = [(O55[i] - O54[i]) // 105 for i in range(L)]
	O64 = [(O56[i] - O55[i]) // 115 for i in range(L)]

	# layer 7
	O65 = [(O58[i] - O57[i]) // 60 for i in range(L)]
	O66 = [(O59[i] - O58[i]) // 72 for i in range(L)]
	O67 = [(O60[i] - O59[i]) // 84 for i in range(L)]
	O68 = [(O61[i] - O60[i]) // 96 for i in range(L)]
	O69 = [(O62[i] - O61[i]) // 108 for i in range(L)]
	O70 = [(O63[i] - O62[i]) // 120 for i in range(L)]
	O71 = [(O64[i] - O63[i]) // 132 for i in range(L)]

	# layer 8
	O72 = [(O66[i] - O65[i]) // 77 for i in range(L)]
	O73 = [(O67[i] - O66[i]) // 91 for i in range(L)]
	O74 = [(O68[i] - O67[i]) // 105 for i in range(L)]
	O75 = [(O69[i] - O68[i]) // 119 for i in range(L)]
	O76 = [(O70[i] - O69[i]) // 133 for i in range(L)]
	O77 = [(O71[i] - O70[i]) // 147 for i in range(L)]

	# layer 9
	O78 = [(O73[i] - O72[i]) // 96 for i in range(L)]
	O79 = [(O74[i] - O73[i]) // 112 for i in range(L)]
	O80 = [(O75[i] - O74[i]) // 128 for i in range(L)]
	O81 = [(O76[i] - O75[i]) // 144 for i in range(L)]
	O82 = [(O77[i] - O76[i]) // 160 for i in range(L)]

	# layer 10
	O83 = [(O79[i] - O78[i]) // 117 for i in range(L)]
	O84 = [(O80[i] - O79[i]) // 135 for i in range(L)]
	O85 = [(O81[i] - O80[i]) // 153 for i in range(L)]
	O86 = [(O82[i] - O81[i]) // 171 for i in range(L)]

	# layer 11
	O87 = [(O84[i] - O83[i]) // 140 for i in range(L)]
	O88 = [(O85[i] - O84[i]) // 160 for i in range(L)]
	O89 = [(O86[i] - O85[i]) // 180 for i in range(L)]

	# layer 12
	O90 = [(O88[i] - O87[i]) // 165 for i in range(L)]
	O91 = [(O89[i] - O88[i]) // 187 for i in range(L)]

	# the remaining odd variables
	r27 = [(O91[i] - O90[i]) // 192 for i in range(L)]
	r25 = [O90[i] - 819*r27[i]  for i in range(L)]
	r23 = [O87[i] - 650*r25[i] - 241605*r27[i]  for i in range(L)]
	r21 = [O83[i] - 506*r23[i] - 148005*r25[i] - 32955780*r27[i]  for i in range(L)]
	r19 = [O78[i] - 385*r21[i] - 86779*r23[i] - 15047175*r25[i] - 2230238010*r27[i]  for i in range(L)]
	r17 = [O72[i] - 285*r19[i] - 48279*r21[i] - 6369275*r23[i] - 725520510*r25[i] - 75177525150*r27[i]  for i in range(L)]
	r15 = [O65[i] - 204*r17[i] - 25194*r19[i] - 2458676*r21[i] - 209609235*r23[i] - 16410363840*r25[i] - 1213911823620*r27[i]  for i in range(L)]
	r13 = [O57[i] - 140*r15[i] - 12138*r17[i] - 846260*r19[i] - 52253971*r21[i] - 2995372800*r23[i] - 163648537860*r25[i] - 8657594647800*r27[i]  for i in range(L)]
	r11 = [O48[i] - 91*r13[i] - 5278*r15[i] - 251498*r17[i] - 10787231*r19[i] - 434928221*r21[i] - 16875270660*r23[i] - 638816292660*r25[i] - 23793900258765*r27[i]  for i in range(L)]
	r9 = [O38[i] - 55*r11[i] - 2002*r13[i] - 61490*r15[i] - 1733303*r17[i] - 46587905*r19[i] - 1217854704*r21[i] - 31306548900*r23[i] - 796513723005*r25[i] - 20135227330075*r27[i]  for i in range(L)]
	r7 = [O27[i] - 30*r9[i] - 627*r11[i] - 11440*r13[i] - 196053*r15[i] - 3255330*r17[i] - 53157079*r19[i] - 860181300*r21[i] - 13850000505*r23[i] - 222384254950*r25[i] - 3565207699131*r27[i]  for i in range(L)]
	r5 = [O15[i] - 14*r7[i] - 147*r9[i] - 1408*r11[i] - 13013*r13[i] - 118482*r15[i] - 1071799*r17[i] - 9668036*r19[i] - 87099705*r21[i] - 784246870*r23[i] - 7059619931*r25[i] - 63542171784*r27[i]  for i in range(L)]
	r3 = [O2[i] - 5*r5[i] - 21*r7[i] - 85*r9[i] - 341*r11[i] - 1365*r13[i] - 5461*r15[i] - 21845*r17[i] - 87381*r19[i] - 349525*r21[i] - 1398101*r23[i] - 5592405*r25[i] - 22369621*r27[i]  for i in range(L)]
	r1 = [O1[i] - r3[i] - r5[i] - r7[i] - r9[i] - r11[i] - r13[i] - r15[i] - r17[i] - r19[i] - r21[i] - r23[i] - r25[i] - r27[i]  for i in range(L)]

	return (r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, r26, r27, r28)

