from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QGridLayout, QCheckBox, QLineEdit
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QTextEdit, QMessageBox
from time_class import Czas
import sys
import socket
import threading
import time

global okno


class ServerClient(QWidget):

	global ip_adress, czy_clear, czy_connected

	def __init__(self):
		super(ServerClient, self).__init__()
		self.czy_clear = True
		self.czy_connected = False
		self.okno()
		self.interfejs()
		self.tab = []
		self.thread = threading.Thread(target=self.timer)
		self.thread.start()
		self.serwer_thread = threading.Thread(target=self.serwerFunction)
		self.serwer_thread.start()

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
		self.setWindowTitle("Serwer PyQt5")
		self.setGeometry(300, 300, 720, 400)

	def interfejs(self):
		# textbox oraz label
		self.serwer_textbox = QTextEdit(self)
		self.ip_label = QLabel("IP klienta: 0.0.0.0:0000             ", self)
		self.connect_label = QLabel("Stan: Rozłączono z klientem", self)
		self.time_label = QLabel("2018-01-06  16:00:00", self)

		# Przyciski
		self.exit_btn = QPushButton("&Wyjdż", self)
		self.clear_btn = QPushButton("&Wyczyść hisotorię", self)

		self.exit_btn.clicked.connect(self.exitFunction)
		self.clear_btn.clicked.connect(self.clear)

		ukladH1 = QHBoxLayout()
		ukladH1.addWidget(self.ip_label, 0)
		ukladH1.addWidget(self.connect_label, 1)
		ukladH1.addWidget(self.time_label, 2)

		ukladH2 = QHBoxLayout()
		ukladH2.addWidget(self.clear_btn)
		ukladH2.addWidget(self.exit_btn)

		ukladT = QGridLayout()
		ukladT.addLayout(ukladH1, 0, 0, 1, 3)
		ukladT.addWidget(self.serwer_textbox, 1, 0, 1, 0)
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
				self.disconnect_btn()
				self.close()

	def clear(self):
		self.serwer_textbox.clear()

	def clear_checkbox(self):
		if self.czy_clear:
			self.czy_clear = False
		else:
			self.czy_clear = True

	#~ def serwer(self):
		#~ ip_adress = self.ip_textbox.text()
		#~ p_o_r_t = 8888
#~ 
		#~ self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#~ self.history_textbox.append("Próba połączenia z: {0}".format(ip_adress))
#~ 
		#~ try:
			#~ self.s.connect((ip_adress, p_o_r_t))
			#~ self.history_textbox.append("Polaczono z: {0}".format(ip_adress))
			#~ self.connect_label.setText("Stan: Połączono")
			#~ self.czy_connected = True
#~ 
		#~ except ConnectionRefusedError as err:
			#~ self.history_textbox.append("Błąd")
			#~ self.history_textbox.append(str(err))
	
	def serwerFunction(self):

		p_o_r_t = 8888

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("Utworzono socket")
		self.serwer_textbox.append("Utworzono socket")

		try:
			s.bind(('', p_o_r_t))

		except socket.error as err:
			self.serwer_textbox.append("ERROR")
			self.serwer_textbox.append(str(err))
			sys.exit()

		s.listen(10)
		self.serwer_textbox.append("Oczekiwanie na polaczenie")

		conn, addr = s.accept()

		self.serwer_textbox.append("Polaczono z {0}:{1}".format(addr[0], addr[1]))
		self.ip_label.setText("IP klienta: {0}:{1}     ".format(addr[0], addr[1]))
		self.connect_label.setText("Stan: Połączono z klientem")

		polaczenie = True

		while True:
			if not polaczenie:
				conn, addr = s.accept()
				self.serwer_textbox.append("Polaczono z {0}:{1}".format(addr[0], addr[1]))
				self.ip_label.setText("IP klienta: {0}:{1}     ".format(addr[0], addr[1]))
				self.connect_label.setText("Stan: Połączono z klientem")
				polaczenie = True

			try:
				data = conn.recv(64)
				data = data.decode("utf-8")
				if data:
					self.serwer_textbox.append(data)

					if data == "exit":
						self.ip_label.setText("IP klienta: 0.0.0.0:0000     ")
						raise ZeroDivisionError

			except:
				self.serwer_textbox.append("Rozlaczono z {0}:{1}".format(addr[0], addr[1]))
				self.serwer_textbox.append("Oczekiwanie na polaczenie")
				self.connect_label.setText("Stan: Rozłączono z klientem")
				polaczenie = False
