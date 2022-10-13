import serial

serialport = serial.Serial("/dev/ttyAMA0", 9600, timeout=3)

while True:
    towrite = input("TX data : ")

    serialport.write((towrite+'\n').encode("ascii"))

    print("RX data : " + serialport.readline().decode("utf-8"))
