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
    try:
        with open(file) as f:
            try:
                return eval(f"f'''"+f.read()+"'''")
            except NameError as e:
                e=e[:-16][6:]
                exec(f"{e} = '{e}'")
                return eval(f"f'''"+f.read()+"'''")
            except: # Catching all errors so we can have this working no matter what
                return f.read()
    except FileNotFoundError:
        return "The page you were looking for could not be found, is it valid?", 404

@app.route("/")
def index():
    try:
        with open("./index.html") as f:
            return f.read()
    except FileNotFoundError:
        return "No index.html file"

@app.route("/<path:filepath>")
def page_loader(filepath):
    return html_format("./"+filepath)

WSGIServer(('0.0.0.0',9000), app).serve_forever()