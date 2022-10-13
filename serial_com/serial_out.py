import serial
import time

dev = serial.Serial("/dev/ttyACM0", 9600)
dev.flush()

cmds = ['h', 'l']
idx = 0

try:
	while True:
		idx = 0 if idx == 1 else 1
		raw = cmds[idx]
		print(raw)
		
		dev.write(raw.encode("utf-8"))
		time.sleep(1)
except KeyboardInterrupt:
	pass
	
