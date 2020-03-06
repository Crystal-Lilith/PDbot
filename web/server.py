from gevent.pywsgi import WSGIServer
from flask import Flask, url_for, render_template

app=Flask(__name__)

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
    except FileNotFoundError:
        return "No index.html file"

@app.route('/contact')
def contact():
    try:
        return render_template('Contact.html')
    except FileNotFoundError:
        return "No Contact.html file"
    
@app.route('/dashboard')
def dashboard():
    try:
        return html_format('templates/dashboard.html')
    except FileNotFoundError:
        return "No dashboard.html file"

@app.route("/<path:filepath>")
def page_loader(filepath):
    return html_format("./"+filepath)

WSGIServer((ssl_context='adhoc', '0.0.0.0', 9000), app).serve_forever()
