import datetime


class Czas:

	def __init__(self):
		super(Czas, self).__init__()
		self.tab = []

	def daj_dane(self):
		czas = datetime.datetime.now()
		rok = czas.year
		miesiac = czas.month
		dzien = czas.day
		godzina = czas.hour
		minuta = czas.minute
		sekunda = czas.second

		return [rok, miesiac, dzien, godzina, minuta, sekunda]

	def digits(self, numer):
		self.tab.clear()
		for i in range (0, len(numer)):
			if 0 <= numer[i] < 10:
				string = '0' + str(numer[i])
				self.tab.append(string)
			else:
				self.tab.append(numer[i])
		return self.tab
