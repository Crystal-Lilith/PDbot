import os
from flask import Flask, url_for, redirect, render_template
from gevent.pywsgi import WSGIServer

app=Flask(__name__)

app.secret_key = b'Y\xd9\x8c\xcc\x8e\x16\x8d\x94\x93{/\xa2\x16\x88\t"\x11j\xc3/\xb9\xf9ra'

def html_format(file):
    try:
        with open(file) as f:
            if file.lower().endswith(".css"):
                return f.read()
            try:
                return eval(f"f'''"+f.read().replace("{", "|~~").replace("}", "~~|").replace("$>", "{").replace("}", "<$")+"'''").replace("|~~", "{").replace("~~|", "}")
            except Exception as e: # Catching all errors so we can have this working no matter what
                print(e)
                return f.read()
    except FileNotFoundError:
        return "The page you were looking for could not be found, is it valid?", 404

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except:
        return 'Unable to find index.html'
@app.route('/contact')
def contact():
    try:
        return render_template('contact.html')
    except:
        return 'Unable to find contact.html'

@app.route('/about')
def about():
    try:
        return render_template('about.html')
    except:
        return 'Unable to find about.html'

@app.route("/commit", methods=['POST'])
def commit_update():
    os.system("bash stop.sh")
    return ''

@app.route('/apply')
def apply(): 
    try:
        return render_template('apply.html')
    except:
        return 'Unable to find apply.html'

# @app.route("/<path:filepath>")
# def page_loader(filepath):
#     return html_format("./"+filepath)

WSGIServer(('0.0.0.0', 8080), app).serve_forever()
