from flask import Flask, url_for, render_template
from gevent.pywsgi import WSGIServer

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

app.static('/static', './static')
for filename in listdir('./static'):
    app.url_for('static', filename=filename) == f'/static/{filename}'

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except FileNotFoundError:
        return "No index.html file"

@app.route('/contact')
def contact():
    try:
        return render_template('contact.html')
    except FileNotFoundError:
        return "No Contact.html file"
    
@app.route('/dashboard')
def dashboard():
    try:
        return html_format('templates/dashboard.html')
    except FileNotFoundError:
        return "No dashboard.html file"

# @app.route("/<path:filepath>")
# def page_loader(filepath):
#     return html_format("./"+filepath)

WSGIServer(('0.0.0.0', 80), app, keyfile='keys/private.key', certfile='keys/certificate.crt').serve_forever()
