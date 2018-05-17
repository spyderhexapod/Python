from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout, QLineEdit, QSlider,QMessageBox, QHBoxLayout, QMainWindow
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QTextEdit, QCheckBox, QLCDNumber, QGroupBox
from PyQt5.QtCore import Qt, QObject, pyqtSignal, QByteArray
from SerialMonitor import SerialMonitor_class
from IK import IK_class
from elipsa import Elipsa_class
from SendTest import Okno
from TestOpcje import TestWindowClass
import sys, time, threading, random, math, os

#Bartek wtykał kabelki 26.04.2018

class Sterowanie(QWidget):
	global IK, monitor, katyVar, sliderTab, elipsa
	
	IK = IK_class()
	monitor = SerialMonitor_class()
	elipsa = Elipsa_class()
	
	def __init__(self, parent=None):
		super().__init__(parent)
		self.slider = []
		self.label = []
		self.lcd = []		
		self.label1 = []
		self.numerySerw = [16, 17, 18, 13, 14, 15, 10, 11, 12, 7, 8, 9, 4, 5, 6, 1, 2, 3]
		self.katyVar = False
		
		self.interfejs()
		
		self.x_label_camera.setText("X: {0}".format(str(self.x_slider_camera.value())))
		self.y_label_camera.setText("Y: {0}".format(str(self.y_slider_camera.value())))
		self.yLabelSpyder.setText("Y: {0} %".format(IK.mapFunction(self.y_slider_spyder.value(), -180, -40, 0, 100)))
		self.xLabelSpyder.setText("Y: {0} %".format(IK.mapFunction(self.x_slider_spyder.value(), -180, -40, 0, 100)))
		self.zLabelSpyder.setText("Z: {0} %".format(IK.mapFunction(self.z_slider_spyder.value(), -180, -40, 0, 100)))
		
		self.distanceLabel.setText("Odległość: Nieznana")
		
		self.LP_line.setText("LP: {0} {1} {2}".format(IK.katy[0], IK.katy[1], IK.katy[2]))
		self.LS_line.setText("LS: {0} {1} {2}".format(IK.katy[3], IK.katy[4], IK.katy[5]))
		self.LT_line.setText("LT: {0} {1} {2}".format(IK.katy[6], IK.katy[7], IK.katy[8]))
		self.PP_line.setText("PP: {0} {1} {2}".format(IK.katy[9], IK.katy[10], IK.katy[11]))
		self.PS_line.setText("PS: {0} {1} {2}".format(IK.katy[12], IK.katy[13], IK.katy[14]))
		self.PT_line.setText("PT: {0} {1} {2}".format(IK.katy[15], IK.katy[16], IK.katy[17]))
		thread = threading.Thread(target = self.default)
		#thread = threading.Thread(target = self.test)
		#thread.start()

		self.x_slider_spyder.setTickPosition(QSlider.TicksBelow)
		self.x_slider_spyder.setTickInterval(10)
		self.y_slider_spyder.setTickPosition(QSlider.TicksBothSides)
		self.y_slider_spyder.setTickInterval(10)
		self.z_slider_spyder.setTickPosition(QSlider.TicksBelow)
		self.z_slider_spyder.setTickInterval(10)
		self.x_slider_camera.setTickPosition(QSlider.TicksBelow)
		self.x_slider_camera.setTickInterval(10)
		self.y_slider_camera.setTickPosition(QSlider.TicksBothSides)
		self.y_slider_camera.setTickInterval(10)
		
	def test(self):
		time.sleep(2.5)
		self.noga1('|')
		self.noga2('|')
		self.noga3('|')
		self.noga4('|')
		self.noga5('|')
		self.noga6('#')
		print("dziala")

	def default(self):
		time.sleep(2.5)
		elipsa.tablica("LP", IK.katy[0], IK.katy[1], IK.katy[2], 254, False)
		elipsa.tablica("LS", IK.katy[3], IK.katy[4], IK.katy[5], 254, False)
		elipsa.tablica("LT", IK.katy[6], IK.katy[7], IK.katy[8], 254, False)
		elipsa.tablica("PP", IK.katy[9], IK.katy[10], IK.katy[11], 254, False)
		elipsa.tablica("PS", IK.katy[12], IK.katy[13], IK.katy[14], 254, False)
		elipsa.tablica("PT", IK.katy[15], IK.katy[16], IK.katy[17], 255, True)
		
	def kinematyka_wartosci(self):
		
		self.auto_checkbox.setChecked(False)
		
		self.slider[0].setRange(-200, 100)
		self.slider[0].setValue(-59)
		
		self.slider[1].setRange(-150, 0)
		self.slider[1].setValue(-118)
		
		self.slider[2].setRange(-150, 100)
		self.slider[2].setValue(-60)
		
		self.slider[3].setRange(-200, 100)
		self.slider[3].setValue(-85)
		
		self.slider[4].setRange(-150, 0)
		self.slider[4].setValue(-118)
		
		self.slider[5].setRange(-80, 80)
		self.slider[5].setValue(0)
		
		self.slider[6].setRange(-200, 100)
		self.slider[6].setValue(-60)
		
		self.slider[7].setRange(-161, 0)
		self.slider[7].setValue(-118)
		
		self.slider[8].setRange(-200, 100)
		self.slider[8].setValue(60)
		
		self.slider[9].setRange(0, 170)
		self.slider[9].setValue(60)
		
		self.slider[10].setRange(-150, 0)
		self.slider[10].setValue(-118)
		
		self.slider[11].setRange(-100, 100)
		self.slider[11].setValue(-60)
		
		self.slider[12].setRange(-200, 100)
		self.slider[12].setValue(85)
		
		self.slider[13].setRange(-150, 0)
		self.slider[13].setValue(-118)
		
		self.slider[14].setRange(-80, 80)
		self.slider[14].setValue(0)
		
		self.slider[15].setRange(0, 170)
		self.slider[15].setValue(60)
		
		self.slider[16].setRange(-150, 0)
		self.slider[16].setValue(-118)
		
		self.slider[17].setRange(-100, 100)
		self.slider[17].setValue(60)
		
		self.auto_checkbox.setChecked(True)

	def interfejs(self):

		self.auto_checkbox = QCheckBox("Automatyczne wysyłanie", self)
		self.auto_checkbox.setChecked(True)
		self.auto_checkbox.clicked.connect(self.checkboxFunction)
		
		self.execution_Button = QPushButton("&Wykonaj", self)
		self.execution_Button.clicked.connect(self.execution)
		
		self.forward_Button = QPushButton("&Do przodu", self)
		self.forward_Button.clicked.connect(self.front)
		
		self.reset_button = QPushButton("&Reset", self)
		self.reset_button.clicked.connect(self.resetButtonClicked)
		
		self.naKatyButton = QPushButton("&Zamień na kąty", self)
		self.naKatyButton.clicked.connect(self.katy)
		
		self.distanceButton = QPushButton("                   Odczytaj odległość                  ")
		self.distanceButton.clicked.connect(self.distance)
		
		self.wheelButton = QPushButton("&Rysuj koło", self)
		self.wheelButton.clicked.connect(elipsa.wheel)
		
		self.elipse1Button = QPushButton("&Rysowanie elipsy1", self)
		self.elipse1Button.clicked.connect(elipsa.ellipse1)
		
		self.elipse2Button = QPushButton("&Rysowanie elipsy2", self)
		self.elipse2Button.clicked.connect(elipsa.ellipse2)
		
		self.elipse3Button = QPushButton("&Rysowanie elipsy3", self)
		self.elipse3Button.clicked.connect(elipsa.ellipse3)
		
		self.elipse4Button = QPushButton("&Rysowanie elipsy4", self)
		self.elipse4Button.clicked.connect(elipsa.ellipse4)
		
		self.elipse5Button = QPushButton("&Rysowanie elipsy5", self)
		self.elipse5Button.clicked.connect(elipsa.ellipse5)
		
		self.elipse6Button = QPushButton("&Rysowanie elipsy6", self)
		self.elipse6Button.clicked.connect(elipsa.ellipse6)
		
		self.walk1Button = QPushButton("&ChodźR", self)
		self.walk1Button.clicked.connect(elipsa.walkR)
		
		self.walk2Button = QPushButton("&ChodźL", self)
		self.walk2Button.clicked.connect(elipsa.walkL)
		
		self.OffButton = QPushButton("&Off RPi", self)
		self.OffButton.clicked.connect(self.Shutdown)
		
		self.RestartButton = QPushButton("&Restart RPi", self)
		self.RestartButton.clicked.connect(self.Reboot)
		
		self.ResetArduinoButton = QPushButton("&Reset arduino", self)
		self.ResetArduinoButton.clicked.connect(self.ResetArduino)
		
		self.SendTestButton = QPushButton("&Testy", self)
		self.SendTestButton.clicked.connect(self.SendTest)
		
		self.distanceLabel = QLabel(self)

		self.monitor_receiver = QTextEdit(self)
		
		#TextEdit tablica
		self.tabTextEdit = QTextEdit()
		elipsa.setValue(self.tabTextEdit)
		
		#slidery i labely do kamery
		self.y_slider_camera = QSlider(Qt.Vertical, self)
		self.y_slider_camera.setRange(1,180)
		self.y_slider_camera.setValue(20)
		self.y_slider_camera.valueChanged.connect(self.valueChangedYc)
		self.x_slider_camera = QSlider(Qt.Horizontal, self)
		self.x_slider_camera.setRange(1, 180)
		self.x_slider_camera.setValue(90)
		self.x_slider_camera.valueChanged.connect(self.valueChangedXc)
		self.x_label_camera = QLabel(self)
		self.y_label_camera = QLabel(self) 
		self.camera_labelY = QLabel("OkoY: ", self)
		self.camera_labelX = QLabel("OkoX: ", self)

		#slider gora_dol
		self.y_slider_spyder = QSlider(Qt.Vertical, self)
		self.y_slider_spyder.setRange(-180, -40)
		self.y_slider_spyder.setValue(-118)
		self.y_slider_spyder.valueChanged.connect(self.valueChangedSpyderY)
		self.yLabelSpyder = QLabel(self)
		self.yLabel = QLabel("Pion: ", self)
		
		#slider przod_tyl
		self.x_slider_spyder = QSlider(Qt.Horizontal, self)
		self.x_slider_spyder.setRange(-180, -40)
		self.x_slider_spyder.setValue(-118)
		self.x_slider_spyder.valueChanged.connect(self.valueChangedSpyderX)
		self.xLabelSpyder = QLabel(self)
		self.xLabel = QLabel("Poziomo: ", self)
		
		#slider prawo_lewo
		self.z_slider_spyder = QSlider(Qt.Horizontal, self)
		self.z_slider_spyder.setRange(-180, -40)
		self.z_slider_spyder.setValue(-118)
		self.z_slider_spyder.valueChanged.connect(self.valueChangedSpyderZ)
		self.zLabelSpyder = QLabel(self)
		self.zLabel = QLabel("Prawo - Lewo: ", self)
		
		#wysiwetlacze i label LCD do czujnikow nacisku
		self.Pressure_button = QPushButton("&Odczytaj nacisk", self)
		self.Pressure_button.clicked.connect(self.pressFunction)
		self.LcdN1 = QLCDNumber()
		self.LcdN2 = QLCDNumber()
		self.LcdN3 = QLCDNumber()
		self.LcdN4 = QLCDNumber()
		self.LcdN5 = QLCDNumber()
		self.LcdN6 = QLCDNumber()
		
		self.LcdN1_label = QLabel("LP")
		self.LcdN2_label = QLabel("LS")
		self.LcdN3_label = QLabel("LT")
		self.LcdN4_label = QLabel("PP")
		self.LcdN5_label = QLabel("PS")
		self.LcdN6_label = QLabel("PT")

		self.LP_line = QLineEdit(self)
		self.LS_line = QLineEdit(self)
		self.LT_line = QLineEdit(self)
		self.PP_line = QLineEdit(self)
		self.PS_line = QLineEdit(self)
		self.PT_line = QLineEdit(self)

		ukladKaty = QGridLayout()
		ukladKaty.addWidget(self.CreateKatyGroupBox(), 0, 0)
		ukladKaty.addWidget(self.monitor_receiver, 1, 0)
		ukladKaty.addWidget(self.tabTextEdit, 2, 0)
		
		#opcje
		ukladOpcje = QVBoxLayout()
		ukladOpcje.addWidget(self.OffButton, 1)
		ukladOpcje.addWidget(self.RestartButton, 2)
		ukladOpcje.addWidget(self.ResetArduinoButton, 3)
		
		#dystans
		ukladDystans = QGridLayout()
		ukladDystans.addWidget(self.distanceButton, 0, 0)
		ukladDystans.addWidget(self.distanceLabel, 1, 0)

		#Nogi
		LegLayout = QGridLayout()
		LegLayout.addWidget(self.auto_checkbox, 0, 0)
		LegLayout.addWidget(self.naKatyButton, 0, 1)
		LegLayout.addWidget(self.CreateGroupBox("Lewy Przód", 0, 3), 1, 0)
		LegLayout.addWidget(self.CreateGroupBox("Lewy Środek", 3, 6), 2, 0)
		LegLayout.addWidget(self.CreateGroupBox("Lewy Tył", 6, 9), 3, 0)
		LegLayout.addWidget(self.CreateGroupBox("Prawy Przód", 9, 12), 1, 1)
		LegLayout.addWidget(self.CreateGroupBox("Prawy Środek", 12, 15), 2, 1)
		LegLayout.addWidget(self.CreateGroupBox("Prawy Tył", 15, 18), 3, 1)
		for i in range(0, len(self.slider)):
			self.slider[i].setTickPosition(QSlider.TicksBelow)
			self.slider[i].setTickInterval(10)
		self.kinematyka_wartosci() #ustawienie sliderow na IK
			
		#slidery pionowe (OkoY i pion)
		ukladT1 = QGridLayout()
		ukladT1.addWidget(self.camera_labelY, 0, 0)
		ukladT1.addWidget(self.yLabel, 0, 1)
		ukladT1.addWidget(self.y_slider_camera, 1, 0)
		ukladT1.addWidget(self.y_slider_spyder, 1, 1)
		
		#wartości ze sliderow pionowych (OkoY i pion)
		ukladT12 = QGridLayout()
		ukladT12.addWidget(self.y_label_camera, 0, 0)
		ukladT12.addWidget(self.yLabelSpyder, 0, 1)
		
		#slidery poziome(OkoX i poziom) i prawo-lewo
		ukladXZ = QGridLayout()
		ukladXZ.addWidget(self.camera_labelX, 0, 0)
		ukladXZ.addWidget(self.x_slider_camera, 0, 1)
		ukladXZ.addWidget(self.x_label_camera, 0, 2)
		ukladXZ.addWidget(self.xLabel, 1, 0)
		ukladXZ.addWidget(self.x_slider_spyder, 1, 1)
		ukladXZ.addWidget(self.xLabelSpyder, 1, 2)
		ukladXZ.addWidget(self.zLabel, 2, 0)
		ukladXZ.addWidget(self.z_slider_spyder, 2, 1)
		ukladXZ.addWidget(self.zLabelSpyder, 2, 2)
		
		#elipsy
		ukladT5 = QVBoxLayout()
		ukladT5.addWidget(self.wheelButton, 0)
		ukladT5.addWidget(self.elipse1Button, 1)
		ukladT5.addWidget(self.elipse2Button, 2)
		ukladT5.addWidget(self.elipse3Button, 3)
		ukladT5.addWidget(self.elipse4Button, 4)
		ukladT5.addWidget(self.elipse5Button, 5)
		ukladT5.addWidget(self.elipse6Button, 6)
		ukladT5.addWidget(self.walk1Button, 7)
		ukladT5.addWidget(self.walk2Button, 8)
		ukladT5.addWidget(self.SendTestButton, 9)
		
		#reset, wykonaj, do przodu
		ukladB = QVBoxLayout()
		ukladB.addWidget(self.reset_button, 1)
		ukladB.addWidget(self.execution_Button, 2)
		ukladB.addWidget(self.forward_Button, 3)

		#Czujniki nacisku
		ukladT2 = QGridLayout()
		ukladT2.addWidget(self.LcdN1, 0, 0)
		ukladT2.addWidget(self.LcdN2, 0, 1)
		ukladT2.addWidget(self.LcdN3, 0, 2)
		ukladT2.addWidget(self.LcdN4, 0, 3)
		ukladT2.addWidget(self.LcdN5, 0, 4)
		ukladT2.addWidget(self.LcdN6, 0, 5)
		ukladT2.addWidget(self.Pressure_button, 0 ,6)
		ukladT2.addWidget(self.LcdN1_label, 0, 0)
		ukladT2.addWidget(self.LcdN2_label, 0, 1)
		ukladT2.addWidget(self.LcdN3_label, 0, 2)
		ukladT2.addWidget(self.LcdN4_label, 0, 3)
		ukladT2.addWidget(self.LcdN5_label, 0, 4)
		ukladT2.addWidget(self.LcdN6_label, 0, 5)

		MainLayout = QGridLayout()
		MainLayout.addLayout(LegLayout, 0, 0)
		MainLayout.addLayout(ukladKaty, 0, 1)
		MainLayout.addLayout(ukladDystans, 1, 1)
		MainLayout.addLayout(ukladT1, 0, 2)
		MainLayout.addLayout(ukladT2, 1, 0)
		MainLayout.addLayout(ukladT5, 0, 3)
		MainLayout.addLayout(ukladT12, 1, 2)
		MainLayout.addLayout(ukladB, 2, 1)
		MainLayout.addLayout(ukladXZ, 2, 0)
		MainLayout.addLayout(ukladOpcje, 2, 2)

		self.setLayout(MainLayout)

		self.setGeometry(20, 20, 800, 400)
		self.setWindowTitle("Sterowanie - Spyder")

		monitor.bufferUpdated.connect(self.RSRead)

		self.show()

		monitor.start()
		
	def SendTest(self):
		self.ui = TestWindowClass()
		
	def CreateKatyGroupBox(self):
		groupBox = QGroupBox("Aktualne kąty")
		ukladKaty = QGridLayout()
		ukladKaty.addWidget(self.LP_line, 0, 0)
		ukladKaty.addWidget(self.LS_line, 1, 0)
		ukladKaty.addWidget(self.LT_line, 2, 0)
		ukladKaty.addWidget(self.PP_line, 0, 1)
		ukladKaty.addWidget(self.PS_line, 1, 1)
		ukladKaty.addWidget(self.PT_line, 2, 1)
		groupBox.setLayout(ukladKaty)
		return groupBox
		
	def CreateGroupBox(self, nazwa, p, k):
		groupBox = QGroupBox(nazwa)
		vbox = QGridLayout()
		for i in range(p, k):
			self.slider.append(QSlider(Qt.Horizontal))
			self.label.append(QLabel(str(i + 1) + '.'))
			self.lcd.append(QLCDNumber())			
			if i == 2 or i == 5 or i == 8 or i == 11 or i == 14 or i == 17:
				if i == 0: continue
				self.label1.append(QLabel("(Z)"))
			elif i % 3 == 0:
				self.label1.append(QLabel("(X)"))
			elif i == 1 or i == 4 or i == 7 or i == 10 or i == 13 or i == 16:
				self.label1.append(QLabel("(Y)"))
			vbox.addWidget(self.label[i], i, 0)
			vbox.addWidget(self.slider[i], i, 1)
			vbox.addWidget(self.lcd[i], i, 2)
			vbox.addWidget(self.label1[i], i, 2)
			self.slider[i].valueChanged.connect(lambda value, segment=str(i): self.sliderValueChanged(value, segment))
			self.slider[i].setTickPosition(QSlider.TicksBelow)
			self.slider[i].setTickInterval(10)
			
		groupBox.setLayout(vbox)
		return groupBox
		
	def sliderValueChanged(self, value, segment):
		number = int(segment)
		#print(number)
		self.lcd[number].display(value)
		if not self.katyVar:
			if number >= 0 and number <= 2:
				self.noga1('#')
			elif number >= 3 and number <= 5:
				self.noga2('#')
			elif number >= 6 and number <= 8:
				self.noga3('#')
			elif number >= 9 and number <= 11:
				self.noga4('#')
			elif number >= 12 and number <= 14:
				self.noga5('#')
			elif number >= 15 and number <= 17:
				self.noga6('#')
		else:
			if self.auto_checkbox.isChecked():
				array = QByteArray()
				array.append('$')
				array.append(chr(self.numerySerw[int(segment)]))
				print("segment: {0}, value: {1}, numer: {2}".format(segment, value, self.numerySerw[int(segment)]))
				array.append('|')
				if value == 35:
					array.append(chr(247))
				else:
					array.append(chr(value))
				array.append('#')
				monitor.serialWrite(array)
		
	def Shutdown(self):
		odp = QMessageBox.question(self,
				"Pytanie", "Wyłączanie RPi\nCzy na pewno? ",
				QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if odp == QMessageBox.Yes:
			os.system("sudo shutdown -h now")
		
	def Reboot(self):
		odp = QMessageBox.question(self,
				"Pytanie", "Restartowanie RPi\nCzy na pewno? ",
				QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if odp == QMessageBox.Yes:
			os.system("sudo reboot")
		
	def ResetArduino(self):
		odp = QMessageBox.question(self,
				"Pytanie", "Reset Arduino\nCzy na pewno? ",
				QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if odp == QMessageBox.Yes:
			array = QByteArray()
			array.append('*')
			monitor.serialWrite(array)
			
			time.sleep(3)
			
			thread = threading.Thread(target = self.default)
			#thread = threading.Thread(target = self.test)
			#thread.start()
	
	def valueChangedSpyderX(self):
		self.xLabelSpyder.setText("X: {0} %".format(IK.mapFunction(self.x_slider_spyder.value(), -180, -40, 0, 100)))
		
	def valueChangedSpyderZ(self):
		self.zLabelSpyder.setText("Z: {0} %".format(IK.mapFunction(self.z_slider_spyder.value(), -180, -40, 0, 100)))

	def valueChangedSpyderY(self):
		i = 1
		while i <= 17:
			self.auto_checkbox.setChecked(False)
			self.slider[i].setValue(self.y_slider_spyder.value())
			self.yLabelSpyder.setText("Y: {0} %".format(IK.mapFunction(self.y_slider_spyder.value(), -180, -40, 0, 100)))
			i += 3
		self.execution()

	def distance(self):
		array = QByteArray()
		array.append('%')
		monitor.serialWrite(array)
		
	def front(self):
		ft = threading.Thread(target = self.front_thread)
		ft.start()
		
	def front_thread(self):
		delay = 0.75
		self.sliderY2.setValue(-80)
		self.sliderY4.setValue(-80)
		self.sliderY6.setValue(-80)
		#monitor.Czy_ready()
		time.sleep(delay)
		self.execution()
		
		self.sliderZ2.setValue(-50)
		self.sliderX2.setValue(-60)
		self.sliderZ4.setValue(-100)
		self.sliderX4.setValue(5)
		self.sliderZ6.setValue(0)
		self.sliderX6.setValue(85)
		#monitor.Czy_ready()
		time.sleep(delay)
		self.execution()
		
		self.sliderY2.setValue(-118)
		self.sliderY4.setValue(-118)
		self.sliderY6.setValue(-118)
		self.sliderX2.setValue(-70)
		#monitor.Czy_ready()
		time.sleep(delay)
		self.execution()
		
	def execution(self):
		self.auto_checkbox.setChecked(True)
		self.noga1(254)
		self.noga2(254)
		self.noga3(254)
		self.noga4(254)
		self.noga5(254)
		self.noga6(255)
		self.auto_checkbox.setChecked(False)
		
	def katy(self):
		if self.katyVar:            
			self.naKatyButton.setText("Kąty")
			self.katyVar = False
			self.y_slider_spyder.setEnabled(True)
			self.x_slider_spyder.setEnabled(True)
			self.z_slider_spyder.setEnabled(True)
			self.kinematyka_wartosci()
		elif not self.katyVar:
			self.naKatyButton.setText("Kinematyka")
			self.katyVar = True
			self.y_slider_spyder.setEnabled(False)
			self.x_slider_spyder.setEnabled(False)
			self.z_slider_spyder.setEnabled(False)
			for i in range(0, len(self.slider)):
				self.slider[i].setRange(0, 180)
				self.slider[i].setValue(IK.katy[i])
					   
	def pressFunction(self):
		self.thread = threading.Thread(target = self.pressFunctionThread)
		self.thread.start()
		
	def pressFunctionThread(self):
		while True:
			array = QByteArray()
			array.append('@')
			monitor.serialWrite(array)
			time.sleep(0.4)
	   
	def valueChangedYc(self):
		array = QByteArray()
		array.append(chr(20))
		array.append('|')
		if self.y_slider_camera.value() != 124:
			array.append(chr(self.y_slider_camera.value()))
		else:
			array.append(chr(200))
		array.append('|')
		array.append(chr(255))
		array.append('#')
		
		self.y_label_camera.setText("Y: " + str(self.y_slider_camera.value()))
			  
		monitor.serialWrite(array)
		
	def valueChangedXc(self):
		array = QByteArray()
		array.append(chr(19))
		array.append('|')
		array.append(chr(self.x_slider_camera.value()))
		array.append('|')
		array.append(chr(255))
		array.append('#')
		
		self.x_label_camera.setText("X: " + str(self.x_slider_camera.value()))
		
		monitor.serialWrite(array)
		 
	def resetButtonClicked(self):      
		self.x_slider_camera.setValue(90)
		self.y_slider_camera.setValue(20)
		
		if not self.katyVar:
			self.slider[0].setValue(-85)
			self.slider[1].setValue(-118)
			self.slider[2].setValue(-90)

			self.slider[3].setValue(-85)
			self.slider[4].setValue(-118)
			self.slider[5].setValue(0)

			self.slider[6].setValue(-85)
			self.slider[7].setValue(-120)
			self.slider[8].setValue(50)

			self.slider[9].setValue(85)
			self.slider[10].setValue(-118)
			self.slider[11].setValue(-80)

			self.slider[12].setValue(85)
			self.slider[13].setValue(-118)
			self.slider[14].setValue(0)

			self.slider[15].setValue(85)
			self.slider[16].setValue(-118)
			self.slider[17].setValue(100)
			
		else:
			for i in range(0, len(self.slider)):
				self.slider[i].setValue(IK.katy[i])
			
	def closeEvent(self, QCloseEvent):
		odp = QMessageBox.question(self,
			"Pytanie", "Czy na pewno? ",
			QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if odp == QMessageBox.Yes:
			QCloseEvent.accept()
		else:
			QCloseEvent.ignore()
			
	def keyPressEvent(self, e):
		if e.key() == Qt.Key_Escape:
			self.close()
		elif e.key() == Qt.Key_W:
			self.front()
		elif e.key() == Qt.Key_S:
			print("Dziala s")
		elif e.key() == Qt.Key_A:
			print("Dziala a")
		elif e.key() == Qt.Key_D:
			print("Dziala D")

	def koniec(self):
		self.close()
		
	def noga1(self, znak):
		value = IK.IK_LP(self.slider[0].value(), self.slider[1].value(), self.slider[2].value())
		if self.auto_checkbox.isChecked() and not self.katyVar:
			try:               
				elipsa.tablica("LP", value[0], value[1], value[2], znak, True)
			except:
				print("Poza zakresem")    
		self.LP_line.setText("LP: " + str(value[0]) + "  " + str(value[1]) + "  " + str(value[2]))
			
	def noga2(self, znak):
		value = IK.IK_LS(self.slider[3].value(), self.slider[4].value(), self.slider[5].value())
		if self.auto_checkbox.isChecked() and not self.katyVar:
			try:
				elipsa.tablica("LS", value[0], value[1], value[2], znak, True)
			except:
				print("Poza zakresem")
		self.LS_line.setText("LS: " + str(value[0]) + "  " + str(value[1]) + "  " + str(value[2]))       
		 
	def noga3(self, znak):
		value = IK.IK_LT(self.slider[6].value(), self.slider[7].value(), self.slider[8].value())
		if self.auto_checkbox.isChecked() and not self.katyVar:
			#try:              
			elipsa.tablica("LT", value[0], value[1], value[2], znak, True)  
		   # except:
			   # print("Poza zakresem")
		self.LT_line.setText("LT: " + str(value[0]) + "  " + str(value[1]) + "  " + str(value[2]))

	def noga4(self, znak):
		value = IK.IK_PP(self.slider[9].value(), self.slider[10].value(), self.slider[11].value())
		if self.auto_checkbox.isChecked() and not self.katyVar:
			try:                
				elipsa.tablica("PP", value[0], value[1], value[2], znak, True)
			except:
				print("Poza zakresem")
		self.PP_line.setText("PP: " + str(value[0]) + "  " + str(value[1]) + "  " + str(value[2]))

	def noga5(self, znak):
		value = IK.IK_PS(self.slider[12].value(), self.slider[13].value(), self.slider[14].value())
		if self.auto_checkbox.isChecked() and not self.katyVar:
			try:
				elipsa.tablica("PS", value[0], value[1], value[2], znak, True)
			except:
				print("Poza zakresem")
		self.PS_line.setText("PS: " + str(value[0]) + "  " + str(value[1]) + "  " + str(value[2]))

	def noga6(self, znak):
		value = IK.IK_PT(self.slider[15].value(), self.slider[16].value(), self.slider[17].value())
		if self.auto_checkbox.isChecked() and not self.katyVar:
			try:
				elipsa.tablica("PT", value[0], value[1], value[2], znak, True)
			except:
				print("Poza zakresem")
		self.PT_line.setText("PT: " + str(value[0]) + "  " + str(value[1]) + "  " + str(value[2]))

	def checkboxFunction(self):
		print("oK")
		
	def RSRead(self, msg):
		if msg[2] == '@':
			tab = msg[3 : -6].split('|')
			self.LcdN1.display(int((int(tab[0]) * 100) / 255))
			self.LcdN2.display(int((int(tab[1]) * 100) / 255))
			self.LcdN3.display(int((int(tab[2]) * 100) / 255))
			self.LcdN4.display(int((int(tab[3]) * 100) / 255))
			self.LcdN5.display(int((int(tab[4]) * 100) / 255))
			self.LcdN6.display(int((int(tab[5]) * 100) / 255))
			self.monitor_receiver.append(str(msg)[3 : -6])
		elif  msg[2] == '%':
			self.distanceLCD.display(int(msg[3: -5]))
			self.monitor_receiver.append(str(msg)[3: -5])
		else:
			self.monitor_receiver.append(str(msg[2 : -5]))  

if __name__ == '__main__':
	app = QApplication(sys.argv)
	okno = Sterowanie()
	sys.exit(app.exec_())
