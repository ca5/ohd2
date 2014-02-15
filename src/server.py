# -*- coding: utf-8 -*-
from module import *
from flask import Flask
import time
import json
import subprocess

app = Flask(__name__)
app.debug=True

def say_alert():
    subprocess.call(u'say せんたくものを　とりこみます。　ものほしざおから　はなれてください', shell=True)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/selenoid")
def selenoid():
    a = ArduinoWrapper()
    say_alert()
    time.sleep(0.3)
    a.update_pin(12, True)
    time.sleep(0.5)
    a.update_pin(12, False)
    return json.dumps({'status': 200})

if __name__ == "__main__":
    app.run()
