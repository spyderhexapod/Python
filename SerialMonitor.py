from PyQt5.QtCore import Qt, QObject, pyqtSignal, QByteArray
import serial
import threading
import time

class SerialMonitor_class(QObject):
	pom = ''
	bufferUpdated = pyqtSignal(str)
	ser = serial.Serial('/dev/ttyACM0', baudrate=115200,  # ttyAMA0
						parity=serial.PARITY_NONE,
						stopbits=serial.STOPBITS_ONE,
						bytesize=serial.EIGHTBITS)

	def __init__(self):
		super(SerialMonitor_class, self).__init__()
		self.running = False
		self.thread = threading.Thread(target=self.serial_monitor_thread)

	def start(self):
		self.running = True
		self.thread.start()

	def stop(self):
		self.running = False
		self.ser.close()

	def serialWrite(self, serialIn):
		self.ser.write(serialIn)

	def Czy_ready(self):
		while self.pom == b'?\r\n':
			time.sleep(0.1)

	def Func(self):
		if self.pom == b'!\r\n':
			print("ready")
		else:
			print("busy")

	def serial_monitor_thread(self):
		while self.running is True:
			msg = self.ser.readline()
			if msg:
				try:
					self.bufferUpdated.emit(str(msg))
					self.pom = msg
					msg = ''
				except ValueError:
					print('Wrong data')
			else:
				pass
			# self.ser.close()
