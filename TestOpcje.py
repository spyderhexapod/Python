from PyQt5.QtWidgets import QGridLayout, QMessageBox, QPushButton, QApplication, QWidget
from PyQt5.QtCore import Qt
from SendTest import Okno
from Client_PyQt5 import Client
from Server_PyQt5 import ServerClient
import sys


class TestWindowClass(QWidget):
	def __init__(self, parent = None):
		super().__init__(parent)
		
		self.testWindowInterfejs()
		
	def testWindowInterfejs(self):
		
		self.selfSendButton = QPushButton("&Testowanie komunikacji", self)
		self.selfSendButton.clicked.connect(self.selfSendButtonFunction)
		
		self.clientServerButton = QPushButton("&Testowanie klient i serwer TCP/IP", self)
		self.clientServerButton.clicked.connect(self.clientServer)
		
		self.clientButton = QPushButton("&Testowanie klienta TCP/IP", self)
		self.clientButton.clicked.connect(self.client)
		
		self.serverButton = QPushButton("&Testowanie serwera TCP/IP", self)
		self.serverButton.clicked.connect(self.server)
		
		self.exitButton = QPushButton("&Wyjdź", self)
		self.exitButton.clicked.connect(self.exitButtonFunction)
		
		mainLayout = QGridLayout()
		
		mainLayout.addWidget(self.selfSendButton, 0, 0)
		mainLayout.addWidget(self.clientServerButton, 1, 0)
		mainLayout.addWidget(self.clientButton, 2, 0)
		mainLayout.addWidget(self.serverButton, 3, 0)
		mainLayout.addWidget(self.exitButton, 4, 0)
		
		self.setLayout(mainLayout)
		
		self.setGeometry(20, 20, 300, 300)
		
		self.setWindowTitle("Testowanie")
		
		self.show()
		
	def exitButtonFunction(self):
		self.close()
		
	def selfSendButtonFunction(self):
		self.ui = Okno()

	def clientServer(self):
		okno_server = ServerClient()
		okno_client = Client()
		
	def client(self):
		self.client = Client()
		
	def server(self):
		self.server = ServerClient()
		
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
			odp = QMessageBox.question(self,
				"Pytanie", "Naciśnięto klawisz W\nCzy chcesz otworzyc testowanie komunikacji?",
				QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
			if odp == QMessageBox.Yes:
				self.selfSendButtonFunction()
		elif e.key() == Qt.Key_S:
			odp = QMessageBox.question(self,
				"Pytanie", "Naciśnięto klawisz S\nCzy chcesz otworzyć testowanie klienta i serwera?",
				QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
			if odp == QMessageBox.Yes:
				self.clientServer()
		elif e.key() == Qt.Key_A:
			odp = QMessageBox.question(self,
				"Pytanie", "Naciśnięto klawisz A\nCzy chcesz otworzyć testowanie klienta?",
				QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
			if odp == QMessageBox.Yes:
				self.client()
		elif e.key() == Qt.Key_D:
			odp = QMessageBox.question(self,
				"Pytanie", "Naciśnięto klawisz S\nCzy chcesz otworzyć testowanie serwera?",
				QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
			if odp == QMessageBox.Yes:
				self.server()


#~ if __name__ == '__main__':
	#~ app = QApplication(sys.argv)
	#~ okno = TestWindowClass()
	#~ sys.exit(app.exec_())
