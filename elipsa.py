from SerialMonitor import SerialMonitor_class
from PyQt5.QtCore import QByteArray
from IK import IK_class
import math, time

class Elipsa_class:

	global monitor, IK, array, TextEdit
	
	monitor = SerialMonitor_class()
	IK = IK_class()
	array = QByteArray()

	def setValue(self, s):
		global TextEdit
		TextEdit = s
		
	def ellipse1(self):
		TextEdit.append("ok")
		i = 180
			
		while i >= 0:
			value = IK.IK_PT(60, int(-118 + 20 * math.cos(i * math.pi / 180)),int(60 + 50 * math.sin(i * math.pi / 180)))
				
			i -= 5

			self.tablica("PT", value[0], value[1], value[2], 255, True)
			
			time.sleep(0.05)
			
		i = 360
		
		while i >= 270:
			value = IK.IK_PT(60, int(-118 + 20 * math.cos(i * math.pi / 180)),int(60 + 50 * math.sin(i * math.pi / 180)))
			i -= 5

			self.tablica("PT", value[0], value[1], value[2], 255, True)
			
			time.sleep(0.05)
			
		i = 10
		j = -116
		
		while i <= 60:
			j -= 2 
			
			value = IK.IK_PT(60, j, i)
			
			i += 5
			
			self.tablica("PT", value[0], value[1], value[2], 255, True)
			
			time.sleep(0.1)
			
	def ellipse2(self):
		i = 180
			
		while i >= 0:
			value = IK.IK_PP(60, int(-118 + 20 * math.cos(i * math.pi / 180)), int(-60 + 50 * math.sin(i * math.pi / 180)))
				
			i -= 5
			
			self.tablica("PP", value[0], value[1], value[2], 255, True)
			
			time.sleep(0.05)
			
		i = 360
		
		while i >= 270:
			value = IK.IK_PP(60, int(-118 + 20 * math.cos(i * math.pi / 180)), int(-60 + 50 * math.sin(i * math.pi / 180)))
				
			i -= 5

			self.tablica("PP", value[0], value[1], value[2], 255, True)
			
			time.sleep(0.05)
			
		i = -110
		j = -124
		
		while i <= -50:
			j -= 1
			
			valuea = IK.IK_PP(60, j, i)
			
			i += 5
			
			self.tablica("PP", value[0], value[1], value[2], 255, True)
			
			time.sleep(0.1)
			
	def ellipse3(self):
		i = 180
			
		while i >= 0:
			value = IK.IK_LS(-85, int(-118 + 20 * math.cos(i * math.pi / 180)), int(0 + 50 * math.sin(i * math.pi / 180)))
				
			i -= 5

			self.tablica("LS", value[0], value[1], value[2], 255, True)
			
			time.sleep(0.05)
			
		i = 360
		
		while i >= 270:
			value = IK.IK_LS(-85, int(-118 + 20 * math.cos(i * math.pi / 180)), int(0 + 50 * math.sin(i * math.pi / 180)))
				
			i -= 5

			self.tablica("LS", value[0], value[1], value[2], 255, True)
			
			time.sleep(0.05)
			
		i = -50
		j = -118
		
		while i < 0:
			j -= 2
			
			value = IK.IK_LS(-85, j, i)
			
			i += 5
			
			self.tablica("LS", value[0], value[1], value[2], 255, True)
			
			time.sleep(0.1)
	
	def ellipse4(self):
		i = 180
			
		while i >= 0:
			value = IK.IK_LT(-60, int(-118 + 20 * math.cos(i * math.pi / 180)),int(60 + 50 * math.sin(i * math.pi / 180)))
			
			i -= 5

			self.tablica("LT", value[0], value[1], value[2], 255, True)
			
			time.sleep(0.05)
			
		i = 360
		
		while i >= 270:
			value = IK.IK_LT(-60, int(-118 + 20 * math.cos(i * math.pi / 180)),int(60 + 50 * math.sin(i * math.pi / 180)))
			
			i -= 5
			
			self.tablica("LT", value[0], value[1], value[2], 255, True)
			
			time.sleep(0.05)
			
		i = 10
		j = -118
		
		while i < 60:
			
			value = IK.IK_LT(-60, j, i)
			
			j -= 2
			i += 5

			self.tablica("LT", value[0], value[1], value[2], 255, True)
			
			time.sleep(0.1)

	def ellipse5(self):
		i = 180
			
		while i >= 0:
			value = IK.IK_PS(85, int(-118 + 20 * math.cos(i * math.pi / 180)), int(0 + 50 * math.sin(i * math.pi / 180))) 
			
			i -= 5

			self.tablica("PS", value[0], value[1], value[2], 255, True)
			
			time.sleep(0.05)
			
		i = 360
		
		while i >= 270:
			value = IK.IK_PS(85, int(-118 + 20 * math.cos(i * math.pi / 180)), int(0 + 50 * math.sin(i * math.pi / 180)))
				
			i -= 5

			self.tablica("PS", value[0], value[1], value[2], 255, True)
			
			time.sleep(0.05)
			
		i = -50
		j = -118
		
		while i < 0:
			value = IK.IK_PS(85, j, i)
			
			j -= 2
			i += 5

			self.tablica("PS", value[0], value[1], value[2], 255, True)
			
			time.sleep(0.1)
		
	def ellipse6(self):
		i = 180
			
		while i >= 0:
			value = IK.IK_LP(-60, int(-118 + 20 * math.cos(i * math.pi / 180)), int(-60 + 50 * math.sin(i * math.pi / 180)))
				
			i -= 5

			self.tablica("LP", value[0], value[1], value[2], 255, True)
			
			time.sleep(0.05)
			
		i = 360
		
		while i >= 270:
			value = IK.IK_LP(-60, int(-118 + 20 * math.cos(i * math.pi / 180)), int(-60 + 50 * math.sin(i * math.pi / 180)))
			
				
			i -= 5

			self.tablica("LP", value[0], value[1], value[2], 255, True)
			
			time.sleep(0.05)
			
		i = -110
		j = -124
		
		while i <= -50:
			
			j -= 1
			
			value = IK.IK_LP(-60, j, i)
			
			i += 5

			self.tablica("LP", value[0], value[1], value[2], 255, True)
			
			time.sleep(0.1)
		
	def walkR(self):
		i = 180
		
		while i >= 0:
			value = IK.IK_PT(60, int(-118 + 20 * math.cos(i * math.pi / 180)),int(60 + 50 * math.sin(i * math.pi / 180)))
			
			self.tablica("PT", value[0], value[1], value[2], 254, True)
			
			value = IK.IK_PP(60, int(-118 + 20 * math.cos(i * math.pi / 180)), int(-60 + 50 * math.sin(i * math.pi / 180)))
			
			self.tablica("PP", value[0], value[1], value[2], 254, True)
			
			value = IK.IK_LS(-85, int(-118 + 20 * math.cos(i * math.pi / 180)), int(0 + 50 * math.sin(i * math.pi / 180)))
			
			self.tablica("LS", value[0], value[1], value[2], 255, True)
			
			time.sleep(0.05)
			
			i -= 5
			
		i = 360
		
		while i >= 270:
			value = IK.IK_PT(60, int(-118 + 20 * math.cos(i * math.pi / 180)),int(60 + 50 * math.sin(i * math.pi / 180)))
			
			self.tablica("PT", value[0], value[1], value[2], 254, True)
			
			value = IK.IK_PP(60, int(-118 + 20 * math.cos(i * math.pi / 180)), int(-60 + 50 * math.sin(i * math.pi / 180)))
			
			self.tablica("PP", value[0], value[1], value[2], 254, True)
			
			value = IK.IK_LS(-85, int(-118 + 20 * math.cos(i * math.pi / 180)), int(0 + 50 * math.sin(i * math.pi / 180)))
				
			self.tablica("LS", value[0], value[1], value[2], 255, True)
			
			time.sleep(0.05)
			
			i -= 5
			
		i = 10
		i2 = -110
		i3 = -50
		
		j = -116
		j2 = -124
		j3 = -118
		
		while i2 <= -50:
			j -= 2
			j2 -= 1
			j3 -= 2 
			
			if i <= 60:
				value = IK.IK_PT(60, j, i)
				
			if i <= 60:
				self.tablica("PT", value[0], value[1], value[2], 254, True)
				
			if i3 < 0:
				value = IK.IK_LS(-85, j3, i3)
				
				self.tablica("LS", value[0], value[1], value[2], 254, True)
		
			value = IK.IK_PP(60, j2, i2)
			
			i += 5
			i2 += 5
			i3 += 5
			
			self.tablica("PP", value[0], value[1], value[2], 255, True)
			
			time.sleep(0.1)
		
	def walkL(self):
		i = 180
		
		while i >= 0:
			value = IK.IK_LT(-60, int(-118 + 20 * math.cos(i * math.pi / 180)),int(60 + 50 * math.sin(i * math.pi / 180))) 
			
			self.tablica("LT", value[0], value[1], value[2], 254, True)
			
			value = IK.IK_PS(85, int(-118 + 20 * math.cos(i * math.pi / 180)), int(0 + 50 * math.sin(i * math.pi / 180))) 

			self.tablica("PS", value[0], value[1], value[2], 254, True)
			
			value = IK.IK_LP(-60, int(-118 + 20 * math.cos(i * math.pi / 180)), int(-60 + 50 * math.sin(i * math.pi / 180))) 
			
			self.tablica("LP", value[0], value[1], value[2], 255, True)
			
			time.sleep(0.05)
			
			i -= 5
			
		i = 360
		
		while i >= 270:
			value = IK.IK_LT(-60, int(-118 + 20 * math.cos(i * math.pi / 180)),int(60 + 50 * math.sin(i * math.pi / 180)))
			
			self.tablica("LT", value[0], value[1], value[2], 254, True)
			
			value = IK.IK_PS(85, int(-118 + 20 * math.cos(i * math.pi / 180)), int(0 + 50 * math.sin(i * math.pi / 180)))

			self.tablica("PS", value[0], value[1], value[2], 254, True)
			
			value = IK.IK_LP(-60, int(-118 + 20 * math.cos(i * math.pi / 180)), int(-60 + 50 * math.sin(i * math.pi / 180)))
			
			self.tablica("LP", value[0], value[1], value[2], 255, True)

			i -= 5

			time.sleep(0.05)

		i = 10
		i2 = -58
		i3 = -110
		
		j = -118
		j2 = -118
		j3 = -124

		while i3 <= -50:
			j -= 2
			j2 -= 2
			j3 -= 1 

			if i < 60:
				value = IK.IK_LT(-60, j, i)

				self.tablica("LT", value[0], value[1], value[2], 255, True)

			if i2 < 0:
				value = IK.IK_PS(85, j2, i2)
				
				self.tablica("PS", value[0], value[1], value[2], 254, True)

			value = IK.IK_LP(-60, j3, i3)
			
			self.tablica("LP", value[0], value[1], value[2], 255, True)
			
			i += 5
			i2 += 5
			i3 += 5
			
			time.sleep(0.1)
		
	def wheel(self):
		i = 0
		while i <= 1440:
			value = IK.IK_PT(60, int(-118 + 50 * math.cos(i * math.pi / 180)),int(60 + 50 * math.sin(i * math.pi / 180)))
			
			i += 5
			self.tablica("PT", value[0], value[1], value[2], 255, True)
			time.sleep(0.05)
	
	def tablica(self, noga, value0, value1, value2, numer, send):
		if noga == "LP":
			serwo = 16
			serwo1 = 17
			serwo2 = 18
		elif noga == "LS":
			serwo = 13
			serwo1 = 14
			serwo2 = 15
		elif noga == "LT":
			serwo = 10
			serwo1 = 11
			serwo2 = 12
		elif noga == "PP":
			serwo = 7
			serwo1 = 8
			serwo2 = 9
		elif noga == "PS":
			serwo = 4
			serwo1 = 5
			serwo2 = 6
		elif noga == "PT":
			serwo = 1
			serwo1 = 2
			serwo2 = 3
		
		if value0 == 124:
			value0 = 200
		if value1 == 124:
			value1 = 200
		if value2 == 124:
			value2 = 200

		array.append(chr(serwo))
		array.append('|')
		array.append(chr(int(value0)))
		array.append('|')
		array.append(chr(254))
		array.append('#')
		array.append(chr(serwo1))
		array.append('|')
		array.append(chr(int(value1)))
		array.append('|')
		array.append(chr(254))
		array.append('#')
		array.append(chr(serwo2))
		array.append('|')
		array.append(chr(int(value2)))
		array.append('|')
		try:
			array.append(chr(numer))
		except:
			array.append(numer)
		array.append('#') # To chyba powinno być wyzej
		
		if send:
			TextEdit.append(str(array))
			print(str(array))
			monitor.serialWrite(array)
			array.clear()
