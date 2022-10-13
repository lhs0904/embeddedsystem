import serial

dev = serial.Serial("/dev/ttyACM0", 9600)
dev.flush()

try:
	while True:
		if dev.in_waiting > 0:
			line = dev.readline().decode("utf-8").rstrip()
			print(line)
except KeyboardInterrupt:
	pass
