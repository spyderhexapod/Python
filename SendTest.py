from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout, QLineEdit, QSlider,QMessageBox, QHBoxLayout
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QTextEdit, QCheckBox, QLCDNumber, QGroupBox
from PyQt5.QtCore import Qt, QObject, pyqtSignal, QByteArray, QTimer, QTime
from SerialMonitor import SerialMonitor_class
from IK import IK_class
from elipsa import Elipsa_class
from random import randint
import sys, time, threading, math, os


class Okno(QWidget):
	global monitor, timer_time, timer, czyTest
	
	monitor = SerialMonitor_class()
	timer = QTimer()
	timer_time = QTime(0, 0, 0)
	czyTest = False
	
	def __init__(self, parent = None):
		super().__init__(parent)
		self.sendInterfejs()
	
	def F(self):
		self.thread = threading.Thread(target = self.e)
		self.thread.start()
		
	def e(self):
		i = 0
		while i <= 255:
			print("Iterator:  {0}, chr(i):  {1}".format(i, chr(i)))
			self.senderMonitor.append("Iterator:  {0}, chr(i):  {1}".format(i, chr(i)))
			self.receiverMonitor.append("Iterator:  {0}, chr(i):  {1}".format(i, chr(i)))
			#time.sleep(0.01)
			i += 1
		print("koniec")
			
	def sendInterfejs(self):
		#timer
		timer.timeout.connect(self.timerEvent)
		
		#przyciski
		self.exitButton = QPushButton("&Zakończ program", self)
		self.exitButton.clicked.connect(self.end)
		
		self.beginButton = QPushButton("&Rozpocznij testowanie", self)
		self.beginButton.clicked.connect(self.beginTest)
		
		self.endButton = QPushButton("&Przerwij testowanie", self)
		self.endButton.clicked.connect(self.endTest)
		self.endButton.setEnabled(False)
		
		self.clearButton = QPushButton("&Wyczyść hisotrię", self)
		self.clearButton.clicked.connect(self.clearHistory)
		
		#SelfSend
		self.selfSendLineEdit = QLineEdit()
		self.selfSendButton = QPushButton("&Wyślij", self)
		self.selfSendButton.clicked.connect(self.selfSend)
		self.selfSendLabel = QLabel("Wyślij coś swojego: ")
		self.selfSendClearButton = QPushButton("&Wyczyść", self)
		self.selfSendClearButton.clicked.connect(self.selfSendClear)

		#moniotory
		self.senderMonitorLabel = QLabel("Wysyłane: ")
		self.senderMonitor = QTextEdit()
		
		self.receiverMonitorLabel = QLabel("Odbierane: ")
		self.receiverMonitor = QTextEdit()
		
		self.stateLabel = QLabel("Stan: Nie rozpoczęto", self)
		
		self.timeLabel = QLabel("Czas trwania:   00:00:00", self)
		
		#Layout przyciski
		ButtonLayout = QGridLayout()
		ButtonLayout.addWidget(self.beginButton, 0, 0)
		ButtonLayout.addWidget(self.exitButton, 0, 1)
		ButtonLayout.addWidget(self.clearButton, 0, 2)
		ButtonLayout.addWidget(self.endButton, 0, 3)
		
		#Layout monitory
		MonitorLayout = QGridLayout()
		MonitorLayout.addWidget(self.senderMonitor, 2, 0)
		MonitorLayout.addWidget(self.receiverMonitor, 2, 1)
		
		#Layout monitoryLabel
		MonitoryLabelLayout = QGridLayout()
		MonitoryLabelLayout.addWidget(self.senderMonitorLabel, 0, 0)
		MonitoryLabelLayout.addWidget(self.stateLabel, 0, 1)
		MonitoryLabelLayout.addWidget(self.receiverMonitorLabel, 0, 2)
		MonitoryLabelLayout.addWidget(self.timeLabel, 0, 3)
		
		#Layout SelfSend
		SelfSendLayout = QGridLayout()
		SelfSendLayout.addWidget(self.selfSendLabel, 0, 0)
		SelfSendLayout.addWidget(self.selfSendLineEdit, 0, 1)
		SelfSendLayout.addWidget(self.selfSendButton, 0, 2)
		SelfSendLayout.addWidget(self.selfSendClearButton, 0, 3)
		
		#Layout programu
		mainLayout = QGridLayout()
		mainLayout.addLayout(ButtonLayout, 0, 0)
		mainLayout.addLayout(MonitoryLabelLayout, 1, 0)
		mainLayout.addLayout(MonitorLayout, 2, 0)
		mainLayout.addLayout(SelfSendLayout, 3, 0)
		
		self.setLayout(mainLayout)
		
		self.setGeometry(20, 20, 800, 400)
		self.setWindowTitle("Program testujący komunikację")
		
		self.show()
		
		#self.e()
	
	def timerEvent(self):
		global timer_time
		timer_time = timer_time.addSecs(1)
		self.timeLabel.setText("Czas trwania:  {0}".format(timer_time.toString("hh:mm:ss")))
	
	def end(self):
		self.close()
		
	def beginTest(self):
		global czyTest
		self.beginButton.setEnabled(False)
		self.endButton.setEnabled(True)
		self.stateLabel.setText("Stan: Rozpoczęte")
		timer.start(1000)
		self.thread = threading.Thread(target = self.testThread)
		self.thread.start()
		czyTest = True
		
	def testThread(self):
		i = 0
		array = QByteArray()
		while i <= 255:
			array.append('(')
			array.append(chr(i))
			#self.senderMonitor.append("Iterator:  {0}, chr(i):  {1}".format(i, chr(i)))
			self.senderMonitor.append(str(i))
			print("Iterator:  {0}, chr(i):  {1}".format(i, chr(i)))
			monitor.serialWrite(array)
			time.sleep(0.08)
			i += 1
			array.clear()
		
	def endTest(self):
		global czyTest
		self.beginButton.setEnabled(True)
		self.endButton.setEnabled(False)
		self.stateLabel.setText("Stan: Przerwane")
		timer.stop()
		czyTest = False
		
	def selfSend(self):
			dane = self.selfSendLineEdit.text()
			self.senderMonitor.append("Własne: " + dane)
			self.selfSendLineEdit.clear()
			array = QByteArray()
			array.append('(')
			try:
				array.append(dane)
			except UnicodeEncodeError as ex:
				msg = QMessageBox()
				msg.setIcon(QMessageBox.Information)
				msg.setText("Wystąpił bład podczas próby wysłania\nPodaj inną wartość\nTreść błędu: " + str(ex))
				msg.setStandardButtons(QMessageBox.Ok)
				pom = msg.exec_()
			monitor.serialWrite(array)
		
	def clearHistory(self):
		self.receiverMonitor.clear()
		self.senderMonitor.clear()
		
	def selfSendClear(self):
		self.selfSendLineEdit.clear()
		
	def closeEvent(self, QCloseEvent):
		odp = QMessageBox.question(self,
				"Pytanie", "Naciśnięto klawisz kończoący program\nNa pewno?",
				QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if odp == QMessageBox.Yes:
			QCloseEvent.accept()
		else:
			QCloseEvent.ignore()
			
	def keyPressEvent(self, e):
		if e.key() == Qt.Key_Escape:
			self.close()
		elif e.key() == Qt.Key_W:
			if czyTest:
				msg = QMessageBox()
				msg.setIcon(QMessageBox.Information)
				msg.setText("Naciśnięto klawisz W\nTestowanie nie może zostać rozpoczęte")
				msg.setStandardButtons(QMessageBox.Ok)
				pom = msg.exec_()
			else:
				odp = QMessageBox.question(self,
					"Pytanie", "Naciśnięto klawisz W\nCzy chcesz rozpocząć testowanie?",
					QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
				if odp == QMessageBox.Yes:
					self.beginTest()
		elif e.key() == Qt.Key_S:
			if czyTest:
				odp = QMessageBox.question(self,
					"Pytanie", "Naciśnięto klawisz S\nCzy chcesz przerwać testowanie?",
					QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
				if odp == QMessageBox.Yes:
					self.endTest()
			else: 
				msg = QMessageBox()
				msg.setIcon(QMessageBox.Information)
				msg.setText("Naciśnięto klawisz S\nTestowanie nie może zostać przerwane")
				msg.setStandardButtons(QMessageBox.Ok)
				pom = msg.exec_()

		
class StoppableThread(threading.Thread):
	def __init__(self):
		super(StoppableThread, self).__init__()
		self._stop_event = threading.Event()
		
	def stop(self):
		self._stop_event.set()
		
	def stopped(self):
		return self._stop_event.is_set()
		
	
if __name__ == '__main__':
	app = QApplication(sys.argv)
	okno = Okno()
	sys.exit(app.exec_())
	
# TO DO LIST
# zaprogramowac arduino na odsylanie to co dostanie po '('
# Spyder ma chodzic
# latac tez moze
# reset arduino przez RPi
# ogarac kontroler
# wymienic czujnik(i) nacisku

