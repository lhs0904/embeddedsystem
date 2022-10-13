from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

# 웹서버의 경로
@app.route("/")
def hello():
	return render_template("index.html")
	
@app.route("/bye")
def bye():
	return "Good bye"
	
@app.route("/socket")
def socket():
	return render_template("socket_index.html")
	
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80) #서버를 생성하고 실행
