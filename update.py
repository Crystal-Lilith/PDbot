from flask import Flask, request
from os import system
import threading

app = Flask(__name__)

@app.route('/update', method=['POST'])
def update():
    if request.method != 'POST':
        return 'bad request',401
    threading.Thread(system, args=('killall python3 && killall ruby && git pull && sh main.sh')).start()
    return "nice"

app.run('0.0.0.0', 9000)