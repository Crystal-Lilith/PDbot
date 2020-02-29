try:
    import flask, gevent
    del(flask, gevent)
except:
    import os
    os.system("pip3 install flask gevent")

from gevent.pywsgi import WSGIServer
from flask import Flask

app=Flask(__name__)

def html_format(file):
    with open(file) as f:
        return eval(f"f'''"+f.read()+"'''") 

@app.route("/")
def index():
    f=open("./index.html")
    return f.read();f.close()

@app.route("/<path:filepath>")
def page_loader(filepath):
    try:
        return html_format("./"+filepath)
    except Exception as e:
        return str(e)

WSGIServer(('0.0.0.0',9000), app).serve_forever()