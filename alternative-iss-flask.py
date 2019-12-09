from flask import Flask, request, jsonify
import RPi.GPIO as GPIO
import time

app = Flask(__name__)
channel = 14

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)


def relay_on(pin):
    GPIO.output(pin, GPIO.HIGH)


def relay_off(pin):
    GPIO.output(pin, GPIO.LOW)


@app.route('/open', methods=["POST"])
def post():
    relay_on(channel)
    time.sleep(1)
    relay_off(channel)
    time.sleep(1)
    GPIO.cleanup()

    return jsonify({'status': 'opened'})


app.run(host='0.0.0.0', port=8090)
