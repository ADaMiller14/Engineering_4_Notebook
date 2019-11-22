from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

app = Flask(__name__)

togglea = True

@app.route("/", methods=["GET","POST"])
def index():
	global togglea
	no1 = "ERROR"
	y = "#000000"
	while True:
		if request.method == "POST":
			msg = request.form.get("submitBtn")
			if msg == "GO":
				if togglea == True:
					togglea = False
				else:
					togglea = True
		else:
			GPIO.output(17,GPIO.LOW)
			msg = "No click yet."

		if togglea == True:
			GPIO.output(17,GPIO.LOW)
			no1 = "Stealth Mode: ON"
			y = "#000000"
		else:
			if togglea == False:
				GPIO.output(17,GPIO.HIGH)
				no1 = "Stealth Mode: OFF"
				y = "#FF0000"
				time.sleep(.5)
				GPIO.output(17,GPIO.LOW)
				no1 = "Stealth Mode: ON"
				y = "#000000"
				togglea = True
		return render_template("annoy.html", no1=no1, y=y)
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
