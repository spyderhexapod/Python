import threading
import os
import sys
import socket
import time
import RPi.GPIO as GPIO
import serial
from PyQt5.QtWidgets import QApplication
from IK import IK_class
from Ui import Sterowanie

Rsread = "1"
global okno

wifiport = 8888
polaczeniewifi = False

bluetoothport = 0
BluetoothRPi = 'B8:27:EB:F8:2F:2A'

polaczeniebluetooth = False

qwerty = 0

timer_czas = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Ard_in = 4

def pisz(numer):
	return 0

def Czytaj():
	try:
		dane = bus.read_byte(adres_i2c)
		print(dane)
		return dane
	except OSError:
		os.system("exit")

def dane(data):
	global qwerty
	if data[0] == 0 or data[0] == 8:
		qwerty = 0

	elif data[0] == 6:
		qwerty = -6

	elif data[0] != 0 or data[0] != 8 or data[0] != 6:
		qwerty = 10

	print(data[0])
	if data[0] >= 0 and data[0] <= 8:
		pisz(data[0])
	if data[0] == 10:
		pisz(7)
		os.system("sudo shutdown -h now")
	if data[0] == 9:
		pisz(7)
		os.system("sudo reboot")

def WiFi():
		global qwerty
		wifi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			wifi.bind(('', wifiport))

		except socket.error as err:
			print("Error")
			print(err)
			sys.exit()

		wifi.listen(10)
		pisz(8)

		conn, addr = wifi.accept()
		qwerty = 0
		file = open("plik.txt", "a")
		print("Polaczono z: {0} : {1} (WiFi)".format(addr[0], str(addr[1])))
		print("Polaczenie nastapilo: {0}".format(czas()))
		file.write("Polaczono z: {0} : {1} (WiFi)  {2}".format(addr[0], str(addr[1]), czas()) + '\n')
		file.close()
		pisz(8)

		polaczeniewifi = True

		while True:
			if polaczeniewifi == False:
				conn, addr = wifi.accept()
				file = open("plik.txt", "a")
				print("Polaczono z: {0} : {1} (WiFi)".format(addr[0], str(addr[1])))
				print("Polaczenie nastapilo: {0}".format(czas()))
				file.write("Polaczono z: {0} : {1} (WiFi)  {2}".format(addr[0], str(addr[1]), czas()) + '\n')
				file.close()
				pisz(8)
				polaczeniewifi = True
				data = conn.recv(64)

				try:
					dane(data)

				except:
					file = open("plik.txt", "a")
					print("Rozlaczono z: {0} : {1} (WiFi)".format(addr[0], str(addr[1])))
					pisz(7)
					print("Rozlaczenie nastapilo: {0}".format(czas()))
					file.write("Rozlaczono z: {0} : {1} (WiFi) {2}".format(addr[0], str(addr[1]), czas()) + '\n')
					file.close()
					print("Oczekiwanie na polaczenie WiFi lub Bluetooth")
					polaczeniewifi = False

		wifi.close()

def Bluetooth():
	global qwerty
	bluetooth = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
	try:
		bluetooth.bind((BluetoothRPi, bluetoothport))

	except socket.error as err:
		print("Error")
		print(err)
		sys.exit()

	bluetooth.listen(1)
	print("Oczekiwanie na polaczenie WiFi lub Bluetooth")
	client, addr = bluetooth.accept()
	pisz(8)
	qwerty = 0
	file = open("plik.txt", "a")
	print("Polaczono z: {0} (Bluetooth)".format(addr[0]))
	print("Polaczenie nastapilo: {0}".format(czas()))
	file.write("Polaczono z: {0} (Bluetooth)  {1}".format(addr[0], czas()) + '\n')
	file.close()

	polaczeniebluetooth = True

	while True:
		if polaczeniebluetooth == False:
			client, addr = bluetooth.accept()
			pisz(8)
			file = open("plik.txt", "a")
			print("Polaczono z: {0} (Bluetooth)".format(addr[0]))
			print("Polaczenie nastapilo: {0}".format(czas()))
			file.write("Polaczono z: {0} (Bluetooth)  {1}".format(addr[0], czas()) + '\n')
			file.close()
			polaczeniebluetooth = True

		try:
			data = client.recv(1024)
			dane(data)

		except:
			file = open("plik.txt", "a")
			print("Rozlaczono z: {0} (Bluetooth)".format(addr[0]))
			pisz(7)
			print("Rozlaczenie nastapilo: {0}".format(czas()))
			file.write("Rozlaczono z: {0} (Bluetooth)  {1}".format(addr[0], czas()) + '\n')
			file.close()
			print("Oczekiwanie na polaczenie WiFi lub Bluetooth")
			polaczeniebluetooth = False

	bluetooth.close()

def czas():
	return time.strftime('%d/%m/%Y, %X')

def licznik():
	global qwerty
	while True:
		qwerty += 1
		time.sleep(1)
		if qwerty == 9:
		 pisz(7)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	okno = Sterowanie()

	a = threading.Thread(name = 'WiFi', target = WiFi)
	b = threading.Thread(name = 'Bluetooth', target = Bluetooth)
	c = threading.Thread(name = 'licznik', target = licznik)

 #  a.start()
 #  b.start()
 #  c.start()
 #  d.start()
 #  e.start()
 #  f.start()
 #  g.start()
 #  h.start()
 #  i.start()

	sys.exit(app.exec_())

