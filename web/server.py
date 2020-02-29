from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    with open("./index.html") as f:
        return f.read()

@app.route("/<path>")
def page_loader(path):
    with open("./"+path) as f:
        return f.read()

app.run("0.0.0.0", 9000)
