from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QGridLayout, QCheckBox, QLineEdit
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QTextEdit, QMessageBox
from time_class import Czas
import sys
import socket
import threading
import time
import datetime

global okno


class Client(QWidget):

	global ip_adress, czy_clear, czy_connected

	def __init__(self):
		super(Client, self).__init__()
		self.czy_clear = True
		self.czy_connected = False
		self.okno()
		self.interfejs()
		self.tab = []
		self.thread = threading.Thread(target=self.timer)
		self.thread.start()

	def timer(self):
		while True:
			A = Czas()
			dane = A.digits(A.daj_dane())
			self.time_label.setText("Data i czas:  {0}-{1}-{2}  {3}:{4}:{5}".format(dane[0], dane[1], dane[2], dane[3], dane[4], dane[5]))
			time.sleep(1)

	def closeEvent(self, QCloseEvent):
		odp = QMessageBox.question(self,
			"Pytanie", "Czy na pewno? ",
			QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if odp == QMessageBox.Yes:
			QCloseEvent.accept()
		else:
			QCloseEvent.ignore()

	def okno(self):
		self.setWindowTitle("Klient PyQt5")
		self.setGeometry(300, 300, 720, 400)

	def interfejs(self):
		# textbox oraz label
		self.ip_textbox = QLineEdit(self)
		self.data_textbox = QLineEdit(self)
		self.history_textbox = QTextEdit(self)
		self.ip_textbox.setText("127.0.0.1")
		self.ip_label = QLabel("Podaj ip: ", self)
		self.send_label = QLabel("Podaj dane: ", self)
		self.connect_label = QLabel("Stan: Rozłączono", self)
		self.time_label = QLabel("2018-01-06  16:00:00", self)

		# Przyciski
		self.connect_btn = QPushButton("&Połącz", self)
		self.send_btn = QPushButton("&Wyślij", self)
		self.disconnect_btn = QPushButton("&Rozłącz", self)
		self.exit_btn = QPushButton("&Wyjdż", self)
		self.clear_btn = QPushButton("&Wyczyść hisotorię", self)

		# Checkbox
		self.auto_checkbox = QCheckBox('Nie czyść po wysłaniu', self)

		self.connect_btn.clicked.connect(self.connectFunction)
		self.disconnect_btn.clicked.connect(self.disconnectFunction)
		self.send_btn.clicked.connect(self.send)
		self.exit_btn.clicked.connect(self.exitFunction)
		self.clear_btn.clicked.connect(self.clear)
		self.auto_checkbox.clicked.connect(self.clear_checkbox)

		ukladH = QHBoxLayout()
		ukladH.addWidget(self.connect_btn)
		ukladH.addWidget(self.send_btn)
		ukladH.addWidget(self.disconnect_btn)

		ukladH1 = QHBoxLayout()
		ukladH1.addWidget(self.ip_label, 0)
		ukladH1.addWidget(self.ip_textbox, 1)
		ukladH1.addWidget(self.connect_label, 2)
		ukladH1.addWidget(self.time_label, 4)

		ukladH2 = QHBoxLayout()
		ukladH2.addWidget(self.clear_btn)
		ukladH2.addWidget(self.auto_checkbox)
		ukladH2.addWidget(self.exit_btn)

		ukladH3 = QHBoxLayout()
		ukladH3.addWidget(self.send_label)
		ukladH3.addWidget(self.data_textbox)

		ukladT = QGridLayout()
		ukladT.addLayout(ukladH1, 0, 0, 1, 3)
		ukladT.addWidget(self.history_textbox, 1, 0, 1, 0)
		ukladT.addLayout(ukladH3, 2, 0, 1, 0)
		ukladT.addLayout(ukladH, 3, 0, 1, 3)
		ukladT.addLayout(ukladH2, 4, 0, 1, 3)

		self.setLayout(ukladT)

		self.show()
	
	def exitFunction(self):
		if not self.czy_connected:
			self.close()
		else:
			msg = QMessageBox()
			msg.setText("Połączenie z serwerem jest aktywne")
			msg.setIcon(QMessageBox.Information)
			msg.setWindowTitle("Informacja")
			msg.setStandardButtons(QMessageBox.Ok)
			retval = msg.exec_()
			odp = QMessageBox.question(self,
				"Pytanie", "Czy chcesz wyjść i zakończyć połączenie? ",
				QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
			if odp == QMessageBox.Yes:
				self.disconnectFunction()
				self.close()

	def connectFunction(self):
		if not self.czy_connected:
			thread = threading.Thread(target=self.serwer())
			thread.start()
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Information)
			msg.setText("Połączenie z serwerem jest aktywne")
			msg.setWindowTitle("Informacja")
			msg.setStandardButtons(QMessageBox.Ok)
			retval = msg.exec_()

	def disconnectFunction(self):
		if self.czy_connected:
			self.s.send(bytes("exit".encode()))
			self.history_textbox.append("exit")
			self.history_textbox.append("Rozłączono z serwerem")
			self.connect_label.setText("Stan: Rozłączono")
			self.czy_connected = False
		else:
			msg = QMessageBox()
			msg.setText("Połączenie z serwerem musi być aktywne")
			msg.setIcon(QMessageBox.Information)
			msg.setWindowTitle("Informacja")
			msg.setStandardButtons(QMessageBox.Ok)
			retval = msg.exec_()

	def clear(self):
		self.history_textbox.clear()

	def clear_checkbox(self):
		if self.czy_clear:
			self.czy_clear = False
		else:
			self.czy_clear = True

	def send(self):
		try:
			if self.czy_connected:
				text = self.data_textbox.text()
				if text:
					self.history_textbox.append(text)
					self.s.send(bytes(text.encode()))
					if self.czy_clear:
						self.data_textbox.clear()
			else:
				msg = QMessageBox()
				msg.setText("Połączenie z serwerem musi być aktywne")
				msg.setIcon(QMessageBox.information)
				msg.setWindowTitle("Informacja")
				msg.setStandardButtons(QMessageBox.Ok)
				retval = msg.exec_()
		except:
			msg = QMessageBox()
			msg.setText("Wystąpił błąd podczas próby wysłania danych")
			msg.setIcon(QMessageBox.Critical)
			msg.setWindowTitle("Error")
			msg.setStandardButtons(QMessageBox.Ok)
			retval = msg.exec_()

	def serwer(self):
		ip_adress = self.ip_textbox.text()
		p_o_r_t = 8888

		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.history_textbox.append("Próba połączenia z: {0}".format(ip_adress))

		try:
			self.s.connect((ip_adress, p_o_r_t))
			self.history_textbox.append("Polaczono z: {0}".format(ip_adress))
			self.connect_label.setText("Stan: Połączono")
			self.czy_connected = True

		except ConnectionRefusedError as err:
			self.history_textbox.append("Błąd")
			self.history_textbox.append(str(err))
