from flask import Flask, request, jsonify
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

URL = 'http://localhost/me'


@app.route('/open', methods=["POST"])
def post():
    token = request.headers['x-auth-token']
    response = requests.get(url=URL, headers={'x-auth-token': token}).content
    print(response)

    # relay_on(channel)
    # time.sleep(5)
    # relay_off(channel)

    return jsonify({'status': 'opened'})


app.run(host='0.0.0.0', port=8090)
