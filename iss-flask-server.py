from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
import requests

# import RPi.GPIO as GPIO
# import time

app = Flask(__name__)
# channel = 14


# GPIO setup
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(channel, GPIO.OUT)


# def relay_on(pin):
# GPIO.output(pin, GPIO.HIGH)


# def relay_off(pin):
# GPIO.output(pin, GPIO.LOW)

app.config['BASIC_AUTH_USERNAME'] = 'iss'
app.config['BASIC_AUTH_PASSWORD'] = 'ujkjdjyju'

basic_auth = BasicAuth(app)


@app.route('/open', methods=["POST"])
@basic_auth.required
def post():

    # relay_on(channel)
    # time.sleep(5)
    # relay_off(channel)

    return jsonify({'status': 'opened'})


app.run(host='0.0.0.0', port=8090)
