from flask import Flask, url_for, render_template
from flask_discord import DiscordOAuth2Session
from gevent.pywsgi import WSGIServer
import os

app=Flask(__name__)

app.config["DISCORD_CLIENT_ID"] = os.environ.get('CLIENT_ID')
app.config["DISCORD_CLIENT_SECRET"] = os.environ.get('CLIENT_SECRET')
app.config["DISCORD_REDIRECT_URI"] = "https://pden.net"
discord = DiscordOAuth2Session(app)

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
        user = discord.fetch_user()
        return html_format('templates/dashboard.html', user=user)

    except FileNotFoundError:
        return "No index.html file"

    except:
        class user:
            name = 'Login'
        return html_format('templates/dashboard.html', user=user)

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

@app.route('/login')
def login():
    try:
        return discord.create_session()
    except FileNotFoundError:
        return "No login.html file"

# @app.route("/<path:filepath>")
# def page_loader(filepath):
#     return html_format("./"+filepath)

WSGIServer(('0.0.0.0', 8080), app).serve_forever()
