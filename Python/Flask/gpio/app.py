from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

app = Flask(__name__)

toggley = True
toggleb = True

@app.route("/", methods=["GET","POST"])
def index():
	global toggley
	global toggleb
	no1 = "ERROR"
	no2 = "ERROR"
	x = "#AAA000"
	y = "#000000"
	while True:
		if request.method == "POST":
			msg = request.form.get("submitBtn")
			if msg == "GO":
				if toggley == True:
					toggley = False
				else:
					toggley = True
			else:
				if msg != "GO":
					msg = request.form.get("submit2")
					if msg == "OFF":
						GPIO.output(17,GPIO.LOW)
						no1 = "Yellow OFF"
						x = "#AAA000"
		if request.method == "POST":
			msg2  = request.form.get("submit2")
			if msg2  == "OFF":
				if toggleb == True:
					toggleb = False
				else:
					toggleb = True
			else:
				if msg2 != "OFF":
					msg2 = request.form.get("submitBtn")
					if msg2 == "GO":
						GPIO.output(6,GPIO.LOW)
						no2 = "Blue OFF"
						y = "#000AAA"
		else:
			GPIO.output(17,GPIO.LOW)
			GPIO.output(6,GPIO.LOW)
			msg = "No click yet."
			msg2 = "No click yet."
		if toggley == True:
			GPIO.output(17,GPIO.LOW)
			no1 = "Yellow OFF"
			x = "#AAA000"
		else:
			if toggley == False:
				GPIO.output(17,GPIO.HIGH)
				no1 = "Yellow ON"
				x = "#FFF000"
		if toggleb == True:
			GPIO.output(6,GPIO.LOW)
			no2 = "Blue OFF"
			y = "#000AAA"
		else:
			if toggleb == False:
				GPIO.output(6,GPIO.HIGH)
				no2 = "Blue ON"
				y = "#000FFF"
		return render_template("index.html", no1=no1, no2=no2, x=x, y=y)
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)

