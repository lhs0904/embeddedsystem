from flask import Flask, render_template
from flask_socketio import SocketIO
import RPi.GPIO as GPIO
from ssd1306_oled import *
from PIL import ImageFont, Image, ImageDraw

LED = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

spi = busio.SPI(11, 10, 9)
rst_pin = digitalio.DigitalInOut(board.D24) # any pin!
cs_pin = digitalio.DigitalInOut(board.D8)    # any pin!
dc_pin = digitalio.DigitalInOut(board.D23)    # any pin!

#font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
font_path = "/home/pi/KDL.ttf"
oled = ssd1306.SSD1306_SPI(128,64, spi, dc_pin, rst_pin, cs_pin)
font = ImageFont.truetype(font_path, 15)

#flask web server
app = Flask(__name__)

# flask web server 위에 socket
socketio = SocketIO(app)
print(__name__)

@socketio.on("text")
def text(q):
	image = Image.new("1", (128,64))
	draw = ImageDraw.Draw(image)

	draw.text((0,0), q, font=font, fill=255)
	oled.image(image)
	oled.show()


# 웹서버의 경로
@app.route("/")
def hello():
	return render_template("index.html")
	
@app.route("/bye")
def bye():
	return "Good bye"

@socketio.on("led_on")
def led_on():
	GPIO.output(LED, True)
	
@socketio.on("led_off")
def led_off():
	GPIO.output(LED, False)
	
@app.route("/socket")
def socket():
	return render_template("socket_index.html")
	
if __name__ == "__main__":
	socketio.run(app, host="0.0.0.0", port=8000) #서버를 생성하고 실행
