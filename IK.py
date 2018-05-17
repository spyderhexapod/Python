import math
  
class IK_class:
	
	katy = [122, 114, 132,
			128, 117, 111,
			120, 125, 84, 
			68, 62, 89, 
			62, 57, 48,
			55, 46, 80]

	def IK_LP(self, y, x, z):
 
		a1 = 85
		a2 = 118

		Q3 = math.atan2(z, y)
		Y_korekta = y / math.cos(Q3)
		L = math.sqrt(math.pow(x, 2) + math.pow(Y_korekta, 2))
		Q3 *= 180 / math.pi

		if Q3 == 0: Q3 = 180

		s3 = int(Q3 - 91)

		if s3 < 0: s3 += 360
	
		if Y_korekta * y < 0: Y_korekta *= (-1)
	
		Q2 = math.acos((math.pow(x, 2) + math.pow(Y_korekta, 2) - math.pow(a1, 2) - math.pow(a2, 2)) / (2 * a1 * a2))

		Q2 *= 180 / math.pi * (-1)

		beta = math.atan2(Y_korekta, x)

		fi = math.acos((math.pow(x, 2) + math.pow(Y_korekta, 2) + math.pow(a1, 2) - math.pow(a2, 2)) / (2 * a1 * L))

		zmienna = True

		while zmienna:
			if Q2 < 0: Q1 = beta + fi
			else: Q1 = beta - fi
			Q1 *= 180 / math.pi
			s2 = int(180-(Q2 + 146))
			if Q1 < 0: s1 = int(Q1 + 206)
			else: s1 = int(Q1 - 360)

			if s2 > 180: Q2 = -Q2

			if s2 <= 180: zmienna = False
			
		#print ("Katy LP: s1: {0}, s2: {1}, s3: {2}".format(s1, s2, s3))

		if s1 or s2 or s3 >= 0:
			return [s2, s1, s3]
   
	def IK_LS (self, y, x, z):
		a1 = 85
		a2 = 118

		Q3 = math.atan2(z, y)
		Y_korekta = y / math.cos(Q3)
		L = math.sqrt(math.pow(x, 2) + math.pow(Y_korekta, 2))
		Q3 *= 180 / math.pi

		if Q3 == 0: Q3 = 180

		s3 = int(Q3 - 64) 

		if s3 < 0: s3 += 360
	
		if Y_korekta * y < 0: Y_korekta *= (-1)
	
		Q2 = math.acos((math.pow(x, 2) + math.pow(Y_korekta, 2) - math.pow(a1, 2) - math.pow(a2, 2)) / (2 * a1 * a2))

		Q2 *= 180 / math.pi * (-1)

		beta = math.atan2(Y_korekta, x)

		fi = math.acos((math.pow(x, 2) + math.pow(Y_korekta, 2) + math.pow(a1, 2) - math.pow(a2, 2)) / (2 * a1 * L))

		zmienna = True       

		while zmienna:   
			if Q2 < 0: Q1 = beta + fi
			else: Q1 = beta - fi
			Q1 *= 180 / math.pi
			s2 = int(-Q2 + 38)
			if Q1 < 0: s1 = int(Q1 + 207)
			else: s1 = int(Q1 - 360)

			if s2 > 180: Q2 = -Q2

			if s2 <= 180: zmienna = False

		if s1 or s2 or s3 >= 0:
			return [s2, s1, s3]

	def IK_LT(self, y, x, z):
		a1 = 85
		a2 = 118

		Q3 = math.atan2(z, y)
		Y_korekta = y / math.cos(Q3)
		L = math.sqrt(math.pow(x, 2) + math.pow(Y_korekta, 2))
		Q3 *= 180 / math.pi

		if Q3 == 0: Q3 = 180

		s3 = int(Q3 - 51) 

		if s3 < 0: s3 += 360
	
		if Y_korekta * y < 0: Y_korekta *= (-1)
	
		Q2 = math.acos((math.pow(x, 2) + math.pow(Y_korekta, 2) - math.pow(a1, 2) - math.pow(a2, 2)) / (2 * a1 * a2))

		Q2 *= 180 / math.pi * (-1)

		beta = math.atan2(Y_korekta, x)

		fi = math.acos((math.pow(x, 2) + math.pow(Y_korekta, 2) + math.pow(a1, 2) - math.pow(a2, 2)) / (2 * a1 * L))

		zmienna = True

		while zmienna:   
			if Q2 < 0: Q1 = beta + fi
			else: Q1 = beta - fi
			Q1 *= 180 / math.pi
			#s2 = int(Q2 + 250)
			s2 = int(180 - (Q2 + 143))
			if Q1 < 0: s1 = int(Q1 + 216)
			else: s1 = int(Q1 - 360)

			if s2 > 180: Q2 = -Q2

			if s2 <= 180: zmienna = False

		#if s3 == 172: s3 = 116
		
		#print("Q1: {0}, s1: {1}\n, Q2: {2}, s2: {3}\n, Q3: {4}, s3: {5}\n".format(Q1, s1, Q2, s2, Q3, s3))
		
		if s1 or s2 or s3 >= 0:
			return [s2, s1, s3]

	def IK_PP(self, y, x, z):
		a1 = 85
		a2 = 118

		Q3 = math.atan2(z, y)
		Y_korekta = y / math.cos(Q3)
		L = math.sqrt(math.pow(x, 2) + math.pow(Y_korekta, 2))
		Q3 *= 180 / math.pi

		if Q3 == 180: Q3 = 0

		s3 = int(Q3 + 134) 

		if s3 < 0: s3 += 360
		if Y_korekta * y < 0: Y_korekta *= (-1)
	
		Q2 = math.acos((math.pow(x, 2) + math.pow(Y_korekta, 2) - math.pow(a1, 2) - math.pow(a2, 2)) / (2 * a1 * a2))

		Q2 *= 180 / math.pi #* (-1)

		beta = math.atan2(Y_korekta, x)

		fi = math.acos((math.pow(x, 2) + math.pow(Y_korekta, 2) + math.pow(a1, 2) - math.pow(a2, 2)) / (2 * a1 * L))

		zmienna = True

		while zmienna:   
			if Q2 < 0: Q1 = beta + fi
			else: Q1 = beta - fi
			Q1 *= 180 / math.pi
		
			s2 = int(180 - (Q2 + 20))

			s1 = int(Q1 - 29)

			if s2 > 180: Q2 = -Q2

			if s2 <= 180: zmienna = False
			
		#print ("PP Q1: {0}, Q2: {1}, Q3 {2}".format(Q1, Q2, Q3))

		if s1 or s2 or s3 >= 0:
			return [s2, s1, s3]

	def IK_PS(self, y, x, z):
		a1 = 85
		a2 = 118

		Q3 = math.atan2(z, y)
		Y_korekta = y / math.cos(Q3)
		L = math.sqrt(math.pow(x, 2) + math.pow(Y_korekta, 2))
		Q3 *= 180 / math.pi

		if Q3 == 180: Q3 = 0

		s3 = int(Q3 + 48) 

		if s3 < 0: s3 += 360
	
		if Y_korekta * y < 0: Y_korekta *= (-1)
	
		Q2 = math.acos((math.pow(x, 2) + math.pow(Y_korekta, 2) - math.pow(a1, 2) - math.pow(a2, 2)) / (2 * a1 * a2))

		Q2 *= 180 / math.pi #* (-1)

		beta = math.atan2(Y_korekta, x)

		fi = math.acos((math.pow(x, 2) + math.pow(Y_korekta, 2) + math.pow(a1, 2) - math.pow(a2, 2)) / (2 * a1 * L))

		zmienna = True

		while zmienna:   
			if Q2 < 0: Q1 = beta + fi
			else: Q1 = beta - fi
			
			Q1 *= 180 / math.pi
		
			s2 = int(-Q2 + 152)

			s1 = int(Q1 - 33)

			if s2 > 180: Q2 = -Q2

			if s2 <= 180: zmienna = False 
			
		#print ("Srodek: Q1: {0},Q2: {1}, Q3: {2}".format(Q1, Q2, Q3))          

		if s1 or s2 or s3 >= 0:
			return [s2, s1, s3]

	def IK_PT(self, y, x, z):
		a1 = 85
		a2 = 118

		Q3 = math.atan2(z, y)
		Y_korekta = y / math.cos(Q3)
		L = math.sqrt(math.pow(x, 2) + math.pow(Y_korekta, 2))
		Q3 *= 180 / math.pi

		if Q3 == 180: Q3 = 0

		s3 = int(Q3 + 32) 

		if s3 < 0: s3 += 360
	
		if Y_korekta * y < 0: Y_korekta *= (-1)
	
		Q2 = math.acos((math.pow(x, 2) + math.pow(Y_korekta, 2) - math.pow(a1, 2) - math.pow(a2, 2)) / (2 * a1 * a2))

		Q2 *= 180 / math.pi #* (-1)

		beta = math.atan2(Y_korekta, x)

		fi = math.acos((math.pow(x, 2) + math.pow(Y_korekta, 2) + math.pow(a1, 2) - math.pow(a2, 2)) / (2 * a1 * L))

		zmienna = True

		while zmienna:   
			if Q2 < 0: Q1 = beta + fi
			else: Q1 = beta - fi
			Q1 *= 180 / math.pi
		
			s2 = int(180 - (Q2 + 35))

			s1 = int(Q1 - 43)

			if s2 > 180: Q2 = -Q2

			if s2 <= 180: zmienna = False
			
		#print ("Q1: {0}, Q2: {1}, Q3: {2}".format(Q1, Q2, Q3))

		if s1 or s2 or s3 >= 0:
			return [s2, s1, s3]

	def mapFunction(self, x, in_min, in_max, out_min, out_max):
		return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
