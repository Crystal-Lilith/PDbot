try:
    import flask
    del(flask)
except:
    import os
    os.system("pip3 install flask")

from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    with open("./index.html") as f:
        return f.read()

@app.route("/<path:filepath>")
def page_loader(filepath):
    with open("./"+filepath) as f:
        return f.read()

app.run("0.0.0.0", 9000)
